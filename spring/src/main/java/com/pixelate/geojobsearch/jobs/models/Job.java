package com.pixelate.geojobsearch.jobs.models;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;

@Entity // This tells Hibernate to make a table out of this class
public class Job {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer jobid;
    private String job_title;
    private String job_location;
    private String salary;
    private String job_description;

    public Job() {

    }

    public Job(Integer jobid, String job_title, String job_location, String salary, String job_description) {
        this.jobid = jobid;
        this.job_title = job_title;
        this.job_location = job_location;
        this.salary = salary;
        this.job_description = job_description;
    }

    public Integer getJobId() {
        return jobid;
    }

    public void setId(Integer jobid) {
        this.jobid = jobid;
    }

    public String getJobTitle() {
        return job_title;
    }

    public void setJobTitle(String job_title) {
        this.job_title = job_title;
    }

    public String getJobLocation() {
        return job_location;
    }

    public void setJobLocation(String job_location) {
        this.job_location = job_location;
    }

    public String getSalary() {
        return salary;
    }

    public void setSalary(String salary) {
        this.salary = salary;
    }

    public String getDescription() {
        return job_description;
    }

    public void setDescription(String new_description) {
        this.job_description = new_description;
    }
}