import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
from linkedInIndividualJobScraper import linkedInIndividualJobScraper
from datetime import datetime


def linkedInMetaSearch(URL):

    headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:73.0) Gecko/20100101 Firefox/73.0'}

    print("")

    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    # print(soup.prettify())
    # promoted = soup.find_all(text = 'Promoted')
    # # listing.findAll(text='Promoted')
    # print(promoted)

# linkedInMetaSearch("https://www.linkedin.com/jobs/search/?f_TPR=r86400&geoId=103644278&keywords=python%20developer%20-senior%20-sr%20-mid-senior&location=United%20States%22")

    # li class="result-card
    # soup.find_all("a", class_="sister")
    listings = soup.find_all("li", class_="result-card")

    # print(listings[0].prettify())

    

    for listing in listings:

        # print(listing)

        score = 1000

        id = "li" + listing.get("data-id")
        # print(jobID)

        # TODO check against a central list to make sure it's not a duplicate

        title = listing.find('h3', class_="job-result-card__title").contents[0]
        # print(jobTitle)

        company = listing.find('a', class_="result-card__subtitle-link").contents[0]
        # print(f"\n\n{company}\n\n")

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

        print(f"\nEvaluating {title} at {company}.")
        # print(link)

        datetimePosted = datetime.strptime(datePosted, '%Y-%m-%d')
        # print(f"{datetimePosted = }")
        age = datetime.now().timestamp() - datetimePosted.timestamp()
        # print(f"{age = }")
        ageInDays = int(age / 24 / 60 / 60)
        # print(f"{ageInDays = }")
        ageReduction = ageInDays ** 2
        score -= ageReduction
        if ageReduction > 0:
            print(f"... docking {ageReduction} from the score ({score}) because the listing is {ageInDays} days old.")
        # age = (datetimePosted - datetime.now())
        # print(age)

        linkedInIndividualJobScraper(title, link, score)

        # print(soup.prettify())
        # print(listings[0].prettify())

        # print("Finished this round.")

        sleep(randint(1, 10))

    return score, id, title, company, link, datePosted, location
