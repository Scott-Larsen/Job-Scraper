import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
import webbrowser


def checkSeniorityLevel(URL):

    # URL = "https://www.linkedin.com/jobs/view/python-developer-at-ateeca-inc-1986278697/?refId=1c0747a8-d317-4f3f-8b46-d126e35e61f3&position=1&pageNum=0&trk=public_jobs_job-result-card_result-card_full-click"

    headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:73.0) Gecko/20100101 Firefox/73.0'}

    print("")

    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    seniorityLevel = soup.find('h3', text = 'Seniority level').next_element.next_element.text
    print(seniorityLevel)

    if seniorityLevel != 'Mid-Senior level':
        pass

    elif soup.find('p', text = 'You applied on'):
        pass

    else:
        webbrowser.open(URL, new = 2)

    # # jobDetails = soup.find('div', id='job-details')
    # jobDetails = soup.find('section', class_="description").get_text()
    # print(jobDetails)
    # # print(jobDetails.prettify())

    print("")

    # sleep(randint(1, 3))

