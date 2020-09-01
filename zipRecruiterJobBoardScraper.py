from time import sleep
from random import randint
from zipRecruiterIndividualJobScraper import zipRecruiterIndividualJobScraper
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# baseURL = "https://www.ziprecruiter.com/candidate/search?radius=5000&days=1&search=Python+-senior+-devops+-etl+-j2ee+-%22data+engineer%22+-%22data+scientist%22+-%22technical+writer%22+-wix+-%22systems+engineer%22+-FPGA+-director+-principal+-%22reliability+engineer%22&location=Omaha%2C+NE"

def zipRecruiterMetaSearch(URL, jobs, scrapedJobs):
    # options = webdriver.ChromeOptions()
    #         options.add_argument('headless')
    #         try:
    #             cls.client = webdriver.Chrome(options=options)

    # options = Options()  
    # options.add_argument("--headless")  
    # try:
    driver = webdriver.Chrome()#options = options)

    # URLs = []

    driver.get(URL)
    sleep(40)
    print("Doing a metascrape of jobs on ZipRecruiter:")
    jobListings = driver.find_elements_by_xpath("//div[@ class='job_content']")
        
    # print(webAttributeLinks[0])
    for jobListing in jobListings:
        # html = (jobListing.get_attribute('innerHTML'))

        # print(jobListing.get_attribute('innerHTML'))
        # print("\n" * 10)
        
        # print("\n" * 10)
        id = link = jobListing.find_element_by_css_selector('a.job_link').get_attribute('href')

        if id in scrapedJobs:
            break
        else:
            scrapedJobs.insert(0, id)

        score = 1000

        title = jobListing.find_element_by_css_selector('span.just_job_title').get_attribute('innerHTML')

        company = jobListing.find_element_by_xpath("//a[@class='t_org_link name']").get_attribute('innerHTML')

        # datePosted = jobListing.find

        location = jobListing.find_element_by_xpath("//a[@class='t_location_link location']").get_attribute('innerHTML')

        abridgedText = jobListing.find_element_by_xpath("//p[@class='job_snippet']/a").get_attribute('innerHTML').strip()

        # linkedText = jobListing.find_element_by_xpath("//p[@class='job_snippet']/a").get_attribute('href')

        fullText, datePosted = zipRecruiterIndividualJobScraper(link)

        if fullText == False:
            fullText = abridgedText

        print(f"{link = }")
        # print(f"{linkedText = }")
        print(f"{fullText = }\n\n")
        print(f"{datePosted = }\n\n\n\n")

        jobs[id] = [score, link, title, company, datePosted, location, fullText]

    return jobs, scrapedJobs

        # print(f"{link = }")

        # print("\n" * 10)

    # soup = (webAttributeLinks[0].get_attribute('innerHTML'))

    # sleep(randint(1, 20))


    # finally:
    #     driver.quit()