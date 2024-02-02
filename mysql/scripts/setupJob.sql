CREATE TABLE IF NOT EXISTS jobs (
    jobid INT PRIMARY KEY,
    job_title VARCHAR(255) NOT NULL,
    job_location VARCHAR(255) NOT NULL,
    salary VARCHAR(255) NOT NULL
);
