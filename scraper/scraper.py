import time
import random
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium import webdriver

job_board_list_object = {
    "Indeed": {
        "job_board_base_url": "https://ca.indeed.com",
        "job_board_search_url": "https://ca.indeed.com/jobs?q={job_title}&l={location}",

        "job_card_element": "div",
        "job_card_class": "job_seen_beacon",

        # job page attribute start
        # string parse will be parsing beginning and end of string. Positive will remove character from beginning, negative remove character from end
        "job_title_element": "h1",
        "job_title_search_object": {"class": "jobsearch-JobInfoHeader-title"},

        "job_company_element": "div",
        "job_company_search_object": {"data-company-name": "true"},

        "job_location_element": "div",
        "job_location_search_object": {"data-testid": "inlineHeader-companyLocation"},

        "employment_type_element": "div",
        "employment_type_search_object": {"aria-label": "Job type"},
        "employment_type_string_parse": 8,

        "job_salary_element": "div",
        "job_salary_search_object": {"aria-label": "Pay"},
        "job_salary_string_parse": 3,

        "job_description_element": "div",
        "job_description_search_object": {"id": "jobDescriptionText"},
        # job page attribute ends
    },
    "Canadian Job Bank": {
        "job_board_base_url": "https://www.jobbank.gc.ca",
        "job_board_search_url": "https://www.jobbank.gc.ca/jobsearch/jobsearch?searchstring={job_title}&locationstring={location}",

        "job_card_element": "a",
        "job_card_class": "resultJobItem",

        "job_title_element": "span",
        "job_title_search_object": {"property": "title"},

        "job_company_element": "span",
        "job_company_search_object": {"property": "hiringOrganization"},

        "job_location_element": "span",
        "job_location_search_object": {"property": "address"},

        "employment_type_element": "span",
        "employment_type_search_object": {"property": "employmentType"},

        "job_salary_element": "span",
        "job_salary_search_object": {"property": "baseSalary"},

        "job_description_element": "div",
        "job_description_search_object": {"id": "comparisonchart"},
    }
}


def get_firefox_driver():
    #set web driver options
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("""user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36""")

    # check if geckodriver is installed, if not print an error message and exit
    try:
        service = Service('/usr/bin/geckodriver')
    except Exception as e:
        print("Error: ", e)
        exit()
    driver = webdriver.Firefox( options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => null})")
    driver.implicitly_wait(100)

    return driver



def get_job_cards_from_html(html_string: str, job_board_name: str):
    job_cards = []

    soup = BeautifulSoup(html_string, "html.parser")

    job_board_object = job_board_list_object[job_board_name]
    job_cards = soup.find_all(job_board_object["job_card_element"], class_=job_board_object["job_card_class"])

    for i in range(len(job_cards)):
        job_cards[i] = "<div>" + str(job_cards[i]) + "</div>"
        job_cards[i] = BeautifulSoup(job_cards[i], "html.parser")

    return job_cards


# attribute will be the string defined in the attribute section of the job list object subtracting the suffix
def get_job_attribute(html_string: str, attribute: str, job_board_name: str) -> str:
    job_soup = BeautifulSoup(html_string, "html.parser")

    try:
        data = job_soup.find(
            job_board_list_object[job_board_name][attribute + "_element"],
            job_board_list_object[job_board_name][attribute + "_search_object"]
        ).text
        if (attribute + "_string_parse" in job_board_list_object[job_board_name]):
            data = data[job_board_list_object[job_board_name][attribute + "_string_parse"]:]

    except:
        data = "Unknown"

    return data.strip()


def get_job_json(page_source: str, job_board_name:str, job_url:str) -> dict:
    job_json_object = {}
    job_json_object["title"] = get_job_attribute(page_source, "job_title", job_board_name)
    job_json_object["company"] = get_job_attribute(page_source, "job_company", job_board_name)
    job_json_object["location"] = get_job_attribute(page_source, "job_location", job_board_name)
    job_json_object["employment_type"] = parse_employment_type( get_job_attribute(page_source, "employment_type", job_board_name) )
    job_json_object["salary"] = get_job_attribute(page_source, "job_salary", job_board_name)
    job_json_object["description"] = get_job_attribute(page_source, "job_description", job_board_name)
    job_json_object["url"] = job_url

    return job_json_object


def load_targeted_job_board(specified_job_boards: list[str] = []):
    job_board_search_list = []
    if (specified_job_boards == []):
        job_board_search_list = list(job_board_list_object.keys())
    else:
        for i in specified_job_boards:
            if i in list(job_board_list_object.keys()):
                job_board_search_list.append(i)
    return job_board_search_list

def get_job_board_search_url(job_title:str , location:str, job_board_name:str) -> str: 
    url = job_board_list_object[job_board_name]["job_board_search_url"].format(job_title=job_title,location=location)
    return url

def get_job_url(job_board_name:str, job_card:str) -> str:
    url = job_board_list_object[job_board_name]["job_board_base_url"] + job_card.find('a')['href']
    return url

def stall_driver(driver: webdriver.Firefox):
    driver.implicitly_wait(random.randint(10, 20))
    time.sleep(random.randint(2, 5))

def parse_employment_type(employment_type:str )-> str:
    employment_types = ["Full Time", "Part Time", "Permanent", "Temporary", "Contract", "Internship"]
    employment_data = []

    for i in employment_types:
        if i.lower() in employment_type.replace("-", " ").lower():
            employment_data.append(i)

    return ",".join( tuple(employment_data) )

def insert_into_database(job_object:dict, connection, cursor):
    job_title = job_object["title"]
    job_location = job_object["location"]
    salary = job_object.get("salary", "Negotiable")
    job_description = job_object.get("description", "No description given")
    company = job_object["company"]
    employment_type = job_object["employment_type"]

    if(job_title != "Unknown"):
        get_statemet = f"""SELECT job_description FROM job
                                WHERE job_title = '{job_title}' AND salary = '{salary}'
                                AND company = '{company}' AND employment_type = '{employment_type}';
                        """
        cursor.execute(get_statemet)

        duplicate = False

        for i in cursor.fetchall():
            if (i[0] == job_description):
                duplicate = True
                break
                
        if(not duplicate):
            insert_statement = """INSERT INTO job (jobid, job_title, job_location, salary, job_description, company, employment_type)VALUES (NULL, ?, ?, ?, ?, ?, ?);"""
            res = cursor.execute(insert_statement, (job_title, job_location, salary, job_description, company, employment_type))
            if res == 0:
                print("Error inserting data: ", job_title, job_location, salary, job_description, company, employment_type)
                return 0
        else:
            return -1
        connection.commit()
    return 1



def get_job_info(job_title: str, location: str, specified_job_boards: list[str] = []) :

    driver = get_firefox_driver()

    for job_board_name in load_targeted_job_board(specified_job_boards):

        driver.get(url=get_job_board_search_url(job_title, location, job_board_name))
        stall_driver(driver)

        for job_card in get_job_cards_from_html(driver.page_source, job_board_name):

            job_url = get_job_url(job_board_name, job_card)

            if job_url != None:

                driver.get(url=job_url)
                stall_driver(driver)
                
                yield get_job_json(driver.page_source, job_board_name, job_url)

    yield None

