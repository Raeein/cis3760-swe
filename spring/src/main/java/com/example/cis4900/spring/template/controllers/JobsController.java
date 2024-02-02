package com.example.cis4900.spring.template.controllers;

import com.example.cis4900.spring.template.jobs.JobsService;
import com.example.cis4900.spring.template.jobs.models.Job;

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
    NotesController(JobsService jobsService) {
        this.jobsService = jobsService;
    }

    @PostMapping("/add")
    private @ResponseBody String addJob(@RequestBody Job newJob) {
        return jobsService.addJob(newJob);
    }

    @GetMapping("/get/{id}")
    private @ResponseBody Note getJob(@PathVariable Integer id) {
        return jobsService.getJob(id);
    }

    @PutMapping("/update")
    private @ResponseBody String updateJob(@RequestBody Note updatedJob) {
        return jobsService.updateJob(updatedJob);
    }

    @DeleteMapping("/delete/{id}")
    private @ResponseBody String deleteJob(@PathVariable Integer id) {
        return jobsService.deleteJob(id);
    }

    @GetMapping("/all")
    private @ResponseBody Iterable<Note> allJobs() {
        return jobsService.allJobs();
    }

    @GetMapping("/count")
    private @ResponseBody Integer count() {
        return jobsService.count();
    }
}
