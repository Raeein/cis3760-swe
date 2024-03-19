import mariadb
import sys
import os
# import json
import scraper
import time
import platform
import random
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium import webdriver


def get_firefox_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("""
                            user-agent=Mozilla/5.0
                            (Windows NT 10.0; Win64; x64)
                            AppleWebKit/537.36 (KHTML, like Gecko)
                            Chrome/121.0.0.0 Safari/537.36
                        """.replace("\n", "").replace(" ", ""))
    gecko_driver_path = ''
    if platform.machine() == 'aarch64':
        gecko_driver_path = '/usr/bin/geckodriver-arm'
    else:
        gecko_driver_path = '/usr/bin/geckodriver'
    try:
        service = Service(gecko_driver_path)
        driver = webdriver.Firefox(service=service, options=options)
        driver.execute_script(
            "Object.defineProperty(navigator,'webdriver',{get:()=>undefined})"
        )
        driver.implicitly_wait(10)
        return driver
    except Exception as e:
        print(f"Error initializing Firefox WebDriver: {e}")
        exit()


def stall_driver(driver: webdriver.Firefox):
    driver.implicitly_wait(random.randint(10, 20))
    time.sleep(random.randint(2, 5))


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


user = os.getenv('DB_USER', 'default_user')
password = os.getenv('DB_PASSWORD', 'default_password')
host = os.getenv('DB_ADDRESS', 'default_host')
port = int(os.getenv('DB_PORT', 'default_port'))
database = os.getenv('DB_DATABASE', 'default_database')

try:
    conn = mariadb.connect(
        user=user, password=password, host=host, port=port, database=database
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

print("Connected to MariaDB Platform!")
cur = conn.cursor()


print("Start job scraping session")
job_object_generator = get_job_info(
    "Software Developer", "Toronto, ON", ["Canadian Job Bank", "Indeed"]
)
job_object = next(job_object_generator)
while (job_object is not None):
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
time.sleep(5)
