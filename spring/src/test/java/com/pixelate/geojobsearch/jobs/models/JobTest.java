package com.pixelate.geojobsearch.jobs.models;

import com.pixelate.geojobsearch.models.Job;
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
    public void testSetIdOne(){
        //Arrange & Act
        tester.setJobid(1);
        Integer result = tester.getJobid();

        //Assert
        assertEquals(Integer.valueOf(1), result);
    }

    @Test
    public void testSetIdTwo(){
        //Arrange & Act
        tester.setJobid(50);
        Integer result = tester.getJobid();

        //Assert
        assertEquals(Integer.valueOf(50), result);
    }

    @Test
    public void testGetJobIdOne(){
        //Arrange
        tester.setJobid(24);

        //Act
        Integer result = tester.getJobid();

        //Assert
        assertEquals(Integer.valueOf(24), result);
    }

    @Test
    public void testGetJobIdTwo(){
        //Arrange
        tester.setJobid(67);

        //Act
        Integer result = tester.getJobid();

        //Assert
        assertEquals(Integer.valueOf(67), result);
    }

    @Test
    public void testSetJobTitleOne(){
        //Arrange & Act
        tester.setJob_title("Plumber");
        String result = tester.getJob_title();

        //Assert
        assertEquals("Plumber", result);
    }

    @Test
    public void testSetJobTitleTwo(){
        //Arrange & Act
        tester.setJob_title("Software Engineer");
        String result = tester.getJob_title();

        //Assert
        assertEquals("Software Engineer", result);
    }

    @Test
    public void testGetJobTitleOne(){
        //Arrange
        tester.setJob_title("Mechanic");

        //Act
        String result = tester.getJob_title();

        //Assert
        assertEquals("Mechanic", result);
    }

    @Test
    public void testGetJobTitleTwo(){
        //Arrange
        tester.setJob_title(" ");

        //Act
        String result = tester.getJob_title();

        //Assert
        assertEquals(" ", result);
    }

    @Test
    public void testSetJobLocationOne(){
        //Arrange & Act
        tester.setJob_location("Toronto, Ontario");
        String result = tester.getJob_location();

        //Assert
        assertEquals("Toronto, Ontario", result);
    }

    @Test
    public void testSetJobLocationTwo(){
        //Arrange & Act
        tester.setJob_location("Los Angeles, California, U.S.A.");
        String result = tester.getJob_location();

        //Assert
        assertEquals("Los Angeles, California, U.S.A.", result);
    }

    @Test
    public void testGetJobLocationOne(){
        //Arrange
        tester.setJob_location("Dubai, UAE");

        //Act
        String result = tester.getJob_location();

        //Assert
        assertEquals("Dubai, UAE", result);
    }

    @Test
    public void testGetJobLocationTwo(){
        //Arrange
        tester.setJob_location(" ");

        //Act
        String result = tester.getJob_location();

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

}