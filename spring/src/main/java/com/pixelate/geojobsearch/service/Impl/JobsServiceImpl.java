package com.pixelate.geojobsearch.service.Impl;

import com.pixelate.geojobsearch.models.Job;
import com.pixelate.geojobsearch.service.JobsService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.pixelate.geojobsearch.repository.JobsRepository;

import java.util.Optional;

@Service
public class JobsServiceImpl implements JobsService {
    @Autowired
    private JobsRepository jobsRepository;

    @Override
    public String addJob(Job newJob) {
        try {
            jobsRepository.save(newJob);
        } catch (Exception exception) {
            return exception.getMessage();
        }
        return "Saved";
    }

    @Override
    public Job getJob(Integer id) {
        return jobsRepository.findById(id).get();
    }

    @Override
    public String updateJob(Job updatedJob) {
        try {
            jobsRepository.save(updatedJob);
        } catch (Exception exception) {
            return exception.getMessage();
        }
        return "Updated";
    }

    @Override
    public String deleteJob(Integer id) {
        try {
            jobsRepository.deleteById(id);
        } catch (Exception exception) {
            return exception.getMessage();
        }
        return "Deleted";
    }

    @Override
    public Iterable<Job> allJobs() {
        return jobsRepository.findAll();
    }

    @Override
    public Integer countJobs() {
        return jobsRepository.getJobCount();
    }

    @Override
    public String getJobTitle(Integer id) {
        return jobsRepository.findById(id).map(Job::getJobTitle).orElse("Job not found");
    }

    @Override
    public String getJobLocation(Integer id) {
        return jobsRepository.findById(id).map(Job::getJobLocation).orElse("Job not found");
    }

    @Override
    public String getSalary(Integer id) {
        return jobsRepository.findById(id).map(Job::getSalary).orElse("Job not found");
    }

    @Override
    public String getJobDescription(Integer id) {
        return jobsRepository.findById(id).map(Job::getJobDescription).orElse("Job not found");
    }

    @Override
    public String getCompany(Integer id) {
        return jobsRepository.findById(id).map(Job::getCompany).orElse("Job not found");
    }

    @Override
    public String getEmploymentType(Integer id) {
        return jobsRepository.findById(id).map(Job::getEmploymentType).orElse("Job not found");
    }

    @Override
    public Iterable<Job> searchJobs(String keyword) {
        return jobsRepository.searchJobs(keyword);
    }

    @Override
    public Iterable<Job> filterEmploymentType(String type) {
        return jobsRepository.filterEmploymentType(type);
    }

    @Override
    public Iterable<Job> filterLocation(String location) {
        return jobsRepository.filterLocation(location);
    }

    @Override
    public Iterable<Job> filterSalary(float min, float max) {
        return jobsRepository.filterSalary(min, max);
    }
}