import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
from linkedInIndividualJobScraper import checkSeniorityLevel


URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=103644278&keywords=python%20developer%20-senior%20-sr%20-mid-senior&location=United%20States"

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:73.0) Gecko/20100101 Firefox/73.0'}

print("")

page = requests.get(URL, headers = headers)

soup = BeautifulSoup(page.content, 'html.parser')

# li class="result-card
# soup.find_all("a", class_="sister")
listings = soup.find_all("li", class_="result-card")

for listing in listings:

    score = 1000

    # listing = listings[0]

    # print(listing.prettify())

    jobTitle = listing.find('h3', class_="job-result-card__title").contents[0]
    # print(jobTitle)
    print(f"Evaluating {jobTitle}....")

    jobTitleDisqualifications = ['Lead Python Developer', 'Lead Developer', 'Architect']
    for jobTitleDisqualification in jobTitleDisqualifications:
        if jobTitleDisqualification in jobTitle:
            print("... disqualified")
            break

    jobLink = listing.find("a").get('href')
    # print(jobLink)

    # jobID = listing.get("data-id")
    # print(jobID)

    # datePosted = listing.find("time").get('datetime')
    # print(datePosted)

    # location = listing.find("span",  class_="job-result-card__location").contents[0]
    # print(location)

    checkSeniorityLevel(jobLink)

    # print(soup.prettify())
    # print(listings[0].prettify())

    print("Finished this round.")

    sleep(randint(10, 60))

