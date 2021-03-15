from time import sleep
from random import randint
from pathlib import Path
from ziprecruiter_individual_job_scraper import ziprecruiter_individual_job_scraper
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException


def ziprecruiter_meta_search(URL, jobs, scraped_jobs):
    """Does a meta search of the job board, reaches out to individual job scraper and returns job details"""

    driver = webdriver.Chrome(
        Path.cwd()
        / "chromedriver"  # "/Users/Scott/Desktop/DATA/SORT/CodingProgrammingPython/job_scraper/chromedriver"
    )

    driver.get(URL)
    sleep(randint(3, 10))
    print("\nDoing a metascrape of jobs on ZipRecruiter:")
    jobListings = driver.find_elements_by_xpath(".//div[@ class='job_content']")

    for jobListing in jobListings:

        id = link = jobListing.find_element_by_css_selector("a.job_link").get_attribute(
            "href"
        )

        if id not in scraped_jobs:
            scraped_jobs.insert(0, id)

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

            full_text, date_posted = ziprecruiter_individual_job_scraper(link)

            if full_text == False:
                full_text = abridgedText

            jobs[id] = [score, link, title, company, date_posted, location, full_text]

    return jobs, scraped_jobs
