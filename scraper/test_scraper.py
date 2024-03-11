import scraper
import pytest
from unittest.mock import MagicMock


@pytest.fixture
def mock_connection():
    connection = MagicMock()
    cursor = connection.cursor
    return connection, cursor



@pytest.mark.parametrize("file_location, job_board, length", [
    ("testWebsite/indeed/indeedJobBoard1.txt", "Indeed", 15),
    ("testWebsite/indeed/indeedJobBoard2.txt", "Indeed", 5),
    ("testWebsite/indeed/indeedJobBoard3.txt", "Indeed", 6),
    ("testWebsite/canadian_job/canadianJobBank.txt", "Canadian Job Bank", 25)
])
def testGetJobCardFromIndeed1(file_location:str, job_board:str, length:int):

    job_board_file_1 = open(file_location, "r", encoding="utf8")
    job_cards = scraper.get_job_cards_from_html(job_board_file_1.read(), job_board)
    job_board_file_1.close
    assert len(job_cards) == length



@pytest.mark.parametrize("file_location, job_board, title, company, location, employment_type, salary", [
    (
        "testWebsite/indeed/indeedJob1.txt", "Indeed", "Cloud Solutions Engineer - .NET and Azure", 
        "Aviso Wealth", "151 Yonge Street, Toronto, ON", "Full Time", "$105,000–$117,000 a year"
    ),
    (
        "testWebsite/indeed/indeedJob2.txt", "Indeed", "Junior Java Developer", 
        "Triunity Software", "Toronto, ON", "Full Time", "$70,000 a year"
    ),
    (
        "testWebsite/indeed/indeedJob3.txt", "Indeed", "Senior Software Engineer | Python Developer",
        "Scotiabank", "40 King Street West, Toronto, ON", "Permanent", "Unknown"
    ),
    (
        "testWebsite/canadian_job/CanadianJob1.txt", "Canadian Job Bank", "software engineer",
        "Micharity Inc", "Toronto, ON", "Full Time,Permanent", "$52.88HOUR hourly /   40 hours per week"
    )
])
def test_get_and_insert_job_data(file_location:str, job_board:str, title:str, company:str, location:str, employment_type:str, salary:str, mock_connection):
    connection, cursor = mock_connection
    insert_statement = """INSERT INTO job (jobid, job_title, job_location, salary, job_description, company, employment_type)VALUES (NULL, ?, ?, ?, ?, ?, ?);"""
    job_file = open(file_location, "r", encoding="utf8")
    job_json = scraper.get_job_json(job_file.read(), job_board, "https://dummy.url" )
    job_file.close()

    assert job_json["title"] == title
    assert job_json["company"] == company
    assert job_json["location"] == location
    assert job_json["employment_type"] == employment_type
    assert job_json["salary"] == salary

    res = scraper.insert_into_database(job_json, connection, cursor)
    assert res == 1
    cursor.execute.assert_called_with(insert_statement, (job_json["title"], job_json["location"], job_json["salary"], job_json["description"], job_json["company"], job_json["employment_type"]))
    


def testGetWebDriver():
    driver = scraper.get_firefox_driver()
    assert  driver != None
    scraper.stall_driver(driver)
    assert True


def testLoadTargetedJobBoard():
    targeted_job_board = scraper.load_targeted_job_board()
    assert targeted_job_board == ["Indeed", "Canadian Job Bank"]

    targeted_job_board = scraper.load_targeted_job_board(["Canadian Job Bank",])
    assert targeted_job_board == ["Canadian Job Bank",]

    targeted_job_board = scraper.load_targeted_job_board(["Indeed", ])
    assert targeted_job_board == ["Indeed", ]

def testGetJobBoardSearchUrl():
    url = scraper.get_job_board_search_url("Software Engineer", "Toronto", "Indeed")
    assert url != None

def testGetIndeedJobUrl():
    job_board_file_1 = open("testWebsite/indeed/indeedJobBoard1.txt", "r", encoding="utf8")
    jobCards = scraper.get_job_cards_from_html(job_board_file_1.read(), "Indeed")

    assert scraper.get_job_url("Indeed", jobCards[0]) == "https://ca.indeed.com/pagead/clk?mo=r&ad=-6NYlbfkN0DFRBgdkffDjRejVobbg8KVPSs6CgnXSfnYo3Qc-NFE2L-XKvK7g0tzAN47iE-7-6GDlOe0HPUmlFwR_W5ypPuLTdyMgC2RALOPVZz4DDdOBNFIt6a4mgwlZBRnyzfg1y22jsSY3BTy8gBYMrrjaAotockQpKfUEP2-fkF0cY_Qbc-2_hO1lIyEhDClCVFXclvMoxn0eihqFz_WUQyHnV4A0pD-MXULJUp0nmRFoj2TmngceU0STyyjbx-Ki7kwUBiFaddQ1efAo7w2jk_98bO3yOTZE-zRDilOMXBlAm5SdL99COtUackXtvf9t_d0YO7r1dlp6jrJ65sU7TFY0r49PD3wYx0KhylThzOL9qqLHjvjM9hK2NBJJFrQDHsmzjGGmmUu5bREDSz2YkrLYYDg3zg-zTPcRyiycGMbZSNVe2tCUDyMSOAxB10mBuUQAtInt-9arhdbPO4Sgww2UqF3gz75EvPTnoZ-FEoAqGCGRltr7krCOf3NPrPgAAqSpj3163jqQJPd0ZBFK_9_kZuPPiDiZKAo-otjUX09Q7Lh11zlwHKh6t4lCGj-I_xFsflBfzYqOVH4SG1odvB72bgzIw9E7ygRqb2IOpcuiddBpzIZCg8XWmqCEq9h6H2KxtrPlOJSPaQ93sIz3Zp3kPbOKZzcZ_zEba7wSZIYRBt0ww==&xkcb=SoDW6_M3EPWoaZWQx50LbzkdCdPP&camk=4HOcmqOLYrCLTJoowOo4eQ==&p=0&fvj=1&vjs=3"

def testGetCanadianJobUrl():
    job_board_file_4 = open("testWebsite/canadian_job/canadianJobBank.txt", "r", encoding="utf8")
    jobCards = scraper.get_job_cards_from_html(job_board_file_4.read(), "Canadian Job Bank")

    assert scraper.get_job_url("Canadian Job Bank", jobCards[0]) == "https://www.jobbank.gc.ca/jobsearch/jobposting/40322760;jsessionid=1B78D6117D1291E6CA832BF65BFBD84E.jobsearch74?source=searchresults"

