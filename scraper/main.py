import json
import scraper
import db_util
import os
from driver_util import get_firefox_driver
from driver_util import stall_driver


def get_job_info(
        job_title: str,
        location: str,
        specified_job_boards: list[str] = []
):
    driver = get_firefox_driver()
    for job_board_name in scraper.load_targeted_job_board(specified_job_boards):
        driver.get(url=scraper.get_search_url(job_title, location, job_board_name))
        stall_driver(driver)
        for job_card in scraper.get_job_cards_from_html(
                driver.page_source, job_board_name
        ):
            job_url = scraper.get_job_url(job_board_name, job_card)
            if job_url is not None:
                driver.get(url=job_url)
                stall_driver(driver)
                job_json = scraper.get_job_json(
                    driver.page_source,
                    job_board_name, job_url
                )
                yield job_json
    yield None


conn = db_util.get_connection()
cur = conn.cursor()


print("Reading the config file")
config_file_name = "scraper_config.json"

if not os.path.exists(config_file_name):
    print("Config file not found. Exiting...")
    exit()

try:
    with open(config_file_name, 'r') as file:
        config = json.load(file)

        required_keys = ['search_term', 'location', 'websites']
        if not all(key in config for key in required_keys):
            missing_keys = [key for key in required_keys if key not in config]
            print("Error. Missing required key(s): ", missing_keys)

        print("search_term: ", config["search_term"])
        print("location: ", config["location"])
        print("websites: ", config["websites"])

except json.JSONDecodeError:
    print("Error. Invalid JSON format. Exiting...")
    exit()
except Exception as e:
    print("Error. Exiting...", e)
    exit()

print("Start job scraping session")
job_object_generator = get_job_info(
    config["search_term"], config["location"], config["websites"]
)

job_object = next(job_object_generator)
while job_object is not None:
    res = scraper.insert_into_database(job_object, conn, cur)
    if res == 0:
        print(
            "Error inserting data: ", job_object["title"],
            job_object["location"], job_object["salary"],
            job_object["description"], job_object["company"],
            job_object["employment_type"]
        )
    job_object = next(job_object_generator)

print("Finish scraping for this session. Next session starts at 12:00 am")
conn.close()
