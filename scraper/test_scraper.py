import scraper
import pytest
from unittest.mock import MagicMock


insert_statement = """
    INSERT INTO job (
        jobid, job_title, job_location,
        salary, job_description, company, employment_type
    )
    VALUES (NULL, ?, ?, ?, ?, ?, ?);
"""


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
def test_get_job_card(file_location: str, job_board: str, length: int):
    job_board_file_1 = open(file_location, "r", encoding="utf8")
    job_cards = scraper.get_job_cards_from_html(
        job_board_file_1.read(), job_board
    )
    job_board_file_1.close
    assert len(job_cards) == length


@pytest.mark.parametrize(
    """file_location, job_board, title, company,
    location, employment_type, salary""", [
        (
                "testWebsite/indeed/indeedJob1.txt", "Indeed",
                "Cloud Solutions Engineer - .NET and Azure",
                "Aviso Wealth", "151 Yonge Street, Toronto, ON",
                "Full Time", "$105,000–$117,000 a year"
        ),
        (
                "testWebsite/indeed/indeedJob2.txt", "Indeed",
                "Junior Java Developer",
                "Triunity Software", "Toronto, ON",
                "Full Time", "$70,000 a year"
        ),
        (
                "testWebsite/indeed/indeedJob3.txt", "Indeed",
                "Senior Software Engineer | Python Developer",
                "Scotiabank", "40 King Street West, Toronto, ON",
                "Permanent", "Unknown"
        ),
        (
                "testWebsite/canadian_job/CanadianJob1.txt", "Canadian Job Bank",
                "software engineer",
                "Micharity Inc", "Toronto, ON",
                "Full Time,Permanent", "$52.88HOUR hourly /   40 hours per week"
        )
    ]
)
def test_get_and_insert_job_data(
        file_location: str, job_board: str, title: str, company: str,
        location: str, employment_type: str, salary: str, mock_connection
):
    connection, cursor = mock_connection
    insert_statement = scraper.insert_statement
    job_file = open(file_location, "r", encoding="utf8")
    job_json = scraper.get_job_json(
        job_file.read(), job_board, "https://dummy.url"
    )
    job_file.close()

    assert job_json["title"] != title
    assert job_json["company"] == company
    assert job_json["location"] == location
    assert job_json["employment_type"] == employment_type
    assert job_json["salary"] == salary

    res = scraper.insert_into_database(job_json, connection, cursor)
    assert res == 1
    cursor.execute.assert_called_with(insert_statement, (
        job_json["title"], job_json["location"],
        job_json["salary"], job_json["description"],
        job_json["company"], job_json["employment_type"]
    ))


def test_load_targeted_job_board():
    targeted_job_board = scraper.load_targeted_job_board()
    assert targeted_job_board == ["Indeed", "Canadian Job Bank"]

    targeted_job_board = scraper.load_targeted_job_board(
        ["Canadian Job Bank",]
    )
    assert targeted_job_board == ["Canadian Job Bank",]

    targeted_job_board = scraper.load_targeted_job_board(["Indeed", ])
    assert targeted_job_board == ["Indeed", ]


def test_get_job_board_search_url():
    url = scraper.get_search_url(
        "Engineer", "Toronto", "Indeed"
    )
    assert url == "https://ca.indeed.com/jobs?q=Engineer&l=Toronto&sort=date"
    url = scraper.get_search_url(
        "Engineer", "Toronto", "Canadian Job Bank"
    )
    assert url == """
                        https://www.jobbank.gc.ca/jobsearch/jobsearch?
                        searchstring=Engineer&locationstring=Toronto&sort=D
                """.replace("\n", "").replace(" ", "")


def test_get_indeed_job_url():
    job_board_file_1 = open(
        "testWebsite/indeed/indeedJobBoard1.txt", "r", encoding="utf8"
    )
    jobCards = scraper.get_job_cards_from_html(
        job_board_file_1.read(), "Indeed"
    )
    indeed_link = """
                    https://ca.indeed.com/pagead/clk
                    ?mo=r&ad=-6NYlbfkN0DFRBgdkffDjRejVobbg8KVPSs6CgnXSfnYo3Qc-
                    NFE2L-XKvK7g0tzAN47iE-7-6GDlOe0HPUmlFwR_W5ypPuLTdyMgC2RALO
                    PVZz4DDdOBNFIt6a4mgwlZBRnyzfg1y22jsSY3BTy8gBYMrrjaAotockQp
                    KfUEP2-fkF0cY_Qbc-2_hO1lIyEhDClCVFXclvMoxn0eihqFz_WUQyHnV4
                    A0pD-MXULJUp0nmRFoj2TmngceU0STyyjbx-Ki7kwUBiFaddQ1efAo7w2j
                    k_98bO3yOTZE-zRDilOMXBlAm5SdL99COtUackXtvf9t_d0YO7r1dlp6jr
                    J65sU7TFY0r49PD3wYx0KhylThzOL9qqLHjvjM9hK2NBJJFrQDHsmzjGGm
                    mUu5bREDSz2YkrLYYDg3zg-zTPcRyiycGMbZSNVe2tCUDyMSOAxB10mBuU
                    QAtInt-9arhdbPO4Sgww2UqF3gz75EvPTnoZ-FEoAqGCGRltr7krCOf3NP
                    rPgAAqSpj3163jqQJPd0ZBFK_9_kZuPPiDiZKAo-otjUX09Q7Lh11zlwHK
                    h6t4lCGj-I_xFsflBfzYqOVH4SG1odvB72bgzIw9E7ygRqb2IOpcuiddBp
                    zIZCg8XWmqCEq9h6H2KxtrPlOJSPaQ93sIz3Zp3kPbOKZzcZ_zEba7wSZI
                    YRBt0ww==&xkcb=SoDW6_M3EPWoaZWQx50LbzkdCdPP&camk=4HOcmqOLY
                    rCLTJoowOo4eQ==&p=0&fvj=1&vjs=3
                """.replace("\n", "").replace(" ", "")

    assert scraper.get_job_url("Indeed", jobCards[0]) == indeed_link


def test_get_canadian_job_url():
    job_board_file_4 = open(
        "testWebsite/canadian_job/canadianJobBank.txt", "r", encoding="utf8"
    )
    jobCards = scraper.get_job_cards_from_html(
        job_board_file_4.read(), "Canadian Job Bank"
    )

    canadian_job_link = """
                            https://www.jobbank.gc.ca/jobsearch/jobposting/
                            40322760;jsessionid=1B78D6117D1291E6CA832BF65BFB
                            D84E.jobsearch74?source=searchresults
                        """.replace("\n", "").replace(" ", "")

    assert scraper.get_job_url(
        "Canadian Job Bank", jobCards[0]
    ) == canadian_job_link
