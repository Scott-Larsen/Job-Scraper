import requests
from bs4 import BeautifulSoup, NavigableString, Tag
from time import sleep
from random import randint
# import webbrowser
# from jobScraper import searchPhrases


def pythonDotOrgIndividualJobScraper(link):

    headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:73.0) Gecko/20100101 Firefox/73.0'}

    # print("")

    page = requests.get(link, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    # print(soup.prettify())

    fullText = soup.find("div", class_="job-description").get_text()
    # print(f"{jobDetailsMeta}")

    # jobDetails = jobDetailsMeta.find_all("h2")
    # # print(jd)

    # for jobDetail in jobDetails:
    #     print(jobDetail.contents[0])
    #     # jobTitle = jobDetail.contents[0].findChild()

    #     # print(jobTitle)

    # jobDescription = soup.find(text = "Job Description")# next_element.next_element
    # print(f"{jobDescription = }")
    # jobDetails = str(soup.find("div", class_="job-description").contents)
    
    """
    jobDetails = soup.find("div", class_="job-description")#.contents
    print(f"{jobDetails = }")

    for header in jobDetails.find_all('h2'):
        jobDetail = header.get_text().strip()
        nextNode = header
        jobDetailText = []
        while True:
            nextNode = nextNode.nextSibling
            if not nextNode: # This writes out the last of the H2 tags and its following contents
                jobDescription[jobDetail] = "\n".join(jobDetailText)
                break
            elif isinstance(nextNode, NavigableString): # Adds non-H2 tags to the text to attach to the text of the H2
                if nextNode.strip():
                    jobDetailText.append(nextNode.strip())
                    pass
            elif isinstance(nextNode, Tag): # Detects the next H2 and writes the compiled text to the previous H2
                if nextNode.name == "h2":
                    jobDescription[jobDetail] = "\n".join(jobDetailText)
                    break
                jobDetailText.append(nextNode.get_text(strip=True))
    """

    sleep(randint(1, 10))

    return fullText

# link = "https://www.python.org/jobs/4793/"
# score = 1000
# pythonDotOrgIndividualJobScraper(link, score)