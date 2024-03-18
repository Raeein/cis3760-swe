package com.pixelate.geojobsearch.repository;
import com.pixelate.geojobsearch.models.Job;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

public interface JobsRepository extends JpaRepository<Job, Integer> {
    @Query(value = "SELECT COUNT(*) FROM job", nativeQuery = true)
    Integer getJobCount();
    
    @Query(value = "SELECT * FROM job WHERE LOWER(job_title) LIKE %:keyword%", nativeQuery = true)
    Iterable<Job> searchJobs(@Param("keyword")String keyword); 
}
