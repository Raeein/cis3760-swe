package com.pixelate.geojobsearch.controller;
import com.pixelate.geojobsearch.models.Job;
import com.pixelate.geojobsearch.service.JobsService;
import com.pixelate.geojobsearch.controllers.JobsController;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.test.web.servlet.MockMvc;
import org.mockito.junit.jupiter.MockitoExtension;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.extension.ExtendWith;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.ResultActions;
import org.springframework.test.web.servlet.result.MockMvcResultMatchers;
import com.fasterxml.jackson.databind.ObjectMapper;

import static org.mockito.BDDMockito.given;
import static org.mockito.Mockito.doNothing;
import static org.mockito.Mockito.when;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;

import org.assertj.core.api.Assertions;
import org.hibernate.mapping.List;


@WebMvcTest(controllers = JobsController.class)
@AutoConfigureMockMvc(addFilters = false)
@ExtendWith(MockitoExtension.class)
public class JobsControllerTests {
    @Autowired
    private MockMvc mockMvc;

    @MockBean
    JobsService jobsService;

    @Autowired
    private ObjectMapper objectMapper;
    private Job job;

    @BeforeEach
    public void init() {
        job = new Job();
        job.setJobId(1);
        job.setJobTitle("Software Developer");
        job.setJobLocation("New York");
        job.setSalary("80000");
        job.setJobDescription("Develop software applications");
        job.setCompany("Pixelate");
        job.setEmploymentType("Full Time");
    }

    @Test
    public void testAddJob() throws Exception {
        ResultActions result = mockMvc.perform(post("/api/jobs/add")
                .contentType(MediaType.APPLICATION_JSON)
                .content(objectMapper.writeValueAsString(job)))
                .andExpect(MockMvcResultMatchers.status().isOk());
    }

    @Test
    public void testGetJob() throws Exception {
        given(jobsService.getJob(1)).willReturn(job);
        ResultActions result = mockMvc.perform(get("/api/jobs/get/1"))
                .andExpect(MockMvcResultMatchers.status().isOk());
    }

    @Test
    public void testUpdateJob() throws Exception {
        ResultActions result = mockMvc.perform(put("/api/jobs/update")
                .contentType(MediaType.APPLICATION_JSON)
                .content(objectMapper.writeValueAsString(job)))
                .andExpect(MockMvcResultMatchers.status().isOk());
    }

    @Test
    public void testDeleteJob() throws Exception {
        when(jobsService.deleteJob(1)).thenReturn("Job deleted successfully");

        ResultActions result = mockMvc.perform(delete("/api/jobs/delete/1"))
                .andExpect(MockMvcResultMatchers.status().isOk());
    }

    @Test
    public void testAllJobs() throws Exception {
        given(jobsService.allJobs()).willReturn(java.util.Arrays.asList(job));
        ResultActions result = mockMvc.perform(get("/api/jobs/all"))
                .andExpect(MockMvcResultMatchers.status().isOk());
    }

    @Test
    public void testCountJobs() throws Exception {
        given(jobsService.countJobs()).willReturn(1);
        ResultActions result = mockMvc.perform(get("/api/jobs/count"))
                .andExpect(MockMvcResultMatchers.status().isOk());
    }

    @Test
    public void testGetJobTitle() throws Exception {
        given(jobsService.getJobTitle(1)).willReturn("Software Developer");
        ResultActions result = mockMvc.perform(get("/api/jobs/get/1/title"))
                .andExpect(MockMvcResultMatchers.status().isOk());
    }

    @Test
    public void testGetJobLocation() throws Exception {
        given(jobsService.getJobLocation(1)).willReturn("New York");
        ResultActions result = mockMvc.perform(get("/api/jobs/get/1/location"))
                .andExpect(MockMvcResultMatchers.status().isOk());
    }

    @Test
    public void testGetJobSalary() throws Exception {
        given(jobsService.getJobLocation(1)).willReturn("80000");
        ResultActions result = mockMvc.perform(get("/api/jobs/get/1/salary"))
                .andExpect(MockMvcResultMatchers.status().isOk());
    }

    @Test
    public void testGetJobDescription() throws Exception {
        given(jobsService.getJobLocation(1)).willReturn("Develop software applications");
        ResultActions result = mockMvc.perform(get("/api/jobs/get/1/description"))
                .andExpect(MockMvcResultMatchers.status().isOk());
    }

    @Test
    public void testGetJobCompany() throws Exception {
        given(jobsService.getJobLocation(1)).willReturn("Pixelate");
        ResultActions result = mockMvc.perform(get("/api/jobs/get/1/company"))
                .andExpect(MockMvcResultMatchers.status().isOk());
    }

    @Test
    public void testGetJobEmploymentType() throws Exception {
        given(jobsService.getEmploymentType(1)).willReturn("Full time");
        ResultActions result = mockMvc.perform(get("/api/jobs/get/1/company"))
                .andExpect(MockMvcResultMatchers.status().isOk());
    }

    @Test
    public void testSearchKeyword() throws Exception {
        when(jobsService.searchJobs("Software")).thenReturn(java.util.Arrays.asList(job));
        Iterable<Job> result = jobsService.searchJobs("Software");
        Assertions.assertThat(result).isEqualTo(java.util.Arrays.asList(job));

 
    }

    @Test
    public void testFilterEmployment() throws Exception {
        when(jobsService.filterEmploymentType("Full time")).thenReturn(java.util.Arrays.asList(job));
        Iterable<Job> result = jobsService.filterEmploymentType("Full time");
        Assertions.assertThat(result).isEqualTo(java.util.Arrays.asList(job));
    }

    @Test
    public void testFilterLocation() throws Exception {
        when(jobsService.filterLocation("New York")).thenReturn(java.util.Arrays.asList(job));
        Iterable<Job> result = jobsService.filterLocation("New York");
        Assertions.assertThat(result).isEqualTo(java.util.Arrays.asList(job));
    }
}
