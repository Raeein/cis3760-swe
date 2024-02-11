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

                        "jobCardElement": "div",
                        "jobCardClass": "job_seen_beacon",

                        "jobTitleElement": "h1",
                        "jobTitleSearchObject": {"class": "jobsearch-JobInfoHeader-title"},

                        "jobCompanyElement": "div",
                        "jobCompanySearchObject": {"data-company-name": "true"},

                        "jobLocationElement": "div",
                        "jobLocationSearchObject": {"data-testid": "inlineHeader-companyLocation"},

                        "jobEmploymentElement": "div",
                        "jobEmploymentSearchObject": {"aria-label":"Job type"},

                        "jobPayElement": "div",
                        "jobPaySearchObject": {"aria-label":"Pay"},

                        "jobDescriptionElement": "div",
                        "jobDescriptionSearchObject": {"id":"jobDescriptionText"}
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


    jobJsonObjectList = []

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
        
        time.sleep(2)
        driver.implicitly_wait(10)
        driver.get(url=url)
        

        soup = BeautifulSoup(driver.page_source, "html.parser")


        # jobUrl = webHome[0]+soup.find_all("div", class_=jobInfoTags[0] )[0].find('a', href=True)['href']
        jobCards = soup.find_all(jobBoardObject["jobCardElement"], class_=jobBoardObject["jobCardClass"] )

        for jobCard in jobCards:

            jobUrl = jobBoardObject["jobBoardBaseUrl"]+jobCard.find('a', href=True)['href']
            jobJsonObject = {}

            time.sleep(2)
            driver.implicitly_wait(10)
            driver.get(url=jobUrl)
            
            
            jobSoup = BeautifulSoup(driver.page_source, "html.parser")

            print("-"*20)
            title = jobSoup.find(jobBoardObject["jobTitleElement"], jobBoardObject["jobTitleSearchObject"]).text
            jobJsonObject["title"] = title
            print("title: ", title)
            

            company = jobSoup.find(jobBoardObject["jobCompanyElement"], jobBoardObject["jobCompanySearchObject"]).text
            jobJsonObject["company"] = company
            print("company: ", company)

            location = jobSoup.find(jobBoardObject["jobLocationElement"], jobBoardObject["jobLocationSearchObject"]).text
            jobJsonObject["location"] = location
            print("location:", location)

            try:
                employmentType = jobSoup.find(jobBoardObject["jobEmploymentElement"], jobBoardObject["jobEmploymentSearchObject"]).text[8:]
            except:
                employmentType = "Unknown"
            finally:
                jobJsonObject["employment_type"] = employmentType
                print("employment type: ", employmentType)

            try:
                salary = jobSoup.find(jobBoardObject["jobPayElement"], jobBoardObject["jobPaySearchObject"]).text[3:]
            except:
                salary = "Unknown"
            finally:
                jobJsonObject["salary"] = salary
                print("salary: ",salary)

            description = jobSoup.find(jobBoardObject["jobDescriptionElement"], jobBoardObject["jobDescriptionSearchObject"]).text
            jobJsonObject["description"] = description
            print("description: ", description)

            print(jobUrl)
            print("-"*20)
            jobJsonObjectList.append(jobJsonObject)


    return jobJsonObjectList

print(getJobInfo("Software","Toronto"))
