package com.pixelate.geojobsearch.service;

import com.pixelate.geojobsearch.models.Job;


public interface JobsService {
    public String addJob(Job newJob);

    public Job getJob(Integer id);
    
    public String updateJob(Job updatedJob);

    public String deleteJob(Integer id);

    public Iterable<Job> allJobs();

    public Integer countJobs();

    // START
    public String getJobTitle(Integer id);

    // public Job getJobLocation(Integer id);
    
    // public Job getSalary(Integer id);
    // END
}
