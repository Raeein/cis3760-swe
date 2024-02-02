package com.example.cis4900.spring.template.jobs.dao;

import com.example.cis4900.spring.template.jobs.models.Job;

import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.CrudRepository;

public interface NotesDao extends CrudRepository<Note, Integer> {

    @Query("SELECT COUNT(*) FROM jobs")
    Integer getCount();
}
