import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint


def pythondotorg_individual_job_scraper(link):
    """Does detailed scrape of each job listing to return the full text of the listing"""

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:73.0) Gecko/20100101 Firefox/73.0"
    }
    page = requests.get(link, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    full_text = soup.find("div", class_="job-description").get_text()

    sleep(randint(1, 10))

    return full_text
