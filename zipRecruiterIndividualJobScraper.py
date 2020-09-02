import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
from urllib.request import Request, urlopen


def zipRecruiterIndividualJobScraper(link):

    headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:73.0) Gecko/20100101 Firefox/73.0'}

    # forwardedLink = urllib.request(link)
    # fL = forwardedLink.geturl()

    # fl = urllib.urlretrieve(link)
    # forwardedLink = requests.get(link)
    # print(f"{forwardedLink.url}")
    # print(f"{forwardedLink.history}")
    # print(f"{forwardedLink.status_code}")

    # res = urllib.request.urlopen(link, headers = headers)
    # finalurl = res.geturl()
    # print(finalurl)

    # from urllib.request import Request, urlopen

    # This checks if the ZipRecruiter Link is actually redirecting to a job on LinkedIn, etc.

    # try:
    forwardedLink = Request(link, headers = headers)
    print(f"{forwardedLink = }")
    # forwardedLinkText = urlopen(forwardedLink).read()
    forwardedLinkText = requests.get(link, verify = False, timeout = 10)
    # r = requests.get(w, verify=False, timeout=10)
    print(f"{forwardedLinkText = }")
    
    if b"linkedin.com/jobs/view/" in forwardedLinkText or b"dice.com/jobs/detail/" in forwardedLinkText or b"jobs.rtx.com" in forwardedLinkText:
        print(f"This job is pulled from another site:\n{urlopen(forwardedLink).read()}\n")
        return "", "99999 hours ago"
    
    # except ConnectionResetError as e:
    #     print(f"{e}: server reset trying to reach {link}\n")
    #     pass

    # print(f"{webpage = }")
    # print(f"{redirectLink = }")

    else:
        # print(f"{fL = }")

        # print open(result[0]).read()

        page = requests.get(link, headers = headers)
        
        # print(page.url)
        # newURL = page.url
        # print(page.history)

        soup = BeautifulSoup(page.content, 'html.parser')

        try:
            fullText = soup.find("div", class_="jobDescriptionSection").get_text(separator=' ').strip()
        except AttributeError as e:
            print(f'{e}: no detailed job description for {link}')
            fullText = False

        try:
            classData = soup.find_all('span', class_='data')
            datePosted = classData[-1].get_text().strip()
            if datePosted == 0:
                print(f"Found datePosted as {datePosted}\n")
                print(soup.get_text())
        except AttributeError as e:
            print(f'{e}: no datePosted for {link}')
            datePosted = "99999 hours ago"

        print(f"{datePosted = }")
        
        # print(fullText)
        # print(datePosted)

        sleep(randint(10, 60))

        return fullText, datePosted



# link = "https://www.ziprecruiter.com/jobs/technology-navigators-af7d8881/remote-python-software-engineer-django-aws-docker-vue-js-620c7835?lvk=eEd2aAvQTRi7iC7pDydJ2Q.--LhzbSQDgs"
# # link = "https://www.ziprecruiter.com/ek/l/AAJYbkjuVDTdrn63Ugwb5P6Nx_JrNQha713O8qAf3xqZhkYESqzPhJ03z45-hSYJ0Hon44jZCFioo4HleQpVCrh-6c_Mlr8AMncuWtVGlLGQtpnfm1dMTiNIijy1qYyj7ocejCbML7tVrp_w3Hx1utUkqnEH7XisdZxP7rIlMPfhbG4f5faB39A9SCpnERc?refu=%2Fcandidate%2Fsearch%3Fradius%3D5000%26days%3D1%26search%3DPython%2B-senior%2B-devops%2B-etl%2B-j2ee%2B-%2522data%2Bengineer%2522%2B-%2522data%2Bscientist%2522%2B-%2522technical%2Bwriter%2522%2B-wix%2B-%2522systems%2Bengineer%2522%2B-FPGA%2B-director%2B-principal%2B-%2522reliability%2Bengineer%2522%26location%3DOmaha%252C%2BNE"
# link = "https://www.ziprecruiter.com/ojob/f26468bfb4d68c49167faf6d003f7cbf?lvk=0l1IFuWgXa0K6xDlooexDQ.--Li3-lsSzg"
# link = 'https://www.ziprecruiter.com/ek/l/AAJo9kfH4c0d9d9Ecb-iMsDV-Pl1pOYjq15A51cAU51QygVkKd0GEcFzMQQSxNvr-lSqLGW7r--IatkswwG6ciG9Fp-gjYtYUPuymHPp7NvHALbDau6-b4wUVQni2d35GrGi4BBLP4uMvxpUfd7frlr1aFq1nIvuC8uibChC4ILovJ4So0DiRZ_QDR_DfeA'
# link = "https://www.ziprecruiter.com/jobs/uniquify-inc-4e4696c1/artificial-intelligence-intern-1a844898?lvk=bWxFa68-57Bxg4zLiSSlZg.--LiBH7qabk"
link = "https://www.ziprecruiter.com/ek/l/AALT21NCHOs3JVdIO1GNFXZ2dAp6P89M8v0UahfYMqaQflHMDUVOCCfvmdzdesWpig8c3rHgnXZnYGq48ZyFxW5TOKSETqyulmOXP3nGWYmwIRHCDS9aiQ3VIbQsXjxmTOPbAXnfAzqw4A9r_pzf7KZm30MpJRoNaCUKPDz5Gu0fmpZg8WPVQOHbmiUwBNk"
zipRecruiterIndividualJobScraper(link)