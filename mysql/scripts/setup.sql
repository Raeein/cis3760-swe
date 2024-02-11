DROP DATABASE IF EXISTS geo_job_search_db;
CREATE DATABASE geo_job_search_db;

USE geo_job_search_db;

DROP TABLE IF EXISTS job;

create table job
(
    jobid int auto_increment comment 'Primary Key'
        primary key,
    job_title VARCHAR(255) NOT NULL,
    job_location VARCHAR(255) NOT NULL,
    salary VARCHAR(255) NOT NULL
    job_description VARCHAR(255) NOT NULL
);