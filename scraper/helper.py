# Converts varying employment type strings into 3 groups by searching for key words
def formatEmploymentType(employment_type):
    if "Full-time" in employment_type:
        employment_type = "Full time"
    elif "Part-time" in employment_type:
        employment_type = "Part time"
    elif "Internship / Co-op" in employment_type:
        employment_type = "Internship / Co-op"
    else:
        employment_type = "Unknown"

    return employment_type