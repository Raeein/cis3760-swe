import time
import random
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
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

        "job_employment_element": "div",
        "job_employment_search_object": {"aria-label": "Job type"},
        "job_employment_string_parse": 8,

        "job_pay_element": "div",
        "job_pay_search_object": {"aria-label": "Pay"},
        "job_pay_string_parse": 3,

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

        "job_employment_element": "span",
        "job_employment_search_object": {"property": "employmentType"},

        "job_pay_element": "span",
        "job_pay_search_object": {"property": "baseSalary"},

        "job_description_element": "div",
        "job_description_search_object": {"id": "comparisonchart"},
    }
}

# set web driver options
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
# https://www.whatismybrowser.com/guides/the-latest-user-agent/chrome seem to be working
options.add_argument(
    """user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36""")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)


def get_job_cards_from_html(html_string: str, job_board_name: str):
    job_cards = []

    soup = BeautifulSoup(html_string, "html.parser")

    job_board_object = job_board_list_object[job_board_name]
    job_cards = soup.find_all(job_board_object["job_card_element"], class_=job_board_object["job_card_class"])

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


def get_job_info(job_title: str, location: str, specified_job_boards: list[str] = []) -> list[dict]:
    job_json_object_list = []
    job_board_search_list = []

    if (specified_job_boards == []):
        job_board_search_list = list(job_board_list_object.keys())
    else:
        for i in specified_job_boards:
            if i in list(job_board_list_object.keys()):
                job_board_search_list.append(i)

    for job_board_name in job_board_search_list:
        url = job_board_list_object[job_board_name]["job_board_search_url"].format(job_title=job_title,
                                                                                   location=location)

        driver.get(url=url)
        time.sleep(random.randint(2, 6))

        job_cards = get_job_cards_from_html(driver.page_source, job_board_name)

        for job_card in job_cards:
            job_json_object = {}
            job_card = "<div>" + str(job_card) + "</div>"
            job_card = BeautifulSoup(job_card, "html.parser")

            job_url = job_board_list_object[job_board_name]["job_board_base_url"] + job_card.find('a')['href']

            if job_url is not None:
                driver.get(url=job_url)
                time.sleep(random.randint(2, 8))

                job_json_object["title"] = get_job_attribute(driver.page_source, "job_title", job_board_name)
                job_json_object["company"] = get_job_attribute(driver.page_source, "job_company", job_board_name)
                job_json_object["location"] = get_job_attribute(driver.page_source, "job_location", job_board_name)
                job_json_object["employment_type"] = get_job_attribute(driver.page_source, "job_employment",
                                                                       job_board_name)
                job_json_object["salary"] = get_job_attribute(driver.page_source, "job_pay", job_board_name)
                job_json_object["description"] = get_job_attribute(driver.page_source, "job_description", job_board_name)
                job_json_object["url"] = job_url

                print("-" * 20)
                print("Title: ", job_json_object["title"])
                print("Company: ", job_json_object["company"])
                print("Location: ", job_json_object["location"])
                print("Employment type: ", job_json_object["employment_type"])
                print("Salary: ", job_json_object["salary"])
                print("Description: ", job_json_object["description"])
                print("Url: ", job_json_object["url"])
                print("-" * 20)
                job_json_object_list.append(job_json_object)

    return job_json_object_list


if __name__ == "__main__":
    get_job_info("Software Developer", "Toronto, On", ["Canadian Job Bank", ])
