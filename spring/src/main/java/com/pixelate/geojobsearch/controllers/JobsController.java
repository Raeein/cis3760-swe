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

    // START
    @GetMapping("/get/{id}/title")
    private @ResponseBody String getJobTitle(@PathVariable Integer id) {
        return jobsService.getJobTitle(id);
    }

    // @GetMapping("/get/{id}/location")
    // private @ResponseBody Job getJobLocation(@PathVariable Integer id) {
    //     return jobsService.getJobLocation(id);
    // }

    // @GetMapping("/get/{id}/salary")
    // private @ResponseBody Job getSalary(@PathVariable Integer id) {
    //     return jobsService.getSalary(id);
    // }
    // END
}
