import requests
from bs4 import BeautifulSoup

def zipRecruiterMetaSearch(URL):#, jobs, scrapedJobs):
    # requires Javascript
    headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:73.0) Gecko/20100101 Firefox/73.0'}
    page = requests.get(URL, headers = headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    print(soup.prettify())

# zipRecruiterMetaSearch("https://www.ziprecruiter.com/candidate/search?radius=5000&days=1&search=Python&location=")