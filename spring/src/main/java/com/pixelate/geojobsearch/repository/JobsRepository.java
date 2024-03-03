package com.pixelate.geojobsearch.repository;

import com.pixelate.geojobsearch.models.Job;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

public interface JobsRepository extends JpaRepository<Job, Integer> {
    @Query(value = "SELECT COUNT(*) FROM job", nativeQuery = true)
    Integer getJobCount();

}
