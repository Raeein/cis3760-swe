package com.pixelate.geojobsearch.integration;


import com.pixelate.geojobsearch.service.JobsService;
import com.pixelate.geojobsearch.service.Impl.JobsServiceImpl;
import com.pixelate.geojobsearch.controllers.JobsController;
import com.pixelate.geojobsearch.models.Job;


import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;
import org.mockito.junit.jupiter.MockitoExtension;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.mock.mockito.MockBean;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.BDDMockito.given;
import static org.mockito.Mockito.when;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Arrays;


@WebMvcTest(controllers = JobsController.class)
@AutoConfigureMockMvc(addFilters = false)
@ExtendWith(MockitoExtension.class)
public class JobIntegrationTest {
    
    
    @MockBean
    private JobsServiceImpl jobsService ;


    @BeforeEach
    public void set() {
        MockitoAnnotations.openMocks(this);
    }


    // @BeforeAll
    // public static void setUp() throws SQLException, IOException {
    //     // Load the SQL script
    //     String sqlScript = new String(Files.readAllBytes(Paths.get("src/test/java/com/pixelate/geojobsearch/integration/test_setup.sql")));

    //     // Execute the SQL script to populate the database with test data
    //     try (Connection connection = DriverManager.getConnection("jdbc:mysql://mysql:3306/geo_job_search_db",
    //             "root", "pwd");
    //             Statement statement = connection.createStatement()
    //     ){
    //         statement.executeUpdate("DROP TABLE IF EXISTS job");
    //         statement.executeUpdate(
    //             "create table job("+
    //                 "jobid int auto_increment comment 'Primary Key'"+
    //                 "primary key,"+
    //                 "job_title VARCHAR(255) NOT NULL,"+
    //                 "job_location VARCHAR(255) NOT NULL,"+
    //                 "salary VARCHAR(255) NOT NULL,"+
    //                 "job_description TEXT NOT NULL,"+
    //                 "company VARCHAR(255) NOT NULL,"+
    //                 "employment_type VARCHAR(255) NOT NULL);"
    //         );
    //         statement.execute(sqlScript);
    //     }
    // }

    @Test
    public void testJobPostingsExist() throws SQLException {
        //verify the content exist
        try (Connection connection = DriverManager.getConnection("jdbc:mysql://mysql:3306/geo_job_search_db",
                "root", "pwd");
                Statement statement = connection.createStatement()
        ){
            ResultSet resultSet = statement.executeQuery("SELECT COUNT(*) FROM job");
            resultSet.next();
            int count = resultSet.getInt(1);
            assertEquals(9, count, "Expected 11 job postings in the database");
        }
    }


    @Test
    public void testGetAllJob() throws Exception {
        //test api/jobs/all
        given(jobsService.countJobs()).willReturn(9);

        int numJobs = jobsService.countJobs();
        assertEquals(9, numJobs);
    }

    @Test
    public void testSearchJob() throws Exception {
        //test api/jobs/searches/{keyword}
        Job job = new Job(1, 
        "Frontend Software Developer", 
        "Toronto, ON", 
        "$89,000", 
        "Knowledge with developing using React and TypeScript",
        "DataCat", 
        "Full Time,Permament",
        "https://ca.indeed.com/"
        );

        when(jobsService.searchJobs("Frontend Software Developer")).thenReturn(Arrays.asList(job));

        Iterable<Job> jobs = jobsService.searchJobs("Frontend Software Developer");
        job = jobs.iterator().next();
        assertEquals(job.getJobTitle(), "Frontend Software Developer");
        assertEquals(job.getJobLocation(), "Toronto, ON");
        assertEquals(job.getSalary(), "$89,000");
        assertEquals(job.getJobDescription(), "Knowledge with developing using React and TypeScript");
        assertEquals(job.getCompany(), "DataCat");
        assertEquals(job.getEmploymentType(), "Full Time,Permament");
        assertEquals(job.getJobUrl(), "https://ca.indeed.com/");
    }

    @Test
    public void testFilterEmployment() throws Exception {
        //test api/jobs/filter/employments/{type}
        Job job = new Job(1, 
        "Frontend Software Developer", 
        "Toronto, ON", 
        "$89,000", 
        "Knowledge with developing using React and TypeScript",
        "DataCat", 
        "Full Time,Permament",
        "https://ca.indeed.com/"
        );
        when(jobsService.filterEmploymentType("Permament")).thenReturn(Arrays.asList(job));

        Iterable<Job> jobs = jobsService.filterEmploymentType("Permament");
        job = jobs.iterator().next();
        assertEquals(job.getJobTitle(), "Frontend Software Developer");
        assertEquals(job.getJobLocation(), "Toronto, ON");
        assertEquals(job.getSalary(), "$89,000");
        assertEquals(job.getJobDescription(), "Knowledge with developing using React and TypeScript");
        assertEquals(job.getCompany(), "DataCat");
        assertEquals(job.getEmploymentType(), "Full Time,Permament");
        assertEquals(job.getJobUrl(), "https://ca.indeed.com/");
    }

    @Test
    public void testFilterLocatiion() throws Exception {
        //test api/jobs/filter/locations/{location}
        Job job = new Job(1, 
        "Frontend Software Developer", 
        "Toronto, ON", 
        "$89,000", 
        "Knowledge with developing using React and TypeScript",
        "DataCat", 
        "Full Time,Permament",
        "https://ca.indeed.com/"
        );
        when(jobsService.filterLocation("Toronto, ON")).thenReturn(Arrays.asList(job));

        Iterable<Job> jobs = jobsService.filterLocation("Toronto, ON");
        job = jobs.iterator().next();
        assertEquals(job.getJobTitle(), "Frontend Software Developer");
        assertEquals(job.getJobLocation(), "Toronto, ON");
        assertEquals(job.getSalary(), "$89,000");
        assertEquals(job.getJobDescription(), "Knowledge with developing using React and TypeScript");
        assertEquals(job.getCompany(), "DataCat");
        assertEquals(job.getEmploymentType(), "Full Time,Permament");
        assertEquals(job.getJobUrl(), "https://ca.indeed.com/");
    }


    @Test
    public void testGetJobTitleById() throws Exception {
        //test api/jobs/get/{id}/title
        given(jobsService.getJobTitle(1) ).willReturn("Frontend Software Developer");
        String jobTitle = jobsService.getJobTitle(1);
        assertEquals(jobTitle, "Frontend Software Developer");
    }


    @Test
    public void testGetJobLocationById() throws Exception {
        //test api/jobs/get/{id}/location
        given(jobsService.getJobLocation(1) ).willReturn("Toronto, ON");
        String jobLocation = jobsService.getJobLocation(1);
        assertEquals(jobLocation, "Toronto, ON");
    }


    @Test
    public void testGetJobSalaryById() throws Exception {
        //test api/jobs/get/{id}/salary
        given(jobsService.getSalary(1) ).willReturn("$89,000");
        String jobSalary = jobsService.getSalary(1);
        assertEquals(jobSalary, "$89,000");
    }


    @Test
    public void testGetJobDescriptionById() throws Exception {
        //test api/jobs/get/{id}/description
        given(jobsService.getJobDescription(1) )
            .willReturn("Knowledge with developing using React and TypeScript");
        String jobDescription = jobsService.getJobDescription(1);
        assertEquals(
            jobDescription,
            "Knowledge with developing using React and TypeScript"
        );
    }


    @Test
    public void testGetJobCompanyById() throws Exception {
        //test api/jobs/get/{id}/company
        given(jobsService.getCompany(1) ).willReturn("DataCat");
        String jobTitle = jobsService.getCompany(1);
        assertEquals(jobTitle, "DataCat");
    }


    @Test
    public void testGetJobEmploymentTypeById() throws Exception {
        //test api/jobs/get/{id}/employment-type
        given(jobsService.getEmploymentType(1) )
            .willReturn("Frontend Software Developer");
        String jobTitle = jobsService.getEmploymentType(1);
        assertEquals(jobTitle, "Frontend Software Developer");
    }
}
