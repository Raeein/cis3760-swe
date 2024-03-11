import mariadb
import sys
import os
# import json
import scraper
import time


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
    print("Start job scraping session")
    job_object_generator = scraper.get_job_info("Software Developer", "Toronto, ON", ["Canadian Job Bank", "Indeed"])
    job_object = next(job_object_generator)
    while(job_object != None):
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
            cur.execute(get_statemet)

            duplicate = False

            for i in cur.fetchall():
                if (i[0] == job_description):
                    duplicate = True
                    break
                    
            if(not duplicate):
                res = cur.execute(insert_statement, (job_title, job_location, salary, job_description, company, employment_type))
                if res == 0:
                    print("Error inserting data: ", job_title, job_location, salary, job_description, company, employment_type)
                

            conn.commit()
        job_object = next(job_object_generator)


    
    print("Finish scraping for this session. Next session starts in 1 hour")
    # cur.execute("SELECT jobid, job_title, job_location, salary, company FROM job")
    # for (jobid, job_title, job_location, salary, company) in cur:
    #     print(f"Job: {jobid}, {job_title}, {job_location}, {salary}, {company}")
    time.sleep(3600)
