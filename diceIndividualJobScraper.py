import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
import webbrowser

# from jobScraper import searchPhrases


def diceIndividualJobScraper(link, score):

    # URL = "https://www.dice.com/jobs/view/python-developer-at-ateeca-inc-1986278697/?refId=1c0747a8-d317-4f3f-8b46-d126e35e61f3&position=1&pageNum=0&trk=public_jobs_job-result-card_result-card_full-click"

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:73.0) Gecko/20100101 Firefox/73.0"
    }

    page = requests.get(link, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")

    try:
        seniorityLevel = soup.find(
            "h3", text="Seniority level"
        ).next_element.next_element.text

        if seniorityLevel == "Mid-Senior level":
            score -= 25
            print(
                f"... docking 25 points (down to {score}) for Seniority Level being Mid-Senior"
            )
    except AttributeError as e:
        print(f"{e} - there isn't a 'Seniority Level' listed.")

    if soup.find("p", text="You applied on"):
        score -= 100
        print(f"... already applied, docking 100 points (down to {score})")

    sleep(randint(1, 10))

    return score

