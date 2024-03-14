def parse_salary(salary: str) -> float:
    salary = salary.replace(",", "")

    keywords = ["year", "annual", "annum"]

    index = salary.find("$") + 1

    num = 0.0

    while(salary[index].isnumeric()):
        num = num * 10 + int(salary[index]); index += 1

    if(salary[index] == "."):
        index += 1
        while(salary[index].isnumeric()):
            num += int(salary[index]) * (10 ** (-1 * (index - salary.find(".")))); index += 1
    
    for i in keywords:
        if i in salary.lower():
            num = num / 2080.0
    
    return round(num, 2)

tests = [
    "$43.00HOUR hourly / 30 hours per week",
    "$43.69 to $45.69HOUR hourly (To be negotiated) / 35 to 40 hours per week",
    "TESTING $25 an hour",
    "$50,000 per annum",
    "$60,000 annual salary",
    "$70,000 per year",
    "$30.00 per hour",
    "$65,000 yearly"
]

for salary in tests:
    print("Original:", salary)
    parsed_salary = parse_salary(salary)
    print("Parsed:", parsed_salary)

    print()
