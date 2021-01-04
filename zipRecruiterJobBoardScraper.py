from time import sleep
from random import randint
from zipRecruiterIndividualJobScraper import zipRecruiterIndividualJobScraper
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException


def zipRecruiterMetaSearch(URL, jobs, scrapedJobs):

    driver = webdriver.Chrome(
        "/Users/Scott/Desktop/DATA/SORT/CodingProgrammingPython/jobScraper/chromedriver"
    )

    driver.get(URL)
    sleep(randint(3, 10))
    print("\nDoing a metascrape of jobs on ZipRecruiter:")
    jobListings = driver.find_elements_by_xpath(".//div[@ class='job_content']")

    for jobListing in jobListings:

        id = link = jobListing.find_element_by_css_selector("a.job_link").get_attribute(
            "href"
        )

        if id not in scrapedJobs:
            scrapedJobs.insert(0, id)

            score = 1000

            title = jobListing.find_element_by_css_selector(
                "span.just_job_title"
            ).get_attribute("innerHTML")

            company = jobListing.find_element_by_xpath(
                ".//a[@class='t_org_link name']"
            ).get_attribute("innerHTML")

            try:
                location = jobListing.find_element_by_xpath(
                    ".//a[@class='t_location_link location']"
                ).get_attribute("innerHTML")
            except NoSuchElementException as e:
                print(f"No location found for {id}")
                location = ""

            abridgedText = (
                jobListing.find_element_by_xpath(".//p[@class='job_snippet']/a")
                .get_attribute("innerHTML")
                .strip()
            )

            print(f"Scraping {title} at {company}")

            fullText, datePosted = zipRecruiterIndividualJobScraper(link)

            if fullText == False:
                fullText = abridgedText

            jobs[id] = [score, link, title, company, datePosted, location, fullText]

    return jobs, scrapedJobs

