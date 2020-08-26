import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
from pythonDotOrgIndividualJobScraper import pythonDotOrgIndividualJobScraper



def pythonDotOrgMetaSearch(URL, jobs, scrapedJobs):

    headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:73.0) Gecko/20100101 Firefox/73.0'}

    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    jobsOrderedList = soup.find("ol", class_="list-recent-jobs")

    print("Doing a metascrape of jobs on pythonDotOrg:")
    listings = jobsOrderedList.find_all("li")
    
    for listing in listings:

        id = "po_" + relativeLink[-5:-1]

        if id in scrapedJobs:
            break
        else:
            scrapedJobs.insert(0, id)

        score = 1000

        fullLink = listing.find("a")
        # print(f"{fullLink = }")
        relativeLink = fullLink.get('href')
        # print(f"{relativeLink = }")

        link = "https://www.python.org" + relativeLink
        # print(f"{link = }")
        
        # if link in scrapedJobs:
        #     break
        # else:
        #     scrapedJobs.insert(0, link)

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
        # print(f"{location = }")

        print(f"Scraping {title} at {company}")

        fullText = pythonDotOrgIndividualJobScraper(link)

        sleep(randint(1, 10))

        # jobs[id] = [score, id, title, company, link, datePosted, location]
        jobs[id] = [score, link, title, company, datePosted, location, fullText]

    # return score, id, title, company, link, datePosted, location
    return jobs, scrapedJobs



# jobs = {}
# URL = "https://www.python.org/jobs/"

# pythonDotOrgMetaSearch(URL, jobs)