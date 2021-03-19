import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
from urllib.request import Request, urlopen


def ziprecruiter_individual_job_scraper(link):
    """Does detailed scrape of each job listing to return the full text of the listing"""

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:73.0) Gecko/20100101 Firefox/73.0"
    }

    forwardedLink = Request(link, headers=headers)
    try:
        forwardedLinkText = urlopen(forwardedLink, timeout=10).read()

        if (
            b"linkedin.com/jobs/view/" in forwardedLinkText
            or b"dice.com/jobs/detail/" in forwardedLinkText
        ):

            # forwardedLinkURL = urlopen(forwardedLink).read()
            # print(f"{forwardedLinkURL = }")
            # forwardedLinkURL = s.decode("utf-8")
            # print(f"{forwardedLinkURL = }")
            # forwardedLinkURL = s.split("http")
            # print(f"{forwardedLinkURL = }")
            # forwardedLinkURL = s[1]
            # forwardedLinkURL = s.split("'")
            # forwardedLinkURL = s[0]
            # forwardedLinkURL = "http" + s

            print(f"This job is from another site:\n{forwardedLinkURL}")

            return "", "99999 hours ago"

    except:
        print(f"Server timed out trying to reach {link}\n")
        return "", "99999 hours ago"

    page = requests.get(link, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")

    try:
        full_text = (
            soup.find("div", class_="jobDescriptionSection")
            .get_text(separator=" ")
            .strip()
        )
    except AttributeError as e:
        print(f"{e}: no detailed job description for {link}")
        full_text = False

    try:
        classData = soup.find_all("span", class_="data")
        date_posted = classData[-1].get_text().strip()
        if date_posted == 0:
            print(f"Found date_posted as {date_posted}\n")
            print(soup.get_text())
    except (AttributeError, IndexError) as e:
        print(f"{e}: no date_posted for {link}")
        date_posted = "99999 hours ago"

    sleep(randint(10, 60))

    return full_text, date_posted


# link = "https://www.ziprecruiter.com/ek/l/AALT21NCHOs3JVdIO1GNFXZ2dAp6P89M8v0UahfYMqaQflHMDUVOCCfvmdzdesWpig8c3rHgnXZnYGq48ZyFxW5TOKSETqyulmOXP3nGWYmwIRHCDS9aiQ3VIbQsXjxmTOPbAXnfAzqw4A9r_pzf7KZm30MpJRoNaCUKPDz5Gu0fmpZg8WPVQOHbmiUwBNk"
# ziprecruiter_individual_job_scraper(link)