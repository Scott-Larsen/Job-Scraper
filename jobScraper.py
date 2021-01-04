# If you get an error about chromedriver versions run the following command and download the corresponding version of chromdriver as chrome (https://chromedriver.chromium.org/downloads).  Save chromedriver to project folder"
# brew upgrade chromedriver

# import requests
# from bs4 import BeautifulSoup
from time import sleep
import pytz
from random import randint
import smtplib
import os.path
import pytz
from datetime import datetime
from dateutil import parser
from yaml import safe_load
from sys import path
from linkedInJobBoardScraper import linkedInMetaSearch
from pythonDotOrgJobBoardScraper import pythonDotOrgMetaSearch
from zipRecruiterJobBoardScraper import zipRecruiterMetaSearch
from credentials import USER, PASS, EMAIL


config = safe_load(open(os.path.join(path[0], "config.yml")))

searchPhrases = config["searchPhrases"]
URLs = config["URLs"]

listings = []

scrapedJobsFilename = "scrapedJobs.txt"


def main():
    try:
        jobs = {}
        scrapedJobs = []

        scrapedJobs = readInReturnDelimitedTextFileToDataStructure(
            "", scrapedJobsFilename
        )

        for URL in URLs:
            if "www.linkedin.com" in URL:
                (jobs, scrapedJobs) = linkedInMetaSearch(URL, jobs, scrapedJobs)
            if "www.python.org" in URL:
                (jobs, scrapedJobs) = pythonDotOrgMetaSearch(URL, jobs, scrapedJobs)
            if "www.ziprecruiter.com" in URL:
                (jobs, scrapedJobs) = zipRecruiterMetaSearch(
                    URL, jobs, scrapedJobs
                )  # -> Tuple[Dict[int, str, str, str, str, str, str, str], List[str]]

        writeOutDataStructureToReturnDelimitedTextFile(
            "", "scrapedJobs.txt", scrapedJobs
        )

        for id in jobs.keys():
            score, link, title, company, datePosted, location, fullText = (
                jobs[id][0],
                jobs[id][1],
                jobs[id][2],
                jobs[id][3],
                jobs[id][4],
                jobs[id][5],
                jobs[id][6],
            )

            print(f"\nEvaluating {title} at {company} ({id}).")

            try:
                if "yesterday" in datePosted:
                    ageInDays = 1
                elif "just now" in datePosted:
                    ageInDays = 0
                elif "hours ago" in datePosted or "hour ago" in datePosted:
                    ageInDays = float(datePosted.split()[0]) / 24
                else:
                    datetimePosted = parser.parse(datePosted)

                    age = datetime.now().timestamp() - datetimePosted.timestamp()
                    ageInDays = int(age / 24 / 60 / 60)
            except parser.ParserError as e:
                print(f"{e}: {datePosted} couldn't be parsed properly from {link}")
                ageInDays = 0

            # print(f"{ageInDays = }")

            ageReduction = int(ageInDays ** 2)
            score -= ageReduction
            if ageReduction > 0:
                print(
                    f"... docking {ageReduction} from the score ({score}) because the listing is {ageInDays} days old."
                )

            for searchPhrase in searchPhrases.keys():
                if searchPhrase.lower() in title.lower():

                    scoreAdjustment = 2 * searchPhrases[searchPhrase]
                    score += scoreAdjustment
                    if scoreAdjustment > 0:
                        scoreAdjustment = "+" + str(scoreAdjustment)
                    print(
                        f"... {scoreAdjustment} points ({score}) for {searchPhrase} being in {title}."
                    )
                if searchPhrase.lower() in fullText.lower():
                    scoreAdjustment = searchPhrases[searchPhrase]
                    score += scoreAdjustment
                    if scoreAdjustment > 0:
                        scoreAdjustment = "+" + str(scoreAdjustment)
                    print(
                        f"... {scoreAdjustment} points ({score}) for {searchPhrase} being in the text of the listing."
                    )
            jobs[id][0] = score

        print("\n")

        sendEMail(jobs)

    except:
        sendEMail("Not working")


def readInReturnDelimitedTextFileToDataStructure(directory: str, filename: str):
    listFromFile = []
    dictionaryFromFile = {}

    if os.path.exists(directory + filename):
        print(f"Opening {filename} and writing it into a data structure....\n")

        with open(directory + filename, "r") as filehandle:
            for line in filehandle:
                currentLine = line[:-1]
                if " " in currentLine:
                    currentLine = currentLine.split()
                    dictionaryFromFile[currentLine[0]] = int(currentLine[1])
                else:
                    listFromFile.append(currentLine)
    else:
        print(f"{directory + filename} doesn't exist")
    if len(listFromFile) >= len(dictionaryFromFile):
        dataStructureToReturn = listFromFile
    else:
        dataStructureToReturn = dictionaryFromFile
    print(f"Loaded in {filename}.\n")
    return dataStructureToReturn


def writeOutDataStructureToReturnDelimitedTextFile(
    directory, filename, dataStructureToBeWrittenOut
):
    if os.path.exists(directory + filename):
        print(f"Writing out list to {filename}....\n")
        with open(directory + filename, "w") as filehandle:
            if isinstance(dataStructureToBeWrittenOut, list):
                filehandle.writelines(
                    f"{item}\n" for item in dataStructureToBeWrittenOut
                )
            elif isinstance(dataStructureToBeWrittenOut, dict):
                filehandle.writelines(
                    f"{key} {dataStructureToBeWrittenOut[key]}\n"
                    for key in dataStructureToBeWrittenOut.keys()
                )


def sendEMail(jobs):
    jobs = jobs
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(USER, PASS)

    subject = f"Job Scraper Results"

    if jobs != "Not working":
        body = ""
        jobIDs = [
            jobs[x] for x in sorted(jobs.keys(), key=lambda x: jobs[x][0], reverse=True)
        ][:25]
        for jobID in jobIDs:
            body += f"({jobID[0]}) {jobID[2]} at {jobID[3]} in {jobID[5]} posted {jobID[4][5:11]}\n{jobID[1]}\n... {jobID[6][100:500]} ...\n\n\n"
        if len(body) == 0:
            body += "\nNo results."
        body = body.encode("ascii", "ignore").decode("ascii")  # last working
        msg = f"Subject: {subject}\n\n{body}"
    else:
        msg = f"Subject: {subject} - {jobs}\n\n{jobs}"

    msg = f"From: {EMAIL}\r\nTo: {EMAIL}\r\n" + msg

    server.sendmail(EMAIL, EMAIL, msg)

    timeZone_NY = pytz.timezone("America/NEW_York")
    datetime_NY = datetime.now(timeZone_NY)
    print(f"E-mail was sent at {datetime_NY.strftime('%H:%M')}.\n\n")

    server.quit()


if __name__ == "__main__":
    main()
