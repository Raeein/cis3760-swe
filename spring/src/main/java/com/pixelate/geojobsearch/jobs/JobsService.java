package com.pixelate.geojobsearch.jobs;

import com.pixelate.geojobsearch.jobs.models.Job;


public interface JobsService {
    public String addJob(Job newJob);

    public Job getJob(Integer id);
    
    public String updateJob(Job updatedJob);

    public String deleteJob(Integer id);

    public Iterable<Job> allJobs();

    public Integer countJobs();
}
