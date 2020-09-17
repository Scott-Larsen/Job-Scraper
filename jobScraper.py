import requests
from bs4 import BeautifulSoup
from time import sleep
import pytz
from random import randint
import smtplib
import os.path
import pytz
from datetime import datetime
from dateutil import parser

from linkedInJobBoardScraper import linkedInMetaSearch
from pythonDotOrgJobBoardScraper import pythonDotOrgMetaSearch
from zipRecruiterJobBoardScraper import zipRecruiterMetaSearch
from credentials import USER, PASS, EMAIL

searchPhrases = {
'Entry level': 50, 

'Flask': 25, 'Junior': 25, 'Jr': 25,

'Portland': 10, 'Oregon': 10, ', OR': 10, 'Eugene': 10, 'San Francisco': 10, 'Los Angeles': 10, 'Santa Monica': 10, 'Marina del Rey': 10, 'Venice': 10, 'Long Beach': 10, 'Pasadena': 10, 'Irvine': 10, 'Silicon Valley': 10, 'San Jose': 10, 'California': 10, ', CA': 10, 'Seattle': 10, 'Washington': 10, ', WA': 10, 'New York': 10, 'NYC': 10,

'No longer accepting applications': -1000, 'You applied on': -1000,

'Battery Engineer': -100, 'active TS clearance': -100, 'Staff Backend Engineer': -100,

'Lead Python Developer': -50, 'Lead Developer': -50, 'Lead Software Developer': -50, 'Lead Software Engineer': -50, 'Technology Lead': -50, 'Network Architect': -50, 'Cloud Technical Solutions Engineer': -50,'Ruby on Rails Fullstack Engineer': -50, 'Ruby on Rails Developer': -50, 'Clearance': -50, 'Active SECRET': -50, '7+ years': -50, '6+ years': -50, '5+ years': -50, 'Minimum of 5 years': -50, 'Mid-Level': -50, 'Mid-Senior': -50, 'Senior Python': -50, 'Senior Data': -50, 'Senior Full Stack': -50, 'Senior Backend': -50, 'Microsoft Dynamics': -50, 'Hardware Technician': -50, 'Linux System administrator': -50, 'Embedded Software': -50, 'Engineer III': -50, 'Engineer IV': -50, 'Engineer V': -50, 'Engineer VI': -50, 'Engineer VII': -50, 'Principal Software': -50, 'Security Engineer': -50, 'Senior DevOps': -50,

'Systems Engineering': -25, 'Solutions Engineer': -25, 'Network Developer': -25, 'Network Engineer': -25, 'Data Engineer': -25, 'Data Science': -25, 'Talend': -25, 'ERP': -25, '4+ years': -25, 'Front End Developer': -25, 'Frontend Web': -25, 'Fintech': -25, 'Trading': -25, 'Wall Street': -25, 'DevOps': -25, 'Qlik': -25, 'Engineer Infrastructure': -25, 'Cloud engineer': -25, 'AWS Lead': -25, 'Computer Scientist': -25,

'Application Development': -10, 'Blockchain': -10, 'Crypto': -10, 'Quant': -10, 'ETL Developer': -10, 'React': -10, 'React Native': -10, 'C++': -10, 'PHP': -10, 'Trading': -10, 'Hedge Fund': -10, 'Java': -10, 'Jr.Java': -10, 'Web Developer': -10, 'WordPress': -10, 'Shopify': -10, '3-4 years': -10,'Engineer II': -10, 'Sports Betting': -10, 'Developer Mobile App': -10, 'Container': -10,

'React': -5, 'Vue': -5, 'Angular': -5, 'Cassandra': -5, 'Node': -5, '.NET': -5, 'JavaScript Developer': -5, 'Associate': -5 
}

listings = []

URLs = ["https://www.ziprecruiter.com/candidate/search?radius=5000&days=1&search=Python+-senior+-devops+-etl+-j2ee+-%22data+engineer%22+-%22data+scientist%22+-%22technical+writer%22+-wix+-%22systems+engineer%22+-FPGA+-director+-principal+-%22reliability+engineer%22&location=Omaha%2C+NE",
"https://www.linkedin.com/jobs/search/?f_E=1%2C2%2C3&f_LF=f_AL&f_TPR=r86400&geoId=103644278&keywords=python%20developer%20-senior%20-sr%20-mid-senior&location=United%20States",
"https://www.python.org/jobs/"
]

scrapedJobsFilename = "scrapedJobs.txt"


def main():

    jobs = {}
    scrapedJobs = []
    
    scrapedJobs = readInReturnDelimitedTextFileToDataStructure('', scrapedJobsFilename)

    for URL in URLs:
        if "www.linkedin.com" in URL:
            (jobs, scrapedJobs) = linkedInMetaSearch(URL, jobs, scrapedJobs)
        if "www.python.org" in URL:
            (jobs, scrapedJobs) = pythonDotOrgMetaSearch(URL, jobs, scrapedJobs)
        if "www.ziprecruiter.com" in URL:
            (jobs, scrapedJobs) = zipRecruiterMetaSearch(URL, jobs, scrapedJobs)# -> Tuple[Dict[int, str, str, str, str, str, str, str], List[str]]

    writeOutDataStructureToReturnDelimitedTextFile('', 'scrapedJobs.txt', scrapedJobs)

    for id in jobs.keys():
        score, link, title, company, datePosted, location, fullText = jobs[id][0], jobs[id][1], jobs[id][2], jobs[id][3], jobs[id][4], jobs[id][5], jobs[id][6]

        print("\n" * 2)
        print(id[:35], company, jobs[id][3])
        print(jobs[id])
        print("\n" * 2)
        print(f"\nEvaluating {title} at {company} ({id}).")

        print(f"{datePosted = }")

        try:
            if "yesterday" in datePosted:
                ageInDays = 1
            elif "just now" in datePosted:
                ageInDays = 0
            elif "hours ago" in datePosted or "hour ago" in datePosted:
                ageInDays = float(datePosted.split()[0]) / 24
            else:
                datetimePosted = parser.parse(datePosted)
                
                age = datetime.now().timestamp() - datetimePosted.timestamp()
                ageInDays = int(age / 24 / 60 / 60)
        except parser.ParserError as e:
            print(f"{e}: {datePosted} couldn't be parsed properly from {link}")
            ageInDays = 0

        print(f"{ageInDays = }")

        ageReduction = int(ageInDays ** 2)
        score -= ageReduction
        if ageReduction > 0:
            print(f"... docking {ageReduction} from the score ({score}) because the listing is {ageInDays} days old.")

        for searchPhrase in searchPhrases.keys():
            if searchPhrase.lower() in title.lower():

                scoreAdjustment = 2 * searchPhrases[searchPhrase]
                score += scoreAdjustment
                if scoreAdjustment > 0:
                    scoreAdjustment = '+' + str(scoreAdjustment)
                print(f"... {scoreAdjustment} points ({score}) for {searchPhrase} being in {title}.")
            if searchPhrase.lower() in fullText.lower():
                scoreAdjustment = searchPhrases[searchPhrase]
                score += scoreAdjustment
                if scoreAdjustment > 0:
                    scoreAdjustment = '+' + str(scoreAdjustment)
                print(f"... {scoreAdjustment} points ({score}) for {searchPhrase} being in the text of the listing.")
        jobs[id][0] = score

    print('\n')

    sendEMail(jobs)


def readInReturnDelimitedTextFileToDataStructure(directory: str, filename: str):
    listFromFile = []
    dictionaryFromFile = {}
        
    if os.path.exists(directory + filename):
        print(f"Opening {filename} and writing it into a data structure....\n")

        with open(directory + filename, 'r') as filehandle:
            for line in filehandle:
                currentLine = line[:-1]
                if " " in currentLine:
                    currentLine = currentLine.split()
                    dictionaryFromFile[currentLine[0]] = int(currentLine[1])
                else:
                    listFromFile.append(currentLine)
    else:
        print(f"{directory + filename} doesn't exist")
    if len(listFromFile) >= len(dictionaryFromFile):
        dataStructureToReturn = listFromFile
    else:
        dataStructureToReturn = dictionaryFromFile
    print(f"Loaded in {filename}.\n")
    return dataStructureToReturn

def writeOutDataStructureToReturnDelimitedTextFile(directory, filename, dataStructureToBeWrittenOut):
    if os.path.exists(directory + filename):
        print(f"Writing out list to {filename}....\n")
        with open(directory + filename, 'w') as filehandle:
            if isinstance(dataStructureToBeWrittenOut, list):
                filehandle.writelines(f"{item}\n" for item in dataStructureToBeWrittenOut)
            elif isinstance(dataStructureToBeWrittenOut, dict):
                filehandle.writelines(f"{key} {dataStructureToBeWrittenOut[key]}\n" for key in dataStructureToBeWrittenOut.keys())


def sendEMail(jobs):
    jobs = jobs
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(USER, PASS)

    subject = f"Job Scraper Results"

    body = ""
    jobIDs = [jobs[x] for x in sorted(jobs.keys(), key = lambda x: jobs[x][0], reverse = True)][:25]
    for jobID in jobIDs:
        body += f"({jobID[0]}) {jobID[2]} at {jobID[3]} in {jobID[5]} posted {jobID[4][5:11]}\n{jobID[1]}\n... {jobID[6][100:500]} ...\n\n\n"
    if len(body) == 0:
        body += "\nNo results."
    body = body.encode('ascii', 'ignore').decode('ascii') # last working
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(EMAIL, EMAIL, msg)

    timeZone_NY = pytz.timezone('America/NEW_York')
    datetime_NY = datetime.now(timeZone_NY)
    print(f"E-mail was sent at {datetime_NY.strftime('%H:%M')}.\n\n")

    server.quit()

if __name__ == "__main__":
    main()