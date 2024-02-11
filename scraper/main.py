import mariadb
import sys
import os
import json
import scraper


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
    INSERT INTO job (jobid, job_title, job_location, salary)
    VALUES (NULL, ?, ?, ?);
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


jobObjectList = scraper.getJobInfo("Software Developer", "Toronto, ON")
for job in jobObjectList:
    job_title = job["title"]
    job_location = job["location"]
    salary = job.get("salary", "Negotiable")
    res = cur.execute(insert_statement, (job_title, job_location, salary))

    if res == 0:
        print("Error inserting data: ", job_title, job_location, salary)


conn.commit()
print("Job database populated!")

# Make sure the data is in the database
# cur.execute("SELECT * FROM job")
# for (jobid, job_title, job_location, salary) in cur:
#     print(f"Job: {jobid}, {job_title}, {job_location}, {salary}")

conn.close()
