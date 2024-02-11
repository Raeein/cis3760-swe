package com.pixelate.geojobsearch.jobs.models;

import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.assertEquals;


public class JobTest {
    
    private Job tester;

    @Before
    public void setup() {
        tester = new Job();
    }

    @Test
    public void testSetIdOne(){
        //Arrange & Act
        tester.setId(1);
        Integer result = tester.getJobId();

        //Assert
        assertEquals(1, result);
    }

    @Test
    public void testSetIdTwo(){
        //Arrange & Act
        tester.setId(50);
        Integer result = tester.getJobId();

        //Assert
        assertEquals(50, result);
    }

    @Test
    public void testGetJobIdOne(){
        //Arrange
        tester.setId(24);

        //Act
        Integer result = tester.getJobId();

        //Assert
        assertEquals(24, result);
    }

    @Test
    public void testGetJobIdTwo(){
        //Arrange
        tester.setId(67);

        //Act
        Integer result = tester.getJobId();

        //Assert
        assertEquals(67, result);
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

}