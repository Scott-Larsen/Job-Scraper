import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
from linkedInJobBoardScraper import linkedInMetaSearch
import smtplib
from datetime import datetime
from credentials import USER, PASS, EMAIL

# 'Python': 50, 'Python Developer': 50,
searchPhrases = {

'Flask': 25,

'Portland': 10, 'Junior': 10, 'Jr': 10,

'Lead Python Developer': -50, 'Lead Developer': -50, 'Lead Software Developer': -50, 'Architect': -50, 'Cloud Technical Solutions Engineer': -50,'Ruby on Rails Fullstack Engineer': -50, 'Ruby on Rails Developer': -50, 'Clearance': -50, 'Active SECRET': -50, '7+ years': -50, '5+ years': -50, 'Mid-Level': -50,

'Mid-Senior level': -25, 'Solutions Engineer': -25, 'Data Engineer': -25, 'Data Science': -25, 'Talend': -25, 'ERP': -25, '4+ years': -25, 'Front End Developer': -25, 'Fintech': -25,

'Application Development': -10, 'Blockchain': -10, 'Crypto': -10, 'Quant': -10, 'ETL Developer': -10, 'React': -10, 'React Native': -10, 'C++': -10, 'PHP': -10, 'Trading': -10, 'Hedge Fund': -10, 'Java': -10, 'Jr.Java': -10
}

listings = []

linkedInURL = "https://www.linkedin.com/jobs/search/?f_E=1%2C2%2C3&f_LF=f_AL&f_TPR=r86400&geoId=103644278&keywords=python%20developer%20-senior%20-sr%20-mid-senior&location=United%20States"
# "https://www.linkedin.com/jobs/search/?f_TPR=r86400&geoId=103644278&keywords=python%20developer%20-senior%20-sr%20-mid-senior&location=United%20States%22"
# https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=103644278&keywords=python%20developer%20-senior%20-sr%20-mid-senior&location=United%20States"

# listings.append(linkedInMetaSearch(linkedInURL, jobs))

class Job:
    def __init__(self, score, title, company, link, datePosted, location, listingSite):
        self.score = score
        self.title = title
        self.company = company
        self.link = link
        self.datePosted = datePosted
        self.location = location
        self.listingSite = listingSite

jobs = {}
linkedInMetaSearch(linkedInURL, jobs)

def sendEMail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(USER, PASS)

    subject = f"Job Scraper Results"
    # body = "Check B&HPhoto"

    body = ""
    jobIDs = [jobs[x] for x in sorted(jobs.keys(), key = lambda x: jobs[x][0], reverse = True)][:10]
    for jobID in jobIDs:

        # body += f"({jobID[0]}) <a href='{jobID[4]}'>{jobID[2]}</a> at {jobID[3]} in {jobID[6]} posted {jobID[5]} ({jobID[1]})\n"
        body += f"({jobID[0]}) {jobID[2]} at {jobID[3]} in {jobID[6]} posted {jobID[5]} ({jobID[1]})\n{jobID[4]}\n\n"
        # [score, id, title, company, link, datePosted, location]
    print(body)
    # body = body.encode('utf-8').strip()
    body = body.encode('ascii', 'ignore').decode('ascii')
    msg = f"Subject: {subject}\n\n{body}"
    

    server.sendmail(EMAIL, EMAIL, msg)
    print("E-mail has been sent.")

    server.quit()

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


for job in jobs.keys():
    # print(f"{listing[2] = } {listing[1] = } {listing[3] = }")
    score, id, title, company, link, datePosted, location = jobs[job][0], jobs[job][1], jobs[job][2], jobs[job][3], jobs[job][4], jobs[job][5], jobs[job][6], 
    # score, title = jobs[job][0], jobs[job][2]

    print(f"\nEvaluating {title} at {company} ({id}).")
    # print(link)

    datetimePosted = datetime.strptime(datePosted, '%Y-%m-%d')
    # print(f"{datetimePosted = }")
    age = datetime.now().timestamp() - datetimePosted.timestamp()
    # print(f"{age = }")
    ageInDays = int(age / 24 / 60 / 60)
    # print(f"{ageInDays = }")
    ageReduction = ageInDays ** 2
    score -= ageReduction
    if ageReduction > 0:
        print(f"... docking {ageReduction} from the score ({score}) because the listing is {ageInDays} days old.")

    for searchPhrase in searchPhrases.keys():
        if searchPhrase in title:
            # positiveNegative = -1 if searchPhrases[searchPhrase] < 0 else 1
            scoreAdjustment = 2 * searchPhrases[searchPhrase]
            score += scoreAdjustment
            if scoreAdjustment > 0:
                scoreAdjustment = '+' + str(scoreAdjustment)
            print(f"... {scoreAdjustment} points for {searchPhrase} being in {title}")

#     # TODO if searchPhrase in jobDescription

    # listing = list(listing)
    jobs[job][0] = score

print('\n')

# for job in sorted(jobs.items(), key=lambda x: x[1][0], reverse = True):
#     print(job)

# print(jobs)
# print("\n" * 5)

# jobIDs = [jobs[x] for x in sorted(jobs.keys(), key = lambda x: jobs[x][0], reverse = True)][:10]
# print(jobIDs)

sendEMail()

# print(key, value) for (key, value) in sorted(orders.items(), key=lambda x: x[1]

# for jobID in jobIDs:
#     print(f"({jobs[jobID][0]}) <a href='{jobs[jobID][4]}'>{jobs[jobID][2]}</a> at {jobs[jobID][3]} in {jobs[jobID][6]} posted {jobs[jobID][5]} ({jobs[jobID][1]}")

# print(listings)

# print('\n')
# jobs.sort(key = lambda listing: listing[0], reverse = True)
# print(listings)

# print('\n')
# for listing in listings:#[:10]:
#     score, id, title, company, link, datePosted, location = listing[0], listing[1], listing[2], listing[3], listing[4], listing[5], listing[6]
#     print(f"{score} - <a href='{link}'>{title}</a> at {company} in {location}")


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