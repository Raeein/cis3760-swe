DROP DATABASE IF EXISTS template_db;
CREATE DATABASE  template_db;

USE template_db;

DROP TABLE IF EXISTS note;
DROP TABLE IF EXISTS job;

create table note
(
    id int auto_increment comment 'Primary Key'
        primary key,
    text varchar(255) null
);

create table job
(
    jobid int auto_increment comment 'Primary Key'
        primary key,
    job_title VARCHAR(255) NOT NULL,
    job_location VARCHAR(255) NOT NULL,
    salary VARCHAR(255) NOT NULL
);