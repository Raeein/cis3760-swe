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
    salary VARCHAR(255) NOT NULL,
    job_description TEXT NOT NULL,
    company VARCHAR(255) NOT NULL,
    employment_type VARCHAR(255) NOT NULL
);

INSERT INTO job (
    jobid, job_title, job_location,
    salary, job_description, company, employment_type
)VALUES
(NULL, "Frontend Software Developer", "Toronto, ON", "$89,000", "Knowledge with developing using React and TypeScript", "DataCat", "Full Time,Permament"),
(NULL, "Backend Software Developer", "Kitchener, ON", "$95,000", "Knowledge with developing using Java with Spring Boot", "IR Corporation", "Full Time,Temporary"),
(NULL, "Cloud Developer Intern", "Edmonton, ON", "$55,000", "Knowledge with AWS and C#", "Titanium", "Temporary,Internship"),
(NULL, "Senior Fullstack Developer", "Toronto, ON", "$150,000", "Knowledge with Angular and Node Js", "Titanium", "Full time,Permament"),
(NULL, "IT Helpdesk", "Hamilton, ON", "$33,000", "Knowledge with computer hardware", "PCM", "Part Time,Temporary"),
(NULL, "Mobile Developer", "London, ON", "$82,000", "Knowledge with Kotlin and Swift", "PCM", "Full Time,Contract"),
(NULL, "Quantitative Software Engineer", "Toronto, ON", "$220,000", "Knowledge with Python and R", "ABC Investment", "Full Time"),
(NULL, "ML Engineer", "Ottawa, ON", "$150,000", "Knowledge with Pytorch", "ABC Investment", "Full Time,Contract"),
(NULL, "Embedded Engineer", "Ottawa, ON", "$120,000", "Knowledge with Rust and C++", "IMD", "Full Time");
COMMIT;





