package com.example.cis4900.spring.template.jobs;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.cis4900.spring.template.jobs.dao.JobsDao;
import com.example.cis4900.spring.template.jobs.models.Job;

@Service
public class JobsServiceImpl implements JobsService {
    @Autowired
    private JobsDao jobsDao;

    @Override
    public String addJob(Job newJob) {
        try {
            jobsDao.save(newJob);
        } catch (Exception exception) {
            return exception.getMessage();
        }
        return "Saved";
    }

    @Override
    public Job getJob(Integer id) {
        return jobsDao.findById(id).get();
    }

    @Override
    public String updateJob(Job updatedJob) {
        try {
            jobsDao.save(updatedJob);
        } catch (Exception exception) {
            return exception.getMessage();
        }
        return "Updated";
    }

    @Override
    public String deleteJob(Integer id) {
        try {
            jobsDao.deleteById(id);
        } catch (Exception exception) {
            return exception.getMessage();
        }
        return "Deleted";
    }

    @Override
    public Iterable<Job> allJobs() {
        return jobsDao.findAll();
    }

    @Override
    public Integer countJobs() {
        return jobsDao.getJobCount();
    }
}