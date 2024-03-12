package com.pixelate.geojobsearch.models;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.Setter;
import lombok.NoArgsConstructor;

@Entity
@Getter @Setter @NoArgsConstructor @AllArgsConstructor
public class Job {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "jobid")
    private Integer jobId;

    @Column(name = "job_title")
    private String jobTitle;
    @Column(name = "job_location")
    private String jobLocation;

    @Column(name = "salary")
    private String salary;

    @Column(name = "job_description")
    private String jobDescription;

    @Column(name = "company")
    private String company;

    @Column(name = "employment_type")
    private String employmentType;
}