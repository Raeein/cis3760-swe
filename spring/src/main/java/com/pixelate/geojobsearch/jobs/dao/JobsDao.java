package com.pixelate.geojobsearch.jobs.dao;

import com.pixelate.geojobsearch.jobs.models.Job;

import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.CrudRepository;

public interface JobsDao extends CrudRepository<Job, Integer> {

    @Query(value = "SELECT COUNT(*) FROM job", nativeQuery = true)
    Integer getJobCount();

}
