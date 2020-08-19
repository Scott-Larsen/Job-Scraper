import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
from diceIndividualJobScraper import diceIndividualJobScraper
# from datetime import datetime


def diceMetaSearch(URL, jobs):

    headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:73.0) Gecko/20100101 Firefox/73.0'}

    print("")

    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    # print(soup.prettify())
    # promoted = soup.find_all(text = 'Promoted')
    # # listing.findAll(text='Promoted')
    # print(promoted)

# diceMetaSearch("https://www.dice.com/jobs/search/?f_TPR=r86400&geoId=103644278&keywords=python%20developer%20-senior%20-sr%20-mid-senior&location=United%20States%22")

    # li class="result-card
    # soup.find_all("a", class_="sister")

    print("Doing a metascrape of jobs on dice.\n")
    listings = soup.find_all("li", class_="result-card")

    # print(listings[0].prettify())

    for listing in listings:

        # print(listing)

        score = 1000

        id = "li_" + listing.get("data-id")
        # print(jobID)

        # TODO check against a central list to make sure it's not a duplicate

        title = listing.find('h3', class_="job-result-card__title").contents[0]
        # print(jobTitle)

        try:
            company = listing.find('a', class_="result-card__subtitle-link").contents[0]
            # print(f"\n\n{company}\n\n")
        except AttributeError as e:
            company = None
            print(f"{e} - No company name.")

        link = listing.find("a").get('href')
        # print(jobLink)

        datePosted = listing.find("time").get('datetime')

        location = listing.find("span",  class_="job-result-card__location").contents[0]
        # print(location)

        # try:
        #     promoted = listing.findAll(text='Promoted')
        #     print(promoted)
        # except AttributeError as e:
        #     # print(e + "\n")
        #     print(f"{e} - this is not Promoted.")

        # age = (datetimePosted - datetime.now())
        # print(age)

        print(f"Scraping {title} at {company}\n")

        diceIndividualJobScraper(link, score)

        # print(soup.prettify())
        # print(listings[0].prettify())

        # print("Finished this round.")

        sleep(randint(1, 10))

        jobs[id] = [score, id, title, company, link, datePosted, location]

    # return score, id, title, company, link, datePosted, location
    return jobs
