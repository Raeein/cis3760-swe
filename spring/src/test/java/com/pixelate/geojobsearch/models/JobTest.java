package com.pixelate.geojobsearch.models;

import org.springframework.boot.test.context.SpringBootTest;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.BeforeEach;

import static org.junit.jupiter.api.Assertions.assertEquals;

@SpringBootTest
public class JobTest {

    private Job tester;
    @BeforeEach
    public void setUp() {
        tester = new Job();
    }

    @Test
    public void testAllArgsConstructor() {
        Job job = new Job(1,
                "Software Engineer",
                "San Francisco, CA",
                "$120,000",
                "Develop cutting-edge software solutions.",
                "Tech Innovations Inc.",
                "Full-time");

        // Validate that each field is correctly initialized
        assertEquals(Integer.valueOf(1), job.getJobId(), "Job ID should be initialized correctly");
        assertEquals("Software Engineer", job.getJobTitle(), "Job title should be initialized correctly");
        assertEquals("San Francisco, CA", job.getJobLocation(), "Job location should be initialized correctly");
        assertEquals("$120,000", job.getSalary(), "Salary should be initialized correctly");
        assertEquals("Develop cutting-edge software solutions.", job.getJobDescription(), "Job description should be initialized correctly");
        assertEquals("Tech Innovations Inc.", job.getCompany(), "Company should be initialized correctly");
        assertEquals("Full-time", job.getEmploymentType(), "Employment type should be initialized correctly");
    }



    @Test
    public void testSetIdOne(){
        //Arrange & Act
        tester.setJobId(1);
        Integer result = tester.getJobId();

        //Assert
        assertEquals(Integer.valueOf(1), result);
    }

    @Test
    public void testSetIdTwo(){
        //Arrange & Act
        tester.setJobId(50);
        Integer result = tester.getJobId();

        //Assert
        assertEquals(Integer.valueOf(50), result);
    }

    @Test
    public void testGetJobIdOne(){
        //Arrange
        tester.setJobId(24);

        //Act
        Integer result = tester.getJobId();

        //Assert
        assertEquals(Integer.valueOf(24), result);
    }

    @Test
    public void testGetJobIdTwo(){
        //Arrange
        tester.setJobId(67);

        //Act
        Integer result = tester.getJobId();

        //Assert
        assertEquals(Integer.valueOf(67), result);
    }

    @Test
    public void testSetJobTitleOne(){
        //Arrange & Act
        tester.setJobTitle("Plumber");
        String result = tester.getJobTitle();

        //Assert
        assertEquals("Plumber", result);
    }

    @Test
    public void testSetJobTitleTwo(){
        //Arrange & Act
        tester.setJobTitle("Software Engineer");
        String result = tester.getJobTitle();

        //Assert
        assertEquals("Software Engineer", result);
    }

    @Test
    public void testGetJobTitleOne(){
        //Arrange
        tester.setJobTitle("Mechanic");

        //Act
        String result = tester.getJobTitle();

        //Assert
        assertEquals("Mechanic", result);
    }

    @Test
    public void testGetJobTitleTwo(){
        //Arrange
        tester.setJobTitle(" ");

        //Act
        String result = tester.getJobTitle();

        //Assert
        assertEquals(" ", result);
    }

    @Test
    public void testSetJobLocationOne(){
        //Arrange & Act
        tester.setJobLocation("Toronto, Ontario");
        String result = tester.getJobLocation();

        //Assert
        assertEquals("Toronto, Ontario", result);
    }

    @Test
    public void testSetJobLocationTwo(){
        //Arrange & Act
        tester.setJobLocation("Los Angeles, California, U.S.A.");
        String result = tester.getJobLocation();

        //Assert
        assertEquals("Los Angeles, California, U.S.A.", result);
    }

    @Test
    public void testGetJobLocationOne(){
        //Arrange
        tester.setJobLocation("Dubai, UAE");

        //Act
        String result = tester.getJobLocation();

        //Assert
        assertEquals("Dubai, UAE", result);
    }

    @Test
    public void testGetJobLocationTwo(){
        //Arrange
        tester.setJobLocation(" ");

        //Act
        String result = tester.getJobLocation();

        //Assert
        assertEquals(" ", result);
    }

    @Test
    public void testSetSalaryOne(){
        //Arrange & Act
        tester.setSalary("Negotiable");
        String result = tester.getSalary();

        //Assert
        assertEquals("Negotiable", result);
    }

    @Test
    public void testSetSalaryTwo(){
        //Arrange & Act
        tester.setSalary("$120,000");
        String result = tester.getSalary();

        //Assert
        assertEquals("$120,000", result);
    }

    @Test
    public void testGetSalaryOne(){
        //Arrange
        tester.setSalary("$85,000");

        //Act
        String result = tester.getSalary();

        //Assert
        assertEquals("$85,000", result);
    }

    @Test
    public void testGetSalaryTwo(){
        //Arrange
        tester.setSalary(" ");

        //Act
        String result = tester.getSalary();

        //Assert
        assertEquals(" ", result);
    }

    @Test
    public void testSetJobDescriptionOne(){
        //Arrange & Act
        tester.setJobDescription("Come join our security team at Vtech!");
        String result = tester.getJobDescription();

        //Assert
        assertEquals("Come join our security team at Vtech!", result);
    }

    @Test
    public void testSetJobDescriptionTwo(){
        //Arrange & Act
        tester.setJobDescription("We're looking for passionate game developers");
        String result = tester.getJobDescription();

        //Assert
        assertEquals("We're looking for passionate game developers", result);
    }

    @Test
    public void testGetJobDescriptionOne(){
        //Arrange
        tester.setJobDescription("Join our team as a Software Developer");

        //Act
        String result = tester.getJobDescription();

        //Assert
        assertEquals("Join our team as a Software Developer", result);
    }

    @Test
    public void testGetJobDescriptionTwo(){
        //Arrange
        tester.setJobDescription(" ");

        //Act
        String result = tester.getJobDescription();

        //Assert
        assertEquals(" ", result);
    }

    @Test
    public void testSetCompanyOne(){
         //Arrange & Act
        tester.setCompany("Google");
        String result = tester.getCompany();

        //Assert
        assertEquals("Google", result);
    }

    @Test
    public void testSetCompanyTwo(){
         //Arrange & Act
        tester.setCompany("Dell Technologies Inc.");
        String result = tester.getCompany();

        //Assert
        assertEquals("Dell Technologies Inc.", result);
    }

    @Test
    public void testGetCompanyOne(){
        //Arrange
        tester.setCompany("Facebook");

        //Act
        String result = tester.getCompany();

        //Assert
        assertEquals("Facebook", result);
    }

    @Test
    public void testGetCompanyTwo(){
        //Arrange
        tester.setCompany(" ");

        //Act
        String result = tester.getCompany();

        //Assert
        assertEquals(" ", result);
    }

    @Test
    public void testSetEmploymentTypeOne(){
         //Arrange & Act
        tester.setEmploymentType("Full time");
        String result = tester.getEmploymentType();

        //Assert
        assertEquals("Full time", result);
    }

    @Test
    public void testSetEmploymentTypeTwo(){
         //Arrange & Act
        tester.setEmploymentType("Part time");
        String result = tester.getEmploymentType();

        //Assert
        assertEquals("Part time", result);
    }

    @Test
    public void testEmploymentTypeOne(){
        //Arrange
        tester.setEmploymentType("Internship / Co-op");

        //Act
        String result = tester.getEmploymentType();

        //Assert
        assertEquals("Internship / Co-op", result);
    }

    @Test
    public void testEmploymentTypeTwo(){
        //Arrange
        tester.setEmploymentType(" ");

        //Act
        String result = tester.getEmploymentType();

        //Assert
        assertEquals(" ", result);
    }
}