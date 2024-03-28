package com.pixelate.geojobsearch.service;

import com.pixelate.geojobsearch.models.Job;


public interface JobsService {
    public String addJob(Job newJob);

    public Job getJob(Integer id);
    
    public String updateJob(Job updatedJob);

    public String deleteJob(Integer id);

    public Iterable<Job> allJobs();

    public Integer countJobs();

    public String getJobTitle(Integer id);

    public String getJobLocation(Integer id);
    
    public String getSalary(Integer id);
    
    public String getJobDescription(Integer id);

    public String getCompany(Integer id);
  
    public String getEmploymentType(Integer id);

    public Iterable<Job> searchJobs(String keyword);

    public Iterable<Job> filterEmploymentType(String type);
    
    public Iterable<Job> filterLocation(String location);
    
    public Iterable<Job> filterSalary(float min, float max);
}
