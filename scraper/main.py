import mariadb
import sys
import os
# import json
import scraper
import time

from helper import formatEmploymentType


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

insert_statement = """
    INSERT INTO job (
        jobid, job_title, job_location,
        salary, job_description, company, employment_type
    )
    VALUES (NULL, ?, ?, ?, ?, ?, ?);
"""


while (True):
    print("Start job scraping session")
    job_object_generator = scraper.get_job_info(
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

    print("Finish scraping for this session. Next session starts in 1 hour")
    time.sleep(3600)
