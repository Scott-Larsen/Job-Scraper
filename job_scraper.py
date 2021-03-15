# If you get an error about chromedriver missing (or mismatched versions),
# download the same version of chromedriver as you have of Chrome on your
# computer. You might as well make sure Chrome is updated and then get that
# version's chromedriver from https://chromedriver.chromium.org/downloads .

import smtplib
import os.path
import pytz
from datetime import datetime
from dateutil import parser
from linkedin_job_board_scraper import linkedin_meta_search
from pythondotorg_job_board_scraper import pythondotorg_meta_search
from ziprecruiter_job_board_scraper import ziprecruiter_meta_search
from credentials import EMAIL, PASS
from config import search_phrases, URLs

listings = []

scraped_jobs_filename = "scraped_jobs.txt"


def main():
    """Scrapes job sites and sends e-mail with best job listings ranked by keywords"""
    try:
        jobs = {}
        scraped_jobs = []

        scraped_jobs = read_from_text_file("", scraped_jobs_filename)

        for URL in URLs:
            if "www.linkedin.com" in URL:
                (jobs, scraped_jobs) = linkedin_meta_search(URL, jobs, scraped_jobs)
            if "www.python.org" in URL:
                (jobs, scraped_jobs) = pythondotorg_meta_search(URL, jobs, scraped_jobs)
            if "www.ziprecruiter.com" in URL:
                (jobs, scraped_jobs) = ziprecruiter_meta_search(URL, jobs, scraped_jobs)

        write_to_text_file("", "scraped_jobs.txt", scraped_jobs)

        for id in jobs.keys():
            score, link, title, company, date_posted, location, full_text = jobs[id]

            print(f"\nEvaluating {title} at {company} ({id}).")

            try:
                if "yesterday" in date_posted:
                    age_in_days = 1
                elif "just now" in date_posted:
                    age_in_days = 0
                elif "hours ago" in date_posted or "hour ago" in date_posted:
                    age_in_days = float(date_posted.split()[0]) / 24
                else:
                    datetimePosted = parser.parse(date_posted)
                    age = datetime.now().timestamp() - datetimePosted.timestamp()
                    age_in_days = int(age / 24 / 60 / 60)
            except parser.ParserError as e:
                print(f"{e}: {date_posted} couldn't be parsed properly from {link}")
                age_in_days = 0
            age_reduction = int(age_in_days ** 2)
            score -= age_reduction
            if age_reduction > 0:
                print(
                    f"... docking {age_reduction} from the score ({score}) \
                    because the listing is {age_in_days} days old."
                )

            for search_phrase in search_phrases.keys():
                if search_phrase.lower() in title.lower():

                    score_adjustment = 2 * search_phrases[search_phrase]
                    score += score_adjustment
                    if score_adjustment > 0:
                        score_adjustment = "+" + str(score_adjustment)
                    print(
                        f"... {score_adjustment} points ({score}) for \
                            {search_phrase} being in {title}."
                    )
                if search_phrase.lower() in full_text.lower():
                    score_adjustment = search_phrases[search_phrase]
                    score += score_adjustment
                    if score_adjustment > 0:
                        score_adjustment = "+" + str(score_adjustment)
                    print(
                        f"... {score_adjustment} points ({score}) for {search_phrase} \
                            being in the text of the listing."
                    )
            jobs[id][0] = score

        print("\n")

        send_email(jobs)

    except Exception as e:
        send_email(f"Not working: {e}")  # ".message}, {e.args}")


def read_from_text_file(directory: str, filename: str):
    """Reads in dictionaries and lists from text file"""
    list_from_file = []
    dictionaryFromFile = {}

    if not os.path.exists(directory + filename):
        with open(directory + filename, "w") as filehandle:
            pass

    print(f"Opening {filename} and writing it into a data structure....\n")
    with open(directory + filename, "r") as filehandle:
        for line in filehandle:
            current_line = line[:-1]
            if " " in current_line:
                current_line = current_line.split()
                dictionaryFromFile[current_line[0]] = int(current_line[1])
            else:
                list_from_file.append(current_line)

    if len(list_from_file) >= len(dictionaryFromFile):
        data_structure_to_return = list_from_file
    else:
        data_structure_to_return = dictionaryFromFile
    print(f"Loaded in {filename}.\n")

    return data_structure_to_return


def write_to_text_file(directory, filename, data_structure_to_be_written_out):
    """Writes dictionaries and lists out to text file"""
    if os.path.exists(directory + filename):
        print(f"Writing out list to {filename}....\n")
        with open(directory + filename, "w") as filehandle:
            if isinstance(data_structure_to_be_written_out, list):
                filehandle.writelines(
                    f"{item}\n" for item in data_structure_to_be_written_out
                )
            elif isinstance(data_structure_to_be_written_out, dict):
                filehandle.writelines(
                    f"{key} {data_structure_to_be_written_out[key]}\n"
                    for key in data_structure_to_be_written_out.keys()
                )


def send_email(jobs):
    """Send an e-mail with the top-ranked jobs"""
    jobs = jobs
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(EMAIL, PASS)

    subject = f"Job Scraper Results"

    if jobs != "Not working":
        body = ""
        job_ids = [
            jobs[x] for x in sorted(jobs.keys(), key=lambda x: jobs[x][0], reverse=True)
        ][:25]
        for jobID in job_ids:
            score, link, title, company, date_posted, location, full_text = jobID
            body += f"({score}) {title} at {company} in {location} posted \
                {date_posted[5:11]}\n{link}\n... {full_text[100:500]} ...\n\n\n"
        if len(body) == 0:
            body += "\nNo results."
        body = body.encode("ascii", "ignore").decode("ascii")  # last working
        msg = f"Subject: {subject}\n\n{body}"
    else:
        msg = f"Subject: {subject} - {jobs}\n\n{jobs}"

    msg = f"From: {EMAIL}\r\nTo: {EMAIL}\r\n" + msg

    server.sendmail(EMAIL, EMAIL, msg)

    timezone_ny = pytz.timezone("America/NEW_York")
    datetime_ny = datetime.now(timezone_ny)
    print(f"E-mail was sent at {datetime_ny.strftime('%H:%M')}.\n\n")

    server.quit()


if __name__ == "__main__":
    main()
