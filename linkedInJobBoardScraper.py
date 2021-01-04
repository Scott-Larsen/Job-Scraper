import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
from typing import Tuple, Dict, List
from linkedInIndividualJobScraper import linkedInIndividualJobScraper


def linkedInMetaSearch(
    URL: str, jobs: dict, scrapedJobs: list
) -> Tuple[Dict[int, str], List[str]]:

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:73.0) Gecko/20100101 Firefox/73.0"
    }
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    print("\nDoing a metascrape of jobs on LinkedIn:")
    listings = soup.find_all("li", class_="result-card")

    for listing in listings:

        id = "li_" + listing.get("data-id")
        if id in scrapedJobs:
            break
        else:
            scrapedJobs.insert(0, id)

        score = 1000

        link = listing.find("a").get("href")

        title = listing.find("h3", class_="job-result-card__title").contents[0]

        try:
            company = listing.find("a", class_="result-card__subtitle-link").contents[0]
        except AttributeError as e:
            company = None
            print(f"{e} - No company name.")

        link = listing.find("a").get("href")

        datePosted = listing.find("time").get("datetime")

        location = listing.find("span", class_="job-result-card__location").contents[0]

        print(f"Scraping {title} at {company}")

        fullText = linkedInIndividualJobScraper(link)

        sleep(randint(1, 10))

        jobs[id] = [score, link, title, company, datePosted, location, fullText]

    return jobs, scrapedJobs
