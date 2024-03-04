import scraper
import pytest
from unittest.mock import MagicMock


# testing getting the correct amount of job card
def testGetJobCardFromIndeed1():

    # job board 1 contains 15 jobs
    job_board_file_1 = open("testWebsite/indeed/indeedJobBoard1.txt", "r", encoding="utf8")
    listLength = scraper.get_job_cards_from_html(job_board_file_1.read(), "Indeed")
    job_board_file_1.close

    assert len(listLength) == 15

def testGetJobCardFromIndeed2():

    # job board 2 contains 5 jobs
    job_board_file_2 = open("testWebsite/indeed/indeedJobBoard2.txt", "r", encoding="utf8")
    listLength = scraper.get_job_cards_from_html(job_board_file_2.read(), "Indeed")
    job_board_file_2.close()

    assert len(listLength) == 5

def testGetJobCardFromIndeed3():

    # job board 3 contains 6 jobs
    job_board_file_3 = open("testWebsite/indeed/indeedJobBoard3.txt", "r", encoding="utf8")
    listLength = scraper.get_job_cards_from_html(job_board_file_3.read(), "Indeed")
    job_board_file_3.close()

    assert len(listLength) == 6


# test functionality on one job page
def testGetJobTitleFromIndeed1():
    job_file_1 = open("testWebsite/indeed/indeedJob1.txt", "r", encoding="utf8")

    title1 = scraper.get_job_attribute(job_file_1.read(), "job_title", "Indeed")
    job_file_1.close()
    assert title1 == "Cloud Solutions Engineer - .NET and Azure"

def testGetJobCompanyFromIndeed1():
    job_file_1 = open("testWebsite/indeed/indeedJob1.txt", "r", encoding="utf8")
    company1 = scraper.get_job_attribute(job_file_1.read(), "job_company", "Indeed")
    job_file_1.close()
    assert company1 == "Aviso Wealth"

def testGetJobLocationFromIndeed1():
    job_file_1 = open("testWebsite/indeed/indeedJob1.txt", "r", encoding="utf8")
    location1 = scraper.get_job_attribute(job_file_1.read(), "job_location", "Indeed")
    job_file_1.close()
    assert location1 == "151 Yonge Street, Toronto, ON"

def testGetJobEmploymentFromIndeed1():
    job_file_1 = open("testWebsite/indeed/indeedJob1.txt", "r", encoding="utf8")
    company1 = scraper.get_job_attribute(job_file_1.read(), "job_employment", "Indeed")
    job_file_1.close()
    assert company1 == "Full-time"

def testGetJobPayFromIndeed1():
    job_file_1 = open("testWebsite/indeed/indeedJob1.txt", "r", encoding="utf8")
    pay1 = scraper.get_job_attribute(job_file_1.read(), "job_pay", "Indeed")
    job_file_1.close()
    assert pay1 == "$105,000–$117,000 a year"



def testGetJobTitleFromIndeed2():
    job_file_2 = open("testWebsite/indeed/indeedJob2.txt", "r", encoding="utf8")

    title2 = scraper.get_job_attribute(job_file_2.read(), "job_title", "Indeed")
    job_file_2.close()
    assert title2 == "Junior Java Developer"

def testGetJobCompanyFromIndeed2():
    job_file_2 = open("testWebsite/indeed/indeedJob2.txt", "r", encoding="utf8")
    company2 = scraper.get_job_attribute(job_file_2.read(), "job_company", "Indeed")
    job_file_2.close()
    assert company2 == "Triunity Software"

def testGetJobLocationFromIndeed2():
    job_file_2 = open("testWebsite/indeed/indeedJob2.txt", "r", encoding="utf8")
    location2 = scraper.get_job_attribute(job_file_2.read(), "job_location", "Indeed")
    job_file_2.close()
    assert location2 == "Toronto, ON"

def testGetJobEmploymentFromIndeed2():
    job_file_2 = open("testWebsite/indeed/indeedJob2.txt", "r", encoding="utf8")
    company2 = scraper.get_job_attribute(job_file_2.read(), "job_employment", "Indeed")
    job_file_2.close()
    assert company2 == "Full-time"

def testGetJobPayFromIndeed2():
    job_file_2 = open("testWebsite/indeed/indeedJob2.txt", "r", encoding="utf8")
    pay2 = scraper.get_job_attribute(job_file_2.read(), "job_pay", "Indeed")
    job_file_2.close()
    assert pay2 == "$70,000 a year"



def testGetJobTitleFromIndeed3():
    job_file_3 = open("testWebsite/indeed/indeedJob3.txt", "r", encoding="utf8")

    title3 = scraper.get_job_attribute(job_file_3.read(), "job_title", "Indeed")
    job_file_3.close()
    assert title3 == "Senior Software Engineer | Python Developer"

def testGetJobCompanyFromIndeed3():
    job_file_3 = open("testWebsite/indeed/indeedJob3.txt", "r", encoding="utf8")
    company3 = scraper.get_job_attribute(job_file_3.read(), "job_company", "Indeed")
    job_file_3.close()
    assert company3 == "Scotiabank"

def testGetJobLocationFromIndeed3():
    job_file_3 = open("testWebsite/indeed/indeedJob3.txt", "r", encoding="utf8")
    location3 = scraper.get_job_attribute(job_file_3.read(), "job_location", "Indeed")
    job_file_3.close()
    assert location3 == "40 King Street West, Toronto, ON"

def testGetJobEmploymentFromIndeed3():
    job_file_3 = open("testWebsite/indeed/indeedJob3.txt", "r", encoding="utf8")
    company3 = scraper.get_job_attribute(job_file_3.read(), "job_employment", "Indeed")
    job_file_3.close()
    assert company3 == "Permanent"

def testGetJobPayFromIndeed3():
    job_file_3 = open("testWebsite/indeed/indeedJob3.txt", "r", encoding="utf8")
    pay3 = scraper.get_job_attribute(job_file_3.read(), "job_pay", "Indeed")
    job_file_3.close()
    assert pay3 == "Unknown"




def testGetJobCardFromCanadianJob():
    job_board_file_4 = open("testWebsite/canadian_job/canadianJobBank.txt", "r", encoding="utf8")
    listLength = scraper.get_job_cards_from_html(job_board_file_4.read(), "Canadian Job Bank")
    job_board_file_4.close()
    
    assert len(listLength) == 25


def testGetJobTitleFromCanadaJob():
    job_file_1 = open("testWebsite/canadian_job/CanadianJob1.txt", "r", encoding="utf8")

    title1 = scraper.get_job_attribute(job_file_1.read(), "job_title", "Canadian Job Bank")
    job_file_1.close()
    assert title1 == "software engineer"

def testGetJobCompanyFromCanadaJob():
    job_file_1 = open("testWebsite/canadian_job/CanadianJob1.txt", "r", encoding="utf8")
    company1 = scraper.get_job_attribute(job_file_1.read(), "job_company", "Canadian Job Bank")
    job_file_1.close()
    assert company1 == "Micharity Inc"

def testGetJobLocationFromCanadaJob():
    job_file_1 = open("testWebsite/canadian_job/CanadianJob1.txt", "r", encoding="utf8")
    location1 = scraper.get_job_attribute(job_file_1.read(), "job_location", "Canadian Job Bank")
    job_file_1.close()
    assert location1 == "Toronto, ON"

def testGetJobEmploymentFromCanadaJob():
    job_file_1 = open("testWebsite/canadian_job/CanadianJob1.txt", "r", encoding="utf8")
    company1 = scraper.get_job_attribute(job_file_1.read(), "job_employment", "Canadian Job Bank")
    job_file_1.close()
    assert company1 == "Permanent employmentFull time"

def testGetJobPayFromCanadaJob():
    job_file_1 = open("testWebsite/canadian_job/CanadianJob1.txt", "r", encoding="utf8")
    pay1 = scraper.get_job_attribute(job_file_1.read(), "job_pay", "Canadian Job Bank")
    job_file_1.close()
    assert pay1 == "$52.88HOUR hourly /   40 hours per week"

def testGetWebDriver():
    assert scraper.get_firefox_driver() != None


def testGetJobJson():
    job_file = open("testWebsite/canadian_job/CanadianJob1.txt", "r", encoding="utf8")
    expected_json = {"title": "software engineer", "company": "Micharity Inc", "location": "Toronto, ON", "employment_type": "Permanent employmentFull time", "salary": "$52.88HOUR hourly /   40 hours per week"}
    job_json = scraper.get_job_json(job_file.read(), "Canadian Job Bank")
    
    assert expected_json["title"] == job_json["title"]
    assert expected_json["company"] == job_json["company"]
    assert expected_json["location"] == job_json["location"]
    assert expected_json["employment_type"] == job_json["employment_type"]
    assert expected_json["salary"] == job_json["salary"]

def testDatabase():
    connection = MagicMock()
    job_file = open("testWebsite/canadian_job/CanadianJob1.txt", "r", encoding="utf8")
    job_json = scraper.get_job_json(job_file.read(), "Canadian Job Bank")
    job_title = job_json["title"]
    job_location = job_json["location"]
    salary = job_json.get("salary", "Negotiable")
    job_description = job_json.get("description", "No description given")
    company = job_json["company"]
    
    cursor = connection.cursor.return_value
    insert_statement = """
                        INSERT INTO job (jobid, job_title, job_location, salary, job_description, company)
                        VALUES (NULL, ?, ?, ?, ?, ?);
                        """
    cursor.execute(insert_statement, (job_title, job_location, salary, job_description, company))
    cursor.execute.assert_called_once_with(insert_statement, (job_title, job_location, salary, job_description, company))
