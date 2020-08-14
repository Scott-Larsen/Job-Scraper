import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
from linkedInJobBoardScraper import linkedInMetaSearch


searchPhrases = {'Lead Python Developer': 50, 'Lead Developer': 50, 'Architect': 50, 'Cloud Technical Solutions Engineer': 50,'Ruby on Rails Fullstack Engineer': 50, 'Ruby on Rails Developer': 50,
'Mid-Senior level': 25, 'Solutions Engineer': 25,
'Application Development': 10, 'Blockchain': 10, 'Crypto': 10, 'Quant': 10, 'ETL Developer': 10
}

listings = []

linkedInURL = "https://www.linkedin.com/jobs/search/?f_TPR=r86400&geoId=103644278&keywords=python%20developer%20-senior%20-sr%20-mid-senior&location=United%20States%22"
# https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=103644278&keywords=python%20developer%20-senior%20-sr%20-mid-senior&location=United%20States"

listings.append(linkedInMetaSearch(linkedInURL, jobs))

# class Job:
#     def __init__(self, score, title, applicationDate, datePosted, location):
#         self.score = score
#         # self.id = id
#         self.title = title
#         self.applicationDate = applicationDate
#         self.datePosted = datePosted
#         self.location = location


# li_123 = Job(51, 'Dev', 'February', 'March', 'Paris')

# print(li_123.location)


for listing in listings:
    # print(f"{listing[2] = } {listing[1] = } {listing[3] = }")
    score, title = listing[0], listing[2]
    for searchPhrase in searchPhrases.keys():
        if searchPhrase in title:
            dockingValue = 2 * searchPhrases[searchPhrase]
            score -= dockingValue
            print(f"... docking {dockingValue} points for {searchPhrase} being in {title}")

#     # TODO if searchPhrase in jobDescription

    listing = list(listing)
    listing[0] = score

print('\n')
print(listings)

print('\n')
listings.sort(key = lambda listing: listing[0], reverse = True)
print(listings)

print('\n')
for listing in listings:#[:10]:
    score, id, title, company, link, datePosted, location = listing[0], listing[1], listing[2], listing[3], listing[4], listing[5], listing[6]
    print(f"{score} - <a href='{link}'>{title}</a> at {company} in {location}")


#     # location = listing.find("span",  class_="job-result-card__location").contents[0]
#     # print(location)
#     # jobTitleDisqualifications = ['Lead Python Developer', 'Lead Developer', 'Architect']
#     # for jobTitleDisqualification in jobTitleDisqualifications:
#     #     if jobTitleDisqualification in jobTitle:
#     #         print("... -10 points")
#             # break
            
#     # checkSeniorityLevel(jobLink)

#     # print(soup.prettify())
#     # print(listings[0].prettify())

#     print("Finished this round.")

#     webbrowser.open(URL, new = 2)

#     sleep(randint(10, 60))

