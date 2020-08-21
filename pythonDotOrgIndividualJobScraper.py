import requests
from bs4 import BeautifulSoup, NavigableString, Tag
from time import sleep
from random import randint
import webbrowser
# from jobScraper import searchPhrases


def pythonDotOrgIndividualJobScraper(link, score):

    headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:73.0) Gecko/20100101 Firefox/73.0'}

    # print("")

    page = requests.get(link, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    # print(soup.prettify())

    # jobDetailsMeta = soup.find("div", class_="job-description")
    # # print(f"{jobDetailsMeta}")

    # jobDetails = jobDetailsMeta.find_all("h2")
    # # print(jd)

    # for jobDetail in jobDetails:
    #     print(jobDetail.contents[0])
    #     # jobTitle = jobDetail.contents[0].findChild()

    #     # print(jobTitle)

    # jobDescription = soup.find(text = "Job Description")# next_element.next_element
    # print(f"{jobDescription = }")
    # jobDetails = str(soup.find("div", class_="job-description").contents)

    jobDetails = soup.find("div", class_="job-description")#.contents
    # print(f"{jobDetails = }")

    jobDescription = {}
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
                
            # else:
            #     print("Reached else")
            #     jobDescription[jobDetail] = "\n".join(jobDetailText)
    
    # print(jobDescription['Contact Info'])

    # print(jobDescription.items())
    # print(jobDescription)

                # print(f"{nextNode.get_text(strip=True) = }")
                # print(f"{nextNode.get_text(strip=True).strip() = }")

    # Job Title, Job Description, Restrictions, Requirements, About the Company, Contact Info

    # for header in jobDetails.find_all('h2'):
    #     print(f"\n\n{header = }\n\n")
    #     nextNode = header
    #     while True:
    #         nextNode = nextNode.nextSibling
    #         if nextNode is None:
    #             break
    #         if isinstance(nextNode, NavigableString):
    #             print (nextNode.strip())
    #         if isinstance(nextNode, Tag):
    #             if nextNode.name == "h2":
    #                 break
    #             print (nextNode.get_text(strip=True).strip())

    # currentDetail = False
    # currentDetailText = ""
    # for markup in jobDetails:
    #     print(markup)
        # print(markup + "\n")
        # if "h2" in markup:
        #     print(markup)
        #     if currentDetail:
        #         str(currentDetail) = currentDetailText
        #     currentDetail = markup
        # else:
        #     if currentDetail




    
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

    return score, jobDescription

# link = "https://www.python.org/jobs/4793/"
# score = 1000
# pythonDotOrgIndividualJobScraper(link, score)

