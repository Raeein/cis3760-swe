from bs4 import BeautifulSoup


insert_statement = """
    INSERT INTO job (
        jobid, job_title, job_location,
        salary, job_description, company, employment_type
    )
    VALUES (NULL, ?, ?, ?, ?, ?, ?);
"""

job_board_objects = {
    "Indeed": {
        "base_url": "https://ca.indeed.com",
        "search_url": """
                        https://ca.indeed.com/jobs?
                        q={job_title}&l={location}&sort=date
                    """.replace("\n", "").replace(" ", ""),

        "card_element": "div",
        "card_class": "job_seen_beacon",

        # job page attribute start
        # string parse will be parsing beginning and end of string.
        # Positive will remove character from beginning,
        # negative remove character from end
        "title_element": "h1",
        "title_search_object": {"class": "jobsearch-JobInfoHeader-title"},

        "company_element": "div",
        "company_search_object": {"data-company-name": "true"},

        "location_element": "div",
        "location_search_object": {
            "data-testid": "inlineHeader-companyLocation"
        },

        "employment_type_element": "div",
        "employment_type_search_object": {"aria-label": "Job type"},
        "employment_type_string_parse": 8,

        "salary_element": "div",
        "salary_search_object": {"aria-label": "Pay"},
        "salary_string_parse": 3,

        "description_element": "div",
        "description_search_object": {"id": "jobDescriptionText"},
        # job page attribute ends
    },
    "Canadian Job Bank": {
        "base_url": "https://www.jobbank.gc.ca",
        "search_url": """
                        https://www.jobbank.gc.ca/jobsearch/jobsearch?
                        searchstring={job_title}&locationstring={location}
                        &sort=D
                    """.replace("\n", "").replace(" ", ""),

        "card_element": "a",
        "card_class": "resultJobItem",

        "title_element": "span",
        "title_search_object": {"property": "title"},

        "company_element": "span",
        "company_search_object": {"property": "hiringOrganization"},

        "location_element": "span",
        "location_search_object": {"property": "address"},

        "employment_type_element": "span",
        "employment_type_search_object": {"property": "employmentType"},

        "salary_element": "span",
        "salary_search_object": {"property": "baseSalary"},

        "description_element": "div",
        "description_search_object": {"id": "comparisonchart"},
    }
}


def get_job_cards_from_html(html_string: str, job_board_name: str):
    job_cards = []

    soup = BeautifulSoup(html_string, "html.parser")

    job_board_object = job_board_objects[job_board_name]

    job_cards = soup.find_all(
        job_board_object["card_element"],
        class_=job_board_object["card_class"]
    )

    for i in range(len(job_cards)):
        job_cards[i] = "<div>" + str(job_cards[i]) + "</div>"
        job_cards[i] = BeautifulSoup(job_cards[i], "html.parser")

    return job_cards


def get_job_attribute(
        html_string: str,
        attr: str,
        job_board_name: str
) -> str:
    job_soup = BeautifulSoup(html_string, "html.parser")

    try:
        data = job_soup.find(
            job_board_objects[job_board_name][attr + "_element"],
            job_board_objects[job_board_name][attr + "_search_object"]
        ).text
        if (attr + "_string_parse" in job_board_objects[job_board_name]):
            data = data[
                   job_board_objects[job_board_name][attr + "_string_parse"]:
                   ]

    except Exception:
        data = "Unknown"

    return data.strip()


def get_job_json(page_source: str, job_board_name: str, job_url: str) -> dict:
    job_json_object = {}
    job_json_object["title"] = get_job_attribute(
        page_source, "title", job_board_name
    )
    job_json_object["company"] = get_job_attribute(
        page_source, "company", job_board_name
    )
    job_json_object["location"] = get_job_attribute(
        page_source, "location", job_board_name
    )
    job_json_object["employment_type"] = parse_employment_type(
        get_job_attribute(page_source, "employment_type", job_board_name)
    )
    job_json_object["salary"] = parse_salary(
        get_job_attribute(page_source, "salary", job_board_name)
    )
    job_json_object["description"] = get_job_attribute(
        page_source, "description", job_board_name
    )
    job_json_object["url"] = job_url
    return job_json_object


def load_targeted_job_board(specified_job_boards: list[str] = []):
    job_board_search_list = []
    if (specified_job_boards == []):
        job_board_search_list = list(job_board_objects.keys())
    else:
        for i in specified_job_boards:
            if i in list(job_board_objects.keys()):
                job_board_search_list.append(i)
    return job_board_search_list


def get_search_url(
        job_title: str,
        location: str,
        job_board_name: str
) -> str:
    url = job_board_objects[job_board_name]["search_url"].format(
        job_title=job_title, location=location
    )
    return url


def get_job_url(job_board_name: str, job_card: str) -> str:
    url = job_board_objects[job_board_name]["base_url"]
    url += job_card.find('a')['href']
    return url


def parse_salary(salary: str) -> str:
    salary = salary.replace(",", "")
    year_keywords = ["year", "annual", "annum"]
    index = salary.find("$") + 1

    num = 0.0

    if (index == 0):
        return "Salary not given"

    while (salary[index].isnumeric()):
        num = num * 10 + int(salary[index])
        index += 1
        if (salary[index] == ","):
            index += 1

    if (salary[index] == "."):
        index += 1
        while (salary[index].isnumeric()):
            num += int(salary[index]) * (10 ** (-1 * (index - salary.find("."))))
            index += 1

    if ("day" in salary.lower()):
        num = num / 8

    for i in year_keywords:
        if i in salary.lower():
            num = num / 2080.0
            break

    return str("$" + format(round(num, 2), '.2f'))


def parse_employment_type(employment_type: str) -> str:
    employment_types = [
        "Full Time", "Part Time", "Permanent",
        "Temporary", "Contract", "Internship"
    ]
    employment_data = []

    for i in employment_types:
        if i.lower() in employment_type.replace("-", " ").lower():
            employment_data.append(i)

    return ",".join(tuple(employment_data)) if employment_data else employment_type


def insert_into_database(job_object: dict, connection, cursor):
    job_title = job_object["title"]
    job_location = job_object["location"]
    salary = job_object.get("salary", "Negotiable")
    job_description = job_object.get("description", "No description given")
    company = job_object["company"]
    employment_type = job_object["employment_type"]

    if (job_title != "Unknown"):
        get_statemet = f"""SELECT job_description FROM job
                            WHERE job_title = '{job_title}'
                            AND salary = '{salary}'
                            AND company = '{company}'
                            AND employment_type = '{employment_type}';
                        """
        cursor.execute(get_statemet)

        duplicate = False

        for i in cursor.fetchall():
            if (i[0] == job_description):
                duplicate = True
                break

        if (not duplicate):
            res = cursor.execute(insert_statement, (
                job_title, job_location, salary,
                job_description, company, employment_type
            ))
            if res == 0:
                print(
                    "Error inserting data: ", job_title, job_location,
                    salary, job_description, company, employment_type
                )
                return 0
        else:
            return -1
        connection.commit()
    return 1
