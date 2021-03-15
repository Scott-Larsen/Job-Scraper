import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
from typing import Tuple, Dict, List
from linkedin_individual_job_scraper import linkedin_individual_job_scraper


def linkedin_meta_search(
    URL: str, jobs: dict, scraped_jobs: list
) -> Tuple[Dict[int, str], List[str]]:
    """Does a meta search of the job board, reaches out to individual job scraper and returns job details"""

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:73.0) Gecko/20100101 Firefox/73.0"
    }
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    print("\nDoing a metascrape of jobs on LinkedIn:")
    listings = soup.find_all("li", class_="result-card")

    for listing in listings:

        id = "li_" + listing.get("data-id")
        if id in scraped_jobs:
            break
        else:
            scraped_jobs.insert(0, id)

        score = 1000

        link = listing.find("a").get("href")

        title = listing.find("h3", class_="job-result-card__title").contents[0]

        try:
            company = listing.find("a", class_="result-card__subtitle-link").contents[0]
        except AttributeError as e:
            company = None
            print(f"{e} - No company name.")

        link = listing.find("a").get("href")

        date_posted = listing.find("time").get("datetime")

        location = listing.find("span", class_="job-result-card__location").contents[0]

        print(f"Scraping {title} at {company}")

        full_text = linkedin_individual_job_scraper(link)

        sleep(randint(1, 10))

        jobs[id] = [score, link, title, company, date_posted, location, full_text]

    return jobs, scraped_jobs
