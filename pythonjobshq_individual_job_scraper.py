import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint


def linkedInIndividualJobScraper(link):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:73.0) Gecko/20100101 Firefox/73.0"
    }
    page = requests.get(link, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    try:
        full_text = soup.find("div", class_="show-more-less-html__markup").get_text()

        if soup.find("figcaption", class_="closed-job__flavor--closed"):
            full_text = "No longer accepting applications " + full_text

    except AttributeError as e:
        print(f"{e}: {link} doesn't have any job description")

    sleep(randint(1, 10))

    return full_text


# linkedInIndividualJobScraper("https://www.linkedin.com/jobs/view/1969468384")
