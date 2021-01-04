import requests
from bs4 import BeautifulSoup


def pythonJobsHQMetaSearch(URL):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:73.0) Gecko/20100101 Firefox/73.0"
    }
    session = requests.Session()
    page = session.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    print(soup.prettify())


pythonJobsHQMetaSearch("https://www.pythonjobshq.com/")
