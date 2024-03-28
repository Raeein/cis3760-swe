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

    @Query(value = "SELECT * FROM job WHERE LOWER(employment_type) LIKE %:type%", nativeQuery = true)
    Iterable<Job> filterEmploymentType(@Param("type")String type); 

    @Query(value = "SELECT * FROM job WHERE LOWER(job_location) LIKE %:location%", nativeQuery = true)
    Iterable<Job> filterLocation(@Param("location")String location); 

    @Query(value = "SELECT * FROM job WHERE salary <> 'Salary not given' AND " +
               "CAST(SUBSTRING(salary, 2) AS DECIMAL(10,2)) " +
               "BETWEEN :min AND :max", nativeQuery = true)
    Iterable<Job> filterSalary(@Param("min") float min, @Param("max") float max);

}
