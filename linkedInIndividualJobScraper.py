import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
# import webbrowser
# from jobScraper import searchPhrases


def linkedInIndividualJobScraper(link):

    # URL = "https://www.linkedin.com/jobs/view/python-developer-at-ateeca-inc-1986278697/?refId=1c0747a8-d317-4f3f-8b46-d126e35e61f3&position=1&pageNum=0&trk=public_jobs_job-result-card_result-card_full-click"
    # URL = 'https://www.linkedin.com/jobs/view/1969468384/?midToken=AQGTKeEYrzL8xA&trk=eml-jobs_applicant_applied-applied_jobs-14-applied_job&trkEmail=eml-jobs_applicant_applied-applied_jobs-14-applied_job-null-hujih%7Eke284e8c%7Eme-null-jobs%7Eview'

    link = '/'.join(link.split('/')[:6])

    headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:73.0) Gecko/20100101 Firefox/73.0'}

    # print("")

    page = requests.get(link, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    # print(soup.prettify())

    fullText = soup.find('div', class_="show-more-less-html__markup").get_text()

    if soup.find('figcaption', class_="closed-job__flavor--closed"):
        fullText = 'No longer accepting applications ' + fullText

    # print(fullText)

    # fullText = soup.find('div', class_='jobs-top-card ember-view')
    # print(fullText)

    # applied = soup.find(string = 'You applied on')

    # if applied:
    #     print('applied')
    # else:
    #     print('not yet applied')

    # fullText = soup.find('div', class_='show-more-less-html__markup').get_text()

    # print(fullText)

    # fullText = soup.find('article', class_='jobs-description__container')
    # print(fullText)

    # for fT in fullText:
    #     print(fT.get_text())
    #     print("\n" * 5)

    # print(soup.prettify())
    
    # try:
    #     seniorityLevel = soup.find('h3', text = 'Seniority level').next_element.next_element.text
    #     # print(seniorityLevel)

    #     if seniorityLevel == 'Mid-Senior level':
    #         score -= 25
    #         print(f"... docking 25 points (down to {score}) for Seniority Level being Mid-Senior")
    # except AttributeError as e:
    #     print(f"{e} - there isn't a 'Seniority Level' listed.")

    # if soup.find('p', text = 'You applied on'):
    #     score -= 100
    #     print(f"... already applied, docking 100 points (down to {score})")

    # # jobDetails = soup.find('div', id='job-details')
    # jobDetails = soup.find('section', class_="description").get_text()
    # print(jobDetails)
    # # print(jobDetails.prettify())

    # print("")

    sleep(randint(1, 10))

    return fullText

# linkedInIndividualJobScraper("https://www.linkedin.com/jobs/view/1969468384/?midToken=AQGTKeEYrzL8xA&trk=eml-jobs_applicant_applied-applied_jobs-14-applied_job&trkEmail=eml-jobs_applicant_applied-applied_jobs-14-applied_job-null-hujih%7Eke284e8c%7Eme-null-jobs%7Eview")
# linkedInIndividualJobScraper("https://www.linkedin.com/jobs/view/1989615471")
# linkedInIndividualJobScraper("https://www.linkedin.com/jobs/view/1969468384")