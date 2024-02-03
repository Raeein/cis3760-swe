CREATE TABLE IF NOT EXISTS job (
    jobid int auto_increment comment 'Primary Key'
        primary key,
    job_title VARCHAR(255) NOT NULL,
    job_location VARCHAR(255) NOT NULL,
    salary VARCHAR(255) NOT NULL
);
