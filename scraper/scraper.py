from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


websites = ["https://ca.indeed.com/jobs?q={jobTitle}&l={location}"]

webHome = ["https://ca.indeed.com"]

jobInfoTags = ["job_seen_beacon"]


def getJobInfo(jobTitle:str, location:str):
    
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-blink-features=AutomationControlled")


    #https://www.whatismybrowser.com/guides/the-latest-user-agent/chrome seem to be working
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")


    service = Service(ChromeDriverManager().install())
    

    driver = webdriver.Chrome(service=service, options=options)

    driver.implicitly_wait(10)

    url = websites[0].format(jobTitle=jobTitle, location=location)
    

    driver.get(url=url)

    soup = BeautifulSoup(driver.page_source, "html.parser")


    jobUrl = webHome[0]+soup.find_all("div", class_=jobInfoTags[0] )[0].find('a', href=True)['href']
    driver.get(url=jobUrl)
    
    jobSoup = BeautifulSoup(driver.page_source, "html.parser")

    title = jobSoup.find("h1", {"class": "jobsearch-JobInfoHeader-title"} ).text
    print("title:", title)

    company = jobSoup.find("div", {"data-company-name": "true"}).text
    print(company)

    location = jobSoup.find("div", {"data-testid": "inlineHeader-companyLocation"}).text
    print(location)


    print(jobUrl)


    return 0

getJobInfo("Software","Toronto")
