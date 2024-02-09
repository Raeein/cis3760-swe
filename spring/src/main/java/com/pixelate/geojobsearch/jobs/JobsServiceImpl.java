package com.pixelate.geojobsearch.jobs;

import com.pixelate.geojobsearch.jobs.models.Job;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.pixelate.geojobsearch.jobs.dao.JobsDao;

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