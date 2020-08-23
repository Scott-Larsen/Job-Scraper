import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
from urllib import parse
from urllib.parse import quote, unquote, urljoin
from pythonDotOrgIndividualJobScraper import pythonDotOrgIndividualJobScraper
# from datetime import datetime


def pythonDotOrgMetaSearch(URL, jobs):

    headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:73.0) Gecko/20100101 Firefox/73.0'}

    print("")

    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    # print(soup.prettify())

    # promoted = soup.find_all(text = 'Promoted')
    # # listing.findAll(text='Promoted')
    # print(promoted)

# pythonDotOrgMetaSearch("https://www.pythonDotOrg.com/jobs/search/?f_TPR=r86400&geoId=103644278&keywords=python%20developer%20-senior%20-sr%20-mid-senior&location=United%20States%22")

    # li class="result-card
    # soup.find_all("a", class_="sister")

    jobsOrderedList = soup.find("ol", class_="list-recent-jobs")

    print("Doing a metascrape of jobs on pythonDotOrg.\n")
    listings = jobsOrderedList.find_all("li")

    # print(listings[0].prettify())
    # print(len(listings))

    # print(listings[0].find("a"))
    
    for listing in listings:

        # print(f"{listing}\n\n")

    #     # print(listing.prettify())

        score = 1000

        fullLink = listing.find("a")
        # print(f"{fullLink = }")
        relativeLink = fullLink.get('href')
        # print(f"{relativeLink = }")

        link = "https://www.python.org" + relativeLink
        # print(f"{link = }")

        id = "po_" + relativeLink[-5:-1]
        # print(f"{id = }")

        # TODO check against a central list to make sure it's not a duplicate

        title = fullLink.contents[0]
        # print(f"{title = }")

        company = listing.find("a").next_sibling.next_sibling.strip()
        # print(f"{company = }")

        datePosted = listing.find("time").get('datetime')
        # print(f"{datePosted = }")
        # print(type(datePosted))

        location = listing.find("span", class_="listing-location").findChild().contents[0]
        print(f"{location = }")

        print(f"Scraping {title} at {company}\n")

        pythonDotOrgIndividualJobScraper(link, score)

        sleep(randint(1, 10))

        print("\n")

        jobs[id] = [score, id, title, company, link, datePosted, location]

    # return score, id, title, company, link, datePosted, location
    return jobs



# jobs = {}
# URL = "https://www.python.org/jobs/"

# pythonDotOrgMetaSearch(URL, jobs)