package com.pixelate.geojobsearch.service;

import com.pixelate.geojobsearch.models.Job;
import com.pixelate.geojobsearch.repository.JobsRepository;
import com.pixelate.geojobsearch.service.Impl.JobsServiceImpl;

import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.Mockito;
import org.mockito.junit.jupiter.MockitoExtension;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;

import java.util.Optional;

import static org.junit.jupiter.api.Assertions.assertAll;
import static org.mockito.Mockito.doNothing;
import static org.mockito.Mockito.when;

@ExtendWith(MockitoExtension.class)
public class JobsServiceTests {

    @Mock
    private JobsRepository jobsRepository;

    @InjectMocks
    private JobsServiceImpl jobsService;


    private Job job;

    @BeforeEach
    public void setUp() {
        job = new Job();
        job.setJobId(1);
        job.setJobTitle("Software Engineer");
        job.setJobLocation("New York");
        job.setSalary("100000");
        job.setJobDescription("Develop software applications");
        job.setCompany("Pixelate");
    }

    @Test
    public void testAddJob() {
        when(jobsRepository.save(job)).thenReturn(job);
        String result = jobsService.addJob(job);
        Assertions.assertThat(result).isEqualTo("Saved");
    }

    @Test
    public void testGetJob() {
        when(jobsRepository.findById(1)).thenReturn(Optional.of(job));
        Job result = jobsService.getJob(1);
        assertAll(
                () -> Assertions.assertThat(result.getJobId()).isEqualTo(1),
                () -> Assertions.assertThat(result.getJobTitle()).isEqualTo("Software Engineer"),
                () -> Assertions.assertThat(result.getJobLocation()).isEqualTo("New York"),
                () -> Assertions.assertThat(result.getSalary()).isEqualTo("100000"),
                () -> Assertions.assertThat(result.getJobDescription()).isEqualTo("Develop software applications"),
                () -> Assertions.assertThat(result.getCompany()).isEqualTo("Pixelate")
        );
    }

    @Test
    public void testUpdateJob() {
        when(jobsRepository.save(job)).thenReturn(job);
        String result = jobsService.updateJob(job);
        Assertions.assertThat(result).isEqualTo("Updated");
    }

    @Test
    public void testDeleteJob() {
        doNothing().when(jobsRepository).deleteById(1);
        String result = jobsService.deleteJob(1);
        Assertions.assertThat(result).isEqualTo("Deleted");
    }

    @Test
    public void testAllJobs() {
        when(jobsRepository.findAll()).thenReturn(java.util.Arrays.asList(job));
        Iterable<Job> result = jobsService.allJobs();
        Assertions.assertThat(result).isEqualTo(java.util.Arrays.asList(job));
    }

    @Test
    public void testCountJobs() {
        when(jobsRepository.getJobCount()).thenReturn(1);
        Integer result = jobsService.countJobs();
        Assertions.assertThat(result).isEqualTo(1);
    }
}
