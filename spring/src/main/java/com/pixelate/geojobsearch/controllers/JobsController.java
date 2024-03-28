package com.pixelate.geojobsearch.controllers;

import com.pixelate.geojobsearch.service.JobsService;
import com.pixelate.geojobsearch.models.Job;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping(path = "/api/jobs")
public class JobsController {
    private JobsService jobsService;

    @Autowired
    JobsController(JobsService jobsService) {
        this.jobsService = jobsService;
    }

    @PostMapping("/add")
    private @ResponseBody String addJob(@RequestBody Job newJob) {
        return jobsService.addJob(newJob);
    }

    @GetMapping("/get/{id}")
    private @ResponseBody Job getJob(@PathVariable Integer id) {
        return jobsService.getJob(id);
    }

    @PutMapping("/update")
    private @ResponseBody String updateJob(@RequestBody Job updatedJob) {
        return jobsService.updateJob(updatedJob);
    }

    @DeleteMapping("/delete/{id}")
    private @ResponseBody String deleteJob(@PathVariable Integer id) {
        return jobsService.deleteJob(id);
    }

    @GetMapping("/all")
    private @ResponseBody Iterable<Job> allJobs() {
        return jobsService.allJobs();
    }


    @GetMapping("/count")
    private @ResponseBody Integer countJobs() {
        return jobsService.countJobs();
    }

    @GetMapping("/get/{id}/title")
    private @ResponseBody String getJobTitle(@PathVariable Integer id) {
        return jobsService.getJobTitle(id);
    }

    @GetMapping("/get/{id}/location")
    private @ResponseBody String getJobLocation(@PathVariable Integer id) {
        return jobsService.getJobLocation(id);
    }

    @GetMapping("/get/{id}/salary")
    private @ResponseBody String getSalary(@PathVariable Integer id) {
        return jobsService.getSalary(id);
    }

    @GetMapping("/get/{id}/description")
    private @ResponseBody String getJobDescription(@PathVariable Integer id) {
        return jobsService.getJobDescription(id);
    }

    @GetMapping("/get/{id}/company")
    private @ResponseBody String getCompany(@PathVariable Integer id) {
        return jobsService.getCompany(id);
    }

    @GetMapping("/get/{id}/employment-type")
    private @ResponseBody String getEmploymentType(@PathVariable Integer id) {
        return jobsService.getEmploymentType(id); 
    }

    @GetMapping("/searches/{keyword}")
    private @ResponseBody Iterable<Job> searchJobs(@PathVariable String keyword) {
        return jobsService.searchJobs(keyword);
    }

    @GetMapping("/filter/employments/{type}")
    private @ResponseBody Iterable<Job> filterEmploymentType(@PathVariable String type) {
        return jobsService.filterEmploymentType(type);
    }

    @GetMapping("/filter/locations/{location}")
    private @ResponseBody Iterable<Job> filterLocation(@PathVariable String location) {
        return jobsService.filterLocation(location);
    }

    @GetMapping("/filter/salaries/{min}&{max}")
    private @ResponseBody Iterable<Job> filterSalary(@PathVariable float min, @PathVariable float max) {
        return jobsService.filterSalary(min, max);
    }
}
