import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
from pythondotorg_individual_job_scraper import pythondotorg_individual_job_scraper


def pythondotorg_meta_search(URL, jobs, scraped_jobs):
    """Does a meta search of the job board, reaches out to individual job scraper and returns job details"""

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:73.0) Gecko/20100101 Firefox/73.0"
    }
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    jobsOrderedList = soup.find("ol", class_="list-recent-jobs")

    print("\nDoing a metascrape of jobs on pythonDotOrg:")
    listings = jobsOrderedList.find_all("li")

    for listing in listings:

        fullLink = listing.find("a")
        relativeLink = fullLink.get("href")
        link = "https://www.python.org" + relativeLink

        id = "po_" + relativeLink[-5:-1]
        if id in scraped_jobs:
            break
        else:
            scraped_jobs.insert(0, id)

        score = 1000

        title = fullLink.contents[0]

        company = listing.find("a").next_sibling.next_sibling.strip()

        date_posted = listing.find("time").get("datetime")

        location = (
            listing.find("span", class_="listing-location").findChild().contents[0]
        )

        print(f"Scraping {title} at {company}")

        full_text = pythondotorg_individual_job_scraper(link)

        sleep(randint(1, 10))

        jobs[id] = [score, link, title, company, date_posted, location, full_text]

    return jobs, scraped_jobs