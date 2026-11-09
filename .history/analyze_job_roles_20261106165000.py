
import pandas as pd
import os
import matplotlib.pyplot as plt

# 1. Load dataset
INPUT_FILE = "jobs_informatique_validated_skills.csv"
OUTPUT_DIR = "advanced_analysis"

os.makedirs(OUTPUT_DIR, exist_ok=True)

df = pd.read_csv(INPUT_FILE)

print("Dataset loaded:", len(df), "jobs")

# 2. Classify job roles based on job titles
role_keywords = {
    "Software Development": ["software engineer", "software developer", "backend", "back-end", "full stack", "fullstack"],
    "Web Development": ["web developer", "frontend", "front-end", "react developer", "wordpress"],
    "Data & AI": ["data scientist", "data analyst", "machine learning", "artificial intelligence", "ai engineer"],
    "Cloud & DevOps": ["devops", "cloud engineer", "site reliability", "sre", "platform engineer"],
    "Cybersecurity": ["security engineer", "cybersecurity", "information security", "penetration tester"],
    "IT Support & Systems": ["it support", "help desk", "system administrator", "systems administrator", "technical support"],
    "Networking": ["network engineer", "network administrator"],
    "Database": ["database administrator", "database engineer", "dba"],
    "QA & Testing": ["qa engineer", "quality assurance", "test engineer", "software tester"],
    "UI/UX Design": ["ui designer", "ux designer", "product designer"]
}

def classify_role(title):
    title = str(title).lower()

    for role, keywords in role_keywords.items():
        if any(keyword in title for keyword in keywords):
            return role

    return "Other / Review"

df["Job_Role"] = df["Job_Title"].apply(classify_role)

# 3. Count jobs by role
role_counts = df["Job_Role"].value_counts()

print("\nJOBS BY ROLE:")
print(role_counts)

role_counts.to_csv(
    os.path.join(OUTPUT_DIR, "jobs_by_role.csv"),
    header=["Number_of_Jobs"]
)

# 4. Plot job roles
plt.figure(figsize=(12, 7))
role_counts.sort_values().plot(kind="barh")
plt.title("IT Jobs by Professional Role")
plt.xlabel("Number of Jobs")
plt.ylabel("Job Role")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "jobs_by_role.png"))
plt.close()

# 5. Analyze technical domains from extracted skills
domain_keywords = {
    "Web Development": ["React", "JavaScript", "TypeScript", "HTML", "CSS", "Angular", "Vue", "Node.js"],
    "Software Development": ["Python", "Java", "C++", "C#", "Software Engineering", "PHP", "Ruby"],
    "Data & AI": ["Machine Learning", "Data Analysis", "Power BI", "SQL", "TensorFlow", "Pandas"],
    "Cloud & DevOps": ["AWS", "Azure", "Docker", "Kubernetes", "CI/CD", "Jenkins", "Terraform"],
    "Cybersecurity & Networking": ["Cybersecurity", "Network Security", "Networking", "Linux", "Windows Server"],
    "Databases & APIs": ["API", "PostgreSQL", "MySQL", "MongoDB", "Redis"],
    "Testing & Quality": ["Testing", "Selenium", "QA", "Quality Assurance"],
    "Tools & Collaboration": ["Git", "GitHub", "Agile", "Scrum", "Jira"]
}

def extract_domains(skills):
    skills = str(skills).lower()
    found_domains = []

    for domain, keywords in domain_keywords.items():
        if any(keyword.lower() in skills for keyword in keywords):
            found_domains.append(domain)

    return found_domains

df["Technical_Domains"] = df["Skills"].apply(extract_domains)

domain_counts = {}

for domains in df["Technical_Domains"]:
    for domain in domains:
        domain_counts[domain] = domain_counts.get(domain, 0) + 1

domain_counts = pd.Series(domain_counts).sort_values(ascending=False)

print("\nJOBS BY TECHNICAL DOMAIN:")
print(domain_counts)

domain_counts.to_csv(
    os.path.join(OUTPUT_DIR, "jobs_by_technical_domain.csv"),
    header=["Number_of_Jobs"]
)

# 6. Plot technical domains
plt.figure(figsize=(12, 7))
domain_counts.sort_values().plot(kind="barh")
plt.title("IT Jobs by Technical Domain")
plt.xlabel("Number of Jobs")
plt.ylabel("Technical Domain")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "jobs_by_technical_domain.png"))
plt.close()

# 7. Save final dataset
df.to_csv(
    os.path.join(OUTPUT_DIR, "jobs_with_role_categories.csv"),
    index=False
)

print("\nAnalysis completed successfully!")
print("Results saved in:", OUTPUT_DIR)
 