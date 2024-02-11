import time
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



job_board_list = [
                    {
                        "job_board_name": "Indeed",
                        "job_board_base_url": "https://ca.indeed.com", 
                        "job_board_search_url": "https://ca.indeed.com/jobs?q={job_title}&l={location}",

                        "job_card_element": "div",
                        "job_card_class": "job_seen_beacon",

                        "job_title_element": "h1",
                        "job_title_search_object": {"class": "jobsearch-JobInfoHeader-title"},

                        "job_company_element": "div",
                        "job_company_search_object": {"data-company-name": "true"},

                        "job_location_element": "div",
                        "job_location_search_object": {"data-testid": "inlineHeader-companyLocation"},

                        "job_employment_element": "div",
                        "job_employment_search_object": {"aria-label":"Job type"},

                        "job_pay_element": "div",
                        "job_pay_search_object": {"aria-label":"Pay"},

                        "job_description_element": "div",
                        "job_description_search_object": {"id":"jobDescriptionText"}
                    }
                ]


def getJobInfo(job_title:str, location:str, specified_job_boards:list[str] = [] ):
    #return variable
    job_json_object_list = []

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    #https://www.whatismybrowser.com/guides/the-latest-user-agent/chrome seem to be working
    options.add_argument("""user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36""")
    #service = Service(ChromeDriverManager().install())

    #driver = webdriver.Chrome(service=service, options=options)
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)


    job_board_search_list = []
    if(specified_job_boards == []):
        job_board_search_list = job_board_list
    else:
        for job_board in specified_job_boards:
            for job_board_object in job_board_list:
                if(job_board["job_board_name"] == job_board):
                    job_board_search_list.append(job_board_object)
                    break
        
    for job_board_object in job_board_search_list:
        url = job_board_object["job_board_search_url"].format(job_title=job_title, location=location)
        
        time.sleep(2)
        driver.implicitly_wait(10)
        driver.get(url=url)
        

        soup = BeautifulSoup(driver.page_source, "html.parser")

        job_cards = soup.find_all(job_board_object["job_card_element"], class_=job_board_object["job_card_class"] )

        for job_card in job_cards:

            jobUrl = job_board_object["job_board_base_url"]+job_card.find('a', href=True)['href']
            job_json_object = {}

            time.sleep(2)
            driver.implicitly_wait(10)
            driver.get(url=jobUrl)
            
            
            job_soup = BeautifulSoup(driver.page_source, "html.parser")

            print("-"*20)
            title = job_soup.find(job_board_object["job_title_element"], 
                                 job_board_object["job_title_search_object"]).text
            job_json_object["title"] = title
            print("title: ", title)

            company = job_soup.find(job_board_object["job_company_element"], 
                                   job_board_object["job_company_search_object"]).text
            job_json_object["company"] = company
            print("company: ", company)

            location = job_soup.find(job_board_object["job_location_element"], 
                                    job_board_object["job_location_search_object"]).text
            job_json_object["location"] = location
            print("location:", location)

            try:
                employment_type = job_soup.find(job_board_object["job_employment_element"], 
                                              job_board_object["job_employment_search_object"]).text[8:]
            except:
                employment_type = "Unknown"
            finally:
                job_json_object["employment_type"] = employment_type
                print("employment type: ", employment_type)

            try:
                salary = job_soup.find(job_board_object["job_pay_element"], 
                                      job_board_object["job_pay_search_object"]).text[3:]
            except:
                salary = "Unknown"
            finally:
                job_json_object["salary"] = salary
                print("salary: ",salary)

            description = job_soup.find(job_board_object["job_description_element"], 
                                       job_board_object["job_description_search_object"]).text
            job_json_object["description"] = description
            print("description: ", description)

            print(jobUrl)
            print("-"*20)
            job_json_object_list.append(job_json_object)


    return job_json_object_list


if __name__ == "__main__":
    getJobInfo("Software Developer", "Toronto, On")