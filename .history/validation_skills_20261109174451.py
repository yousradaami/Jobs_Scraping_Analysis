import pandas as pd
import re

# ==========================================
# 1. LOAD DATASET
# ==========================================

df = pd.read_csv("jobs_informatique.csv")

print("Initial number of jobs:", len(df))

# Check required columns
required_columns = ["Job_Title", "Categories", "Description"]

for col in required_columns:
    if col not in df.columns:
        df[col] = ""

for col in required_columns:
    df[col] = df[col].fillna("").astype(str)

# Prepare text
df["Analysis_Text"] = (
    df["Job_Title"] + " " +
    df["Categories"] + " " +
    df["Description"]
).str.lower()


# ==========================================
# 2. IT RELEVANCE VALIDATION
# ==========================================

strong_it_patterns = [
    r"software engineer",
    r"software developer",
    r"backend engineer",
    r"backend developer",
    r"frontend engineer",
    r"frontend developer",
    r"web developer",
    r"website developer",
    r"full.?stack developer",
    r"programmer",
    r"golang engineer",
    r"golang developer",
    r"kubernetes engineer",
    r"it systems engineer",
    r"systems engineer",
    r"system administrator",
    r"network engineer",
    r"solutions architect",
    r"help desk",
    r"it support",
    r"wordpress developer",
    r"joomla developer",
    r"salesforce developer",
    r"dynamics 365.*developer",
    r"portal developer",
    r"commerce cloud developer",
    r"devops engineer",
    r"cloud engineer",
    r"data engineer",
    r"data scientist",
    r"cybersecurity engineer",
    r"mobile developer",
    r"database administrator"
]

review_patterns = [
    r"security sales",
    r"sales specialist",
    r"risk analyst",
    r"customer support",
    r"content developer"
]

it_keywords = [
    "software", "developer", "programmer", "programming",
    "web development", "frontend", "front-end", "backend",
    "back-end", "full stack", "full-stack",
    "computer science", "information technology",
    "IT support", "system administrator", "network engineer",
    "cybersecurity", "data analyst", "data scientist",
    "cloud engineer", "devops", "database",
    "mobile developer", "machine learning",
    "python", "javascript", "typescript", "java",
    "react", "angular", "node.js", "sql",
    "docker", "kubernetes", "linux", "aws", "azure",
    "golang", "wordpress", "salesforce"
]


def validate_it(row):

    title = row["Job_Title"].lower()
    text = row["Analysis_Text"]

    # Ambiguous job titles need manual review
    for pattern in review_patterns:
        if re.search(pattern, title):
            return "Needs review", "Ambiguous job title"

    # Clearly IT-related titles
    for pattern in strong_it_patterns:
        if re.search(pattern, title):
            return "Relevant", "Clear IT-related job title"

    # Check technical keywords in the full text
    matches = [word for word in it_keywords if word in text]

    if len(matches) >= 2:
        return "Relevant", "Multiple IT-related keywords found"

    return "Needs review", "Manual review required"


results = df.apply(validate_it, axis=1)

df["IT_Relevance"] = results.apply(lambda x: x[0])
df["Relevance_Reason"] = results.apply(lambda x: x[1])


# ==========================================
# 3. SKILLS EXTRACTION
# ==========================================

skills = [
    "Python", "Java", "JavaScript", "TypeScript",
    "C++", "C#", "PHP", "SQL",
    "PostgreSQL", "MySQL", "MongoDB",
    "React", "Angular", "Vue.js", "Node.js",
    "Django", "Flask", ".NET", "Spring", "Laravel",
    "Flutter", "Android", "iOS",
    "AWS", "Azure", "Google Cloud",
    "Docker", "Kubernetes", "Linux", "Windows Server",
    "Terraform", "Ansible", "CI/CD", "Git", "Jenkins",
    "REST API", "GraphQL", "Cisco", "Networking",
    "Cybersecurity", "Penetration Testing",
    "Data Analysis", "Machine Learning",
    "Artificial Intelligence", "Power BI", "Tableau",
    "Excel", "Spark", "Hadoop",
    "Selenium", "Automated Testing", "Agile", "Jira",
    "Figma", "Go", "Golang", "Help Desk",
    "IT Support", "Mac OS", "WordPress", "Joomla",
    "Salesforce", "Dynamics 365",
    "Cloud Computing", "Web Development",
    "Software Engineering", "PHPUnit",
    "Ruby", "Rails", "Swift", "Kotlin",
    "Redis", "Elasticsearch", "Kafka",
    "Microservices", "API", "HTML", "CSS",
    "RESTful", "GitHub", "GitLab",
    "Azure DevOps", "Prometheus", "Grafana"
        "Rust",
    "COBOL",
    "IDMS",
    "CICS",
    "Oracle",
    "PowerShell",
    "Assembly",
    "Cryptography",
    "Microcontroller",
    "Firmware",
    "Mainframe",
]


def extract_skills(text):

    found = []

    for skill in skills:

        pattern = (
            r"(?<!\w)" +
            re.escape(skill.lower()) +
            r"(?!\w)"
        )

        if re.search(pattern, text.lower()):
            found.append(skill)

    return found


df["Skills_List"] = df["Analysis_Text"].apply(extract_skills)

df["Skills"] = df["Skills_List"].apply(
    lambda x: ", ".join(x)
)

df["Skills_Count"] = df["Skills_List"].apply(len)


# ==========================================
# 4. SAVE VALIDATED DATASET
# ==========================================

df.drop(
    columns=["Analysis_Text", "Skills_List"],
    inplace=True
)

df.to_csv(
    "jobs_informatique_validated_skills.csv",
    index=False,
    encoding="utf-8-sig"
)


# ==========================================
# 5. IT RELEVANCE SUMMARY
# ==========================================

relevance_summary = (
    df["IT_Relevance"]
    .value_counts()
    .reset_index()
)

relevance_summary.columns = [
    "IT_Relevance",
    "Number_of_Jobs"
]

relevance_summary.to_csv(
    "it_relevance_summary.csv",
    index=False,
    encoding="utf-8-sig"
)


# ==========================================
# 6. SKILLS FREQUENCY
# ==========================================

all_skills = []

for skill_list in df["Skills"].fillna(""):

    if skill_list:
        all_skills.extend(skill_list.split(", "))

skills_frequency = (
    pd.Series(all_skills)
    .value_counts()
    .reset_index()
)

skills_frequency.columns = [
    "Skill",
    "Frequency"
]

skills_frequency.to_csv(
    "skills_frequency.csv",
    index=False,
    encoding="utf-8-sig"
)


# ==========================================
# 7. JOBS NEEDING MANUAL REVIEW
# ==========================================

review_jobs = df[
    df["IT_Relevance"] == "Needs review"
]

review_jobs.to_csv(
    "jobs_needing_manual_review.csv",
    index=False,
    encoding="utf-8-sig"
)


# ==========================================
# 8. FINAL RESULTS
# ==========================================

print("\n========== VALIDATION RESULTS ==========")
print(df["IT_Relevance"].value_counts())

print("\n========== TOP 15 SKILLS ==========")
print(skills_frequency.head(15).to_string(index=False))

print("\n========== DATASET CHECK ==========")
print("Original jobs:", len(pd.read_csv("jobs_informatique.csv")))
print("Processed jobs:", len(df))

print("\n========== OUTPUT FILES ==========")
print("1. jobs_informatique_validated_skills.csv")
print("2. it_relevance_summary.csv")
print("3. skills_frequency.csv")
print("4. jobs_needing_manual_review.csv")

print("\nValidation and skills extraction completed!")
