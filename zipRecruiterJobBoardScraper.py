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
    driver = webdriver.Chrome('/Users/Scott/Desktop/DATA/SORT/CodingProgrammingPython/jobScraper/chromedriver')#options = options)
    # URLs = []

    driver.get(URL)
    sleep(randint(3, 10))
    print("\nDoing a metascrape of jobs on ZipRecruiter:")
    jobListings = driver.find_elements_by_xpath("//div[@ class='job_content']")
        
    # print(webAttributeLinks[0])
    # for i, jobListing in enumerate(jobListings[:3]):
    for jobListing in jobListings[:2]:
        # html = (jobListing.get_attribute('innerHTML'))

        print("\n", jobListing.get_attribute('innerHTML'), "\n")

        # print("\n" * 10)
        # print(jobListing.get_attribute('innerHTML'))
        # print("\n" * 4)
        # titles = (jobListing.find_elements_by_xpath("//a[@class='t_org_link name']"))
        # for title in titles:
        #     print("")
        #     print(title.get_attribute('innerHTML'))

        id = link = jobListing.find_element_by_css_selector('a.job_link').get_attribute('href')

        if id not in scrapedJobs:
            scrapedJobs.insert(0, id)

            # print(f"About to scrape {link}")

            score = 1000

            title = jobListing.find_element_by_css_selector('span.just_job_title').get_attribute('innerHTML')

            # company = None
            # print(f"\n{company = }\n")

            company = jobListing.find_element_by_xpath("//a[@class='t_org_link name']").get_attribute('innerHTML')
            print(f"\n{title = }")
            print(f"{company = }\n")
            # print(f"\n{company = }\n")
            
            # if company == None:
            #     print(f"\n\n{jobListing}\n")

            # datePosted = jobListing.find
            # locations = jobListing.find_elements_by_xpath("//a[@class='t_location_link location']")#.get_attribute('innerHTML')
            # print(f"{len(locations) = }")
            # for l in locations:
            #     print(l.get_attribute('innerHTML'))

            location = jobListing.find_element_by_xpath("//a[@class='t_location_link location']").get_attribute('innerHTML')

            abridgedText = jobListing.find_element_by_xpath("//p[@class='job_snippet']/a").get_attribute('innerHTML').strip()

            # linkedText = jobListing.find_element_by_xpath("//p[@class='job_snippet']/a").get_attribute('href')

            print(f"Scraping {title} at {company}")
            
            fullText, datePosted = zipRecruiterIndividualJobScraper(link)

            if fullText == False:
                fullText = abridgedText

            # print(f"{link = }")
            # print(f"{linkedText = }")
            # print(f"{fullText = }")
            # print(f"{datePosted = }")
            # print(f"\n\n{score = }{link = }{title = }{company = }{datePosted = }{location = }")

            jobs[id] = [score, link, title, company, datePosted, location, fullText]

    return jobs, scrapedJobs

        # print(f"{link = }")

        # print("\n" * 10)

    # soup = (webAttributeLinks[0].get_attribute('innerHTML'))

    # sleep(randint(1, 20))


    # finally:
    #     driver.quit()
# listing = "https://wwww.ziprecruiter.com/ojob/5cf2c67c609f42e5592a229742a76a0b?lvk=JGihlMSN-VwH1Fxhb8qRlQ.--LibjKiDJZ"