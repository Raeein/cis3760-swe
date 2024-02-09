import time
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


# websites = ["https://ca.indeed.com/jobs?q={jobTitle}&l={location}"]

# webHome = ["https://ca.indeed.com"]

# jobInfoTags = ["job_seen_beacon"]


jobBoardList = [
                    {
                        "jobBoardName": "Indeed",
                        "jobBoardBaseUrl": "https://ca.indeed.com", 
                        "jobBoardSearchUrl": "https://ca.indeed.com/jobs?q={jobTitle}&l={location}",
                        "jobCardClass": "job_seen_beacon",
                        "jobCardElement": "div"
                    }
                ]


def getJobInfo(jobTitle:str, location:str, specifiedJobBoards:list[str] = [] ):
    
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-blink-features=AutomationControlled")

    #https://www.whatismybrowser.com/guides/the-latest-user-agent/chrome seem to be working
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")


    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=options)

    driver.implicitly_wait(10)


    jobBoardSearchList = []
    if(specifiedJobBoards == []):
        jobBoardSearchList = jobBoardList
    else:
        for jobBoard in specifiedJobBoards:
            for jobBoardObject in jobBoardList:
                if(jobBoard["jobBoardName"] == jobBoard):
                    jobBoardSearchList.append(jobBoardObject)
                    break


        
    for jobBoardObject in jobBoardSearchList:
    
    # url = websites[0].format(jobTitle=jobTitle, location=location)
        url = jobBoardObject["jobBoardSearchUrl"].format(jobTitle=jobTitle, location=location)
        

        driver.get(url=url)
        time.sleep(5)

        soup = BeautifulSoup(driver.page_source, "html.parser")


        # jobUrl = webHome[0]+soup.find_all("div", class_=jobInfoTags[0] )[0].find('a', href=True)['href']
        jobCards = soup.find_all(jobBoardObject["jobCardElement"], class_=jobBoardObject["jobCardClass"] )

        for jobCard in jobCards:

            jobUrl = jobBoardObject["jobBoardBaseUrl"]+jobCard.find('a', href=True)['href']

            driver.get(url=jobUrl)
            time.sleep(5)
            
            jobSoup = BeautifulSoup(driver.page_source, "html.parser")

            print("-"*20)
            title = jobSoup.find("h1", {"class": "jobsearch-JobInfoHeader-title"} ).text
            print("title:", title)

            company = jobSoup.find("div", {"data-company-name": "true"}).text
            print(company)

            location = jobSoup.find("div", {"data-testid": "inlineHeader-companyLocation"}).text
            print(location)

            print(jobUrl)
            print("-"*20)


    return 0

getJobInfo("Software","Toronto")
