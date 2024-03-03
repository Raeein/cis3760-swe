// Comment out this file if you figure out how to configure H2 database wtih mariadb. i give up.
//package com.pixelate.geojobsearch.repository;
//
//import com.pixelate.geojobsearch.models.Job;
//
//import org.assertj.core.api.Assertions;
//import org.junit.jupiter.api.BeforeEach;
//import org.junit.jupiter.api.Test;
//import org.springframework.beans.factory.annotation.Autowired;
//import org.springframework.boot.jdbc.EmbeddedDatabaseConnection;
//import org.springframework.boot.test.autoconfigure.jdbc.AutoConfigureTestDatabase;
//import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;
//import org.springframework.test.context.ActiveProfiles;
//
//import java.util.List;
//import java.util.Optional;
//
//@DataJpaTest
//@ActiveProfiles("test")
//@AutoConfigureTestDatabase(connection = EmbeddedDatabaseConnection.H2)
//public class JobsRepositoryTests {
//    private JobsRepository jobsRepository;
//
//    @Autowired
//    public JobsRepositoryTests(JobsRepository jobsRepository) {
//        this.jobsRepository = jobsRepository;
//    }
//
//    @BeforeEach
//    public void setUp() {
//        Job job = new Job();
//        job.setJobId(1);
//        job.setJobTitle("Software Engineer");
//        job.setSalary("100000");
//        job.setJobLocation("New York");
//        jobsRepository.save(job);
//    }
//
//
//    @Test
//    public void testGetJobCount() {
//        Integer result = jobsRepository.getJobCount();
//        Assertions.assertThat(result).isEqualTo(1);
//    }
//
//    @Test
//    public void testGetJob() {
//        Optional<Job> result = jobsRepository.findById(1);
//        Assertions.assertThat(result.get().getJobId()).isEqualTo(1);
//    }
//
//    @Test
//    public void testGetAllJobs() {
//        List<Job> result = jobsRepository.findAll();
//        Assertions.assertThat(result.size()).isEqualTo(1);
//    }
//
//    @Test
//    public void testDeleteJob() {
//        jobsRepository.deleteById(1);
//        Optional<Job> result = jobsRepository.findById(1);
//        Assertions.assertThat(result).isEmpty();
//    }
//
//    @Test
//    public void testUpdateJob() {
//        Job job = new Job();
//        job.setJobId(1);
//        job.setJobTitle("Software Developer");
//        job.setJobLocation("New York");
//        job.setSalary("80000");
//        jobsRepository.save(job);
//        Optional<Job> result = jobsRepository.findById(1);
//        Assertions.assertThat(result.get().getJobTitle()).isEqualTo("Software Developer");
//    }
//
//
//}
