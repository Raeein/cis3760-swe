package com.pixelate.geojobsearch.service.Impl;

import com.pixelate.geojobsearch.models.Job;
import com.pixelate.geojobsearch.service.JobsService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.pixelate.geojobsearch.repository.JobsRepository;

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
}