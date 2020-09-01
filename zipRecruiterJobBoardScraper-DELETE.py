import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
# from zipRecruiterIndividualJobScraper import zipRecruiterIndividualJobScraper

def zipRecruiterMetaSearch(URL):#, jobs, scrapedJobs):
    # requires Javascript
    headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:73.0) Gecko/20100101 Firefox/73.0'}
    page = requests.get(URL, headers = headers)
    # session = requests.Session()
    # page = session.get(URL, headers = headers)
    # res1 = session.post(url1, post_data)
    # res2 = session.get(url2)
    soup = BeautifulSoup(page.content, 'html.parser')

    print(soup.prettify())
    
    """
    jobsOrderedList = soup.find("ol", class_="list-recent-jobs")

    print("Doing a metascrape of jobs on zipRecruiter:")
    listings = jobsOrderedList.find_all("li")
    
    for listing in listings:

        id = "po_" + relativeLink[-5:-1]
        if id in scrapedJobs:
            break
        else:
            scrapedJobs.insert(0, id)

        score = 1000

        fullLink = listing.find("a")
        relativeLink = fullLink.get('href')
        link = "https://www.python.org" + relativeLink

        title = fullLink.contents[0]

        company = listing.find("a").next_sibling.next_sibling.strip()

        datePosted = listing.find("time").get('datetime')

        location = listing.find("span", class_="listing-location").findChild().contents[0]

        print(f"Scraping {title} at {company}")

        fullText = zipRecruiterIndividualJobScraper(link)

        sleep(randint(1, 10))

        jobs[id] = [score, link, title, company, datePosted, location, fullText]

    return jobs, scrapedJobs
    """

zipRecruiterMetaSearch("https://www.ziprecruiter.com/candidate/search?radius=5000&days=1&search=Python&location=")