import pandas as pd
import os
import re
import matplotlib.pyplot as plt

# ==========================================
# 1. LOAD DATASET
# ==========================================

INPUT_FILE = "jobs_informatique_validated_skills.csv"
OUTPUT_DIR = "advanced_analysis"

os.makedirs(OUTPUT_DIR, exist_ok=True)

if not os.path.exists(INPUT_FILE):
    raise FileNotFoundError(f"Dataset not found: {INPUT_FILE}")

df = pd.read_csv(INPUT_FILE)

required_columns = ["Job_Title", "Skills"]

for column in required_columns:
    if column not in df.columns:
        raise ValueError(f"Missing required column: {column}")

print("=" * 55)
print("JOB ROLES AND TECHNICAL DOMAINS ANALYSIS")
print("=" * 55)

print(f"\nDataset loaded: {len(df)} jobs")


# ==========================================
# 2. CLASSIFY JOB ROLES
# ==========================================

role_keywords = {
    "Software Development": [
        "software engineer",
        "software developer",
        "backend",
        "back-end",
        "full stack",
        "fullstack"
    ],

    "Web Development": [
        "web developer",
        "frontend",
        "front-end",
        "react developer",
        "wordpress"
    ],

    "Data & AI": [
        "data scientist",
        "data analyst",
        "machine learning",
        "artificial intelligence",
        "ai engineer"
    ],

    "Cloud & DevOps": [
        "devops",
        "cloud engineer",
        "site reliability",
        "sre",
        "platform engineer"
    ],

    "Cybersecurity": [
        "security engineer",
        "cybersecurity",
        "information security",
        "penetration tester"
    ],

    "IT Support & Systems": [
        "it support",
        "help desk",
        "system administrator",
        "systems administrator",
        "technical support"
    ],

    "Networking": [
        "network engineer",
        "network administrator"
    ],

    "Database": [
        "database administrator",
        "database engineer",
        "dba"
    ],

    "QA & Testing": [
        "qa engineer",
        "quality assurance",
        "test engineer",
        "software tester"
    ],

    "UI/UX Design": [
        "ui designer",
        "ux designer",
        "product designer"
    ]
}


def contains_keyword(text, keyword):
    """
    Check whether a keyword exists as a separate phrase.
    Avoid matching Java inside JavaScript.
    """

    pattern = (
        r"(?<![a-zA-Z0-9+#])"
        + re.escape(keyword)
        + r"(?![a-zA-Z0-9+#])"
    )

    return bool(re.search(pattern, text, re.IGNORECASE))


def classify_role(title):

    if pd.isna(title):
        return "Other / Review"

    title = str(title).strip().lower()

    if not title:
        return "Other / Review"

    for role, keywords in role_keywords.items():

        for keyword in keywords:

            if contains_keyword(title, keyword):
                return role

    return "Other / Review"


df["Job_Role"] = df["Job_Title"].apply(classify_role)


# ==========================================
# 3. COUNT JOBS BY ROLE
# ==========================================

role_counts = df["Job_Role"].value_counts()

print("\n" + "=" * 55)
print("JOBS BY PROFESSIONAL ROLE")
print("=" * 55)

print(role_counts)

role_counts.to_csv(
    os.path.join(OUTPUT_DIR, "jobs_by_role.csv"),
    header=["Number_of_Jobs"]
)


# ==========================================
# 4. PLOT JOB ROLES
# ==========================================

plt.figure(figsize=(12, 7))

role_counts.sort_values().plot(kind="barh")

plt.title("IT Jobs by Professional Role")
plt.xlabel("Number of Jobs")
plt.ylabel("Job Role")

plt.tight_layout()

plt.savefig(
    os.path.join(OUTPUT_DIR, "jobs_by_role.png"),
    dpi=300
)

plt.close()


# ==========================================
# 5. CLASSIFY TECHNICAL DOMAINS
# ==========================================

domain_keywords = {

    "Web Development": [
        "React",
        "JavaScript",
        "TypeScript",
        "HTML",
        "CSS",
        "Angular",
        "Vue",
        "Node.js"
    ],

    "Software Development": [
        "Python",
        "Java",
        "C++",
        "C#",
        "Software Engineering",
        "PHP",
        "Ruby"
    ],

    "Data & AI": [
        "Machine Learning",
        "Data Analysis",
        "Power BI",
        "SQL",
        "TensorFlow",
        "Pandas"
    ],

    "Cloud & DevOps": [
        "AWS",
        "Azure",
        "Docker",
        "Kubernetes",
        "CI/CD",
        "Jenkins",
        "Terraform"
    ],

    "Cybersecurity & Networking": [
        "Cybersecurity",
        "Network Security",
        "Networking",
        "Linux",
        "Windows Server"
    ],

    "Databases & APIs": [
        "API",
        "PostgreSQL",
        "MySQL",
        "MongoDB",
        "Redis"
    ],

    "Testing & Quality": [
        "Testing",
        "Selenium",
        "QA",
        "Quality Assurance"
    ],

    "Tools & Collaboration": [
        "Git",
        "GitHub",
        "Agile",
        "Scrum",
        "Jira"
    ]
}


def extract_domains(skills):

    if pd.isna(skills):
        return []

    # Split skills using commas
    skill_list = [
        skill.strip()
        for skill in str(skills).split(",")
        if skill.strip()
    ]

    found_domains = []

    for domain, keywords in domain_keywords.items():

        for keyword in keywords:

            if any(
                contains_keyword(skill, keyword)
                for skill in skill_list
            ):
                found_domains.append(domain)
                break

    return found_domains


df["Technical_Domains"] = df["Skills"].apply(extract_domains)


# ==========================================
# 6. COUNT JOBS BY TECHNICAL DOMAIN
# ==========================================

domain_counts = {}

for domains in df["Technical_Domains"]:

    for domain in domains:

        domain_counts[domain] = (
            domain_counts.get(domain, 0) + 1
        )


domain_counts = pd.Series(
    domain_counts,
    dtype="int64"
).sort_values(ascending=False)


print("\n" + "=" * 55)
print("JOBS BY TECHNICAL DOMAIN")
print("=" * 55)

print(domain_counts)

domain_counts.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "jobs_by_technical_domain.csv"
    ),
    header=["Number_of_Jobs"]
)


# ==========================================
# 7. PLOT TECHNICAL DOMAINS
# ==========================================

if not domain_counts.empty:

    plt.figure(figsize=(12, 7))

    domain_counts.sort_values().plot(kind="barh")

    plt.title("IT Jobs by Technical Domain")
    plt.xlabel("Number of Jobs")
    plt.ylabel("Technical Domain")

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            OUTPUT_DIR,
            "jobs_by_technical_domain.png"
        ),
        dpi=300
    )

    plt.close()


# ==========================================
# 8. SAVE FINAL DATASET
# ==========================================

df.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "jobs_with_role_categories.csv"
    ),
    index=False
)


# ==========================================
# 9. FINAL SUMMARY
# ==========================================

print("\n" + "=" * 55)
print("ANALYSIS COMPLETED SUCCESSFULLY!")
print("=" * 55)

print("Total jobs analyzed:", len(df))

print("\nFiles saved in:", OUTPUT_DIR)

print("- jobs_by_role.csv")
print("- jobs_by_role.png")
print("- jobs_by_technical_domain.csv")
print("- jobs_by_technical_domain.png")
print("- jobs_with_role_categories.csv")