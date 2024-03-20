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

    // @Test
    // public void testJobPostingsExist() throws SQLException {
    //     try (Connection connection = DriverManager.getConnection("jdbc:mysql://mysql:3306/geo_job_search_db",
    //             "root", "pwd");
    //             Statement statement = connection.createStatement()
    //     ){
    //         ResultSet resultSet = statement.executeQuery("SELECT COUNT(*) FROM job");
    //         resultSet.next();
            
    //         int count = resultSet.getInt(1);
    //         assertEquals(9, count, "Expected 11 job postings in the database");
    //     }
    // }




    // @Test
    // public void testGetAllJob() throws Exception {
    //     given(jobsService.countJobs()).willReturn(9);

    //     int numJobs = jobsService.countJobs();
    //     assertEquals(9, numJobs);
    // }


    // @Test
    // public void testSearchJob() throws Exception {

    //     Job job = new Job(1, 
    //     "Frontend Software Developer", 
    //     "Toronto, ON", 
    //     "$89,000", 
    //     "Knowledge with developing using React and TypeScript",
    //     "DataCat", 
    //     "Full Time,Permament"
    //     );

    //     when(jobsService.searchJobs("Frontend Software Developer")).thenReturn(Arrays.asList(job));

    //     Iterable<Job> jobs = jobsService.searchJobs("Frontend Software Developer");
    //     int len = 0;
    //     System.out.print("Job: ");
    //     System.out.println(jobs);
    //     for (Job job : jobs) len++;
    //     assertEquals(3, len);
    // }

    // @Test
    // public void testFilterEmployment() throws Exception {
    //     Iterable<Job> jobs = jobsService.filterEmploymentType("Full time");
    //     int len = 0;
    //     System.out.print("Job: ");
    //     System.out.println(jobs);
    //     for (Job job : jobs) {
    //         len++;
    //     }
    //     assertEquals(7, len);
    // }

    // @Test
    // public void testFilterLocatiion() throws Exception {
    //     Iterable<Job> jobs = jobsService.filterLocation("Kitchener, ON");
    //     int len = 0;
    //     System.out.print("Job: ");
    //     System.out.println(jobs);
    //     for (Job job : jobs) len++;
    //     assertEquals(1, len);
    // }

}
