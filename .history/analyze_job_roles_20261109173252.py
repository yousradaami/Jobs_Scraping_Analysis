import pandas as pd
import os
import re
import matplotlib.pyplot as plt

# =====================================================
# 1. LOAD DATASET
# =====================================================

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

print("=" * 60)
print("JOB ROLES AND TECHNICAL DOMAINS ANALYSIS")
print("=" * 60)

print(f"\nDataset loaded: {len(df)} jobs")


# =====================================================
# 2. ROLE CLASSIFICATION KEYWORDS
# =====================================================

role_keywords = {

    "Cybersecurity": [
        "cybersecurity",
        "cyber security",
        "information security",
        "security engineer",
        "security analyst",
        "security specialist",
        "security architect",
        "security developer",
        "penetration tester",
        "detection and response",
        "incident response",
        "platform security",
        "software security",
        "security operations",
        "soc analyst"
    ],

    "Data & AI": [
        "data scientist",
        "data analyst",
        "data engineer",
        "machine learning",
        "artificial intelligence",
        "ai engineer",
        "ai ml engineer",
        "ml engineer",
        "ai lead",
        "conversational ai",
        "data analytics",
        "analytics engineer",
        "business intelligence",
        "bi developer"
    ],

    "QA & Testing": [
        "qa engineer",
        "qa tester",
        "quality assurance",
        "quality engineer",
        "quality specialist",
        "test engineer",
        "software tester",
        "software verification",
        "automation tester",
        "automated testing",
        "software quality",
        "testing engineer",
        "test automation"
    ],

    "Networking": [
        "network engineer",
        "network administrator",
        "telecommunications engineer",
        "telecommunication engineer",
        "software defined networking",
        "networking engineer",
        "network architect",
        "network specialist"
    ],

    "Database": [
        "database administrator",
        "database engineer",
        "database developer",
        "dba"
    ],

    "IT Support & Systems": [
        "it support",
        "help desk",
        "service desk",
        "system administrator",
        "systems administrator",
        "technical support",
        "it systems engineer",
        "enterprise support",
        "customer support",
        "software support",
        "system support",
        "desktop support",
        "support specialist"
    ],

    "Cloud & DevOps": [
        "devops",
        "cloud engineer",
        "cloud architect",
        "cloud solutions architect",
        "cloud engineering",
        "site reliability",
        "sre",
        "platform engineer",
        "infrastructure engineer",
        "cloud infrastructure",
        "cloud platform",
        "cloud operations",
        "cloud specialist"
    ],

    "UI/UX Design": [
        "ui designer",
        "ux designer",
        "product designer",
        "software designer",
        "web designer",
        "interactive designer",
        "user experience designer",
        "user interface designer"
    ],

    "Web Development": [
        "web developer",
        "website developer",
        "web engineer",
        "web application",
        "web development",
        "web services developer",
        "web platform developer",
        "web scraping",
        "web scraper",
        "web design engineer",
        "web implementation",
        "web support engineer",
        "frontend",
        "front-end",
        "front end",
        "react developer",
        "react js developer",
        "react.js developer",
        "angular developer",
        "wordpress",
        "drupal developer",
        "shopify developer",
        "webflow developer",
        "joomla developer",
        "magento developer",
        "salesforce developer",
        "javascript developer",
        "typescript developer",
        "html developer",
        "php engineer",
        "php developer",
        "ui developer",
        "ui engineer",
        "website designer and developer",
        "interactive web",
        "web game developer",
        "web implementation specialist"
    ],

    "Software Development": [
        "software engineer",
        "software developer",
        "software engineering",
        "software development",
        "software architect",
        "software architecture",
        "software systems engineer",
        "software principal engineer",
        "software chief engineer",
        "software factory engineer",
        "software production engineer",
        "software consultant",
        "software project engineer",
        "software project specialist",
        "software support engineer",
        "software security developer",
        "software integration engineer",
        "software verification engineer",
        "software applications developer",
        "software programmer",
        "software dev engr",
        "software or systems engineer",
        "application developer",
        "application engineer",
        "application architect",
        "embedded software",
        "firmware engineer",
        "firmware developer",
        ".net developer",
        "backend developer",
        "back-end developer",
        "back end developer",
        "full stack developer",
        "fullstack developer",
        "full-stack developer",
        "laravel developer",
        "java developer",
        "python developer",
        "ruby developer",
        "golang developer",
        "go developer",
        "c++ developer",
        "c# developer",
        "cobol developer",
        "cobol programmer",
        "development engineer",
        "software dev",
        "software systems",
        "software or systems engineers",
        "systems engineer",
        "system software",
        "software architect",
        "software project",
        "software consultant",
        "software delivery lead",
        "software applications",
        "software integration",
        "software platform",
        "software development manager",
        "software engineering manager",
        "software development director",
        "engineering manager software",
        "software lead",
        "software specialist",
        "software designer",
        "software engineer",
        "developer",
        "programmer",
        "application",
        "engineer"
    ],

    "Other / Review": []
}


# =====================================================
# 3. KEYWORD MATCHING FUNCTION
# =====================================================

def contains_keyword(text, keyword):

    pattern = (
        r"(?<![a-zA-Z0-9+#])"
        + re.escape(keyword)
        + r"(?![a-zA-Z0-9+#])"
    )

    return bool(
        re.search(pattern, text, re.IGNORECASE)
    )


# =====================================================
# 4. CLASSIFY JOB ROLES
# =====================================================

def classify_role(title):

    if pd.isna(title):
        return "Other / Review"

    title = str(title).strip().lower()

    if not title:
        return "Other / Review"

    for role, keywords in role_keywords.items():

        if role == "Other / Review":
            continue

        for keyword in keywords:

            if contains_keyword(title, keyword):
                return role

    return "Other / Review"


df["Job_Role"] = df["Job_Title"].apply(classify_role)


# =====================================================
# 5. COUNT JOBS BY PROFESSIONAL ROLE
# =====================================================

role_counts = df["Job_Role"].value_counts()

print("\n" + "=" * 60)
print("JOBS BY PROFESSIONAL ROLE")
print("=" * 60)

print(role_counts)

role_counts.to_csv(
    os.path.join(OUTPUT_DIR, "jobs_by_role.csv"),
    header=["Number_of_Jobs"]
)

role_percentages = (
    role_counts / len(df) * 100
).round(2)

print("\nROLE PERCENTAGES:")
print(role_percentages)


# =====================================================
# 6. PLOT JOB ROLES
# =====================================================

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


# =====================================================
# 7. TECHNICAL DOMAIN KEYWORDS
# =====================================================

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


# =====================================================
# 8. EXTRACT TECHNICAL DOMAINS
# =====================================================

def extract_domains(skills):

    if pd.isna(skills):
        return []

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


df["Technical_Domains"] = df["Skills"].apply(
    extract_domains
)


# =====================================================
# 9. COUNT JOBS BY TECHNICAL DOMAIN
# =====================================================

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


print("\n" + "=" * 60)
print("JOBS BY TECHNICAL DOMAIN")
print("=" * 60)

print(domain_counts)

domain_percentages = (
    domain_counts / len(df) * 100
).round(2)

print("\nDOMAIN PERCENTAGES:")
print(domain_percentages)

domain_counts.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "jobs_by_technical_domain.csv"
    ),
    header=["Number_of_Jobs"]
)


# =====================================================
# 10. PLOT TECHNICAL DOMAINS
# =====================================================

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


# =====================================================
# 11. SAVE FINAL DATASET
# =====================================================

df.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "jobs_with_role_categories.csv"
    ),
    index=False
)


# =====================================================
# 12. SAVE UNCLASSIFIED JOBS FOR REVIEW
# =====================================================

unclassified_jobs = df[
    df["Job_Role"] == "Other / Review"
]

unclassified_jobs[
    ["Job_Title", "Skills", "Job_Role"]
].to_csv(
    os.path.join(
        OUTPUT_DIR,
        "unclassified_jobs.csv"
    ),
    index=False
)


# =====================================================
# 13. FINAL SUMMARY
# =====================================================

classified_count = len(df) - len(unclassified_jobs)

classified_percentage = (
    classified_count / len(df) * 100
    if len(df) > 0 else 0
)

print("\n" + "=" * 60)
print("FINAL ANALYSIS SUMMARY")
print("=" * 60)

print("Total jobs:", len(df))

print(
    "Classified jobs:",
    classified_count,
    f"({classified_percentage:.2f}%)"
)

print(
    "Unclassified jobs:",
    len(unclassified_jobs)
)

print("\nFiles saved in:", OUTPUT_DIR)

print("- jobs_by_role.csv")
print("- jobs_by_role.png")
print("- jobs_by_technical_domain.csv")
print("- jobs_by_technical_domain.png")
print("- jobs_with_role_categories.csv")
print("- unclassified_jobs.csv")

print("\nAnalysis completed successfully!")