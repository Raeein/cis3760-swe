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
        user=user,
        password=password,
        host=host,
        port=port,
        database=database
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

print("Connected to MariaDB Platform!")
cur = conn.cursor()

insert_statement = """
    INSERT INTO job (jobid, job_title, job_location, salary, job_description, company, employment_type)
    VALUES (NULL, ?, ?, ?, ?, ?, ?);
    """

# uncomment the code below to use test data

# with open("fake_jobs.json") as f:
#     data = json.load(f)
#     for job in data['jobs']:
#         job_title = job["title"]
#         job_location = job["location"]
#         salary = job.get("salary", "Negotiable")  # Assuming 'salary' might not be present in all records

#         res = cur.execute(insert_statement, (job_title, job_location, salary))
#         if res == 0:
#             print("Error inserting data: ", job_title, job_location, salary)


while(True):
    jobObjectList = scraper.get_job_info("Software Developer", "Toronto, ON", ["Canadian Job Bank", "Indeed"])
    for job in jobObjectList:
        job_title = job["title"]
        job_location = job["location"]
        salary = job.get("salary", "Negotiable")
        job_description = job.get("description", "No description given")
        company = job["company"]
        employment_type = formatEmploymentType(job["employment_type"])

        if(job_title != "Unknown"):
            res = cur.execute(insert_statement, (job_title, job_location, salary, job_description, company, employment_type))

            if res == 0:
                print("Error inserting data: ", job_title, job_location, salary, job_description, company, employment_type)


    conn.commit()
    print("Job database populated!")
    cur.execute("SELECT jobid, job_title, job_location, salary, company, employment_type FROM job")
    for (jobid, job_title, job_location, salary, company, employment_type) in cur:
        print(f"Job: {jobid}, {job_title}, {job_location}, {salary}, {company}, {employment_type}")
    time.sleep(5000)