
import pandas as pd
import matplotlib.pyplot as plt
import os

# =====================================
# 1. LOAD DATA
# =====================================

df = pd.read_csv("jobs_informatique_validated_skills.csv")

print("Dataset loaded:", len(df), "jobs")

# Create folder for charts
os.makedirs("visualizations", exist_ok=True)


# =====================================
# 2. JOBS BY SOURCE
# =====================================

source_counts = df["Source"].value_counts()

plt.figure(figsize=(10, 6))
source_counts.plot(kind="bar")

plt.title("Number of IT Job Offers by Source")
plt.xlabel("Job Source")
plt.ylabel("Number of Jobs")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()

plt.savefig("visualizations/jobs_by_source.png")
plt.close()


# =====================================
# 3. TOP 15 SKILLS
# =====================================

all_skills = []

for skills in df["Skills"].fillna(""):
    all_skills.extend(
        skill.strip() for skill in skills.split(",")
        if skill.strip()
    )

skills_counts = pd.Series(all_skills).value_counts().head(15)

plt.figure(figsize=(10, 7))
skills_counts.sort_values().plot(kind="barh")

plt.title("Top 15 Most Requested IT Skills")
plt.xlabel("Number of Job Offers")
plt.ylabel("Skills")
plt.tight_layout()

plt.savefig("visualizations/top_15_skills.png")
plt.close()


# =====================================
# 4. JOBS BY LOCATION
# =====================================

locations = df["Location"].fillna("Not specified")

location_counts = locations.value_counts().head(10)

plt.figure(figsize=(10, 6))
location_counts.sort_values().plot(kind="barh")

plt.title("Top 10 Job Locations")
plt.xlabel("Number of Job Offers")
plt.ylabel("Location")
plt.tight_layout()

plt.savefig("visualizations/jobs_by_location.png")
plt.close()


# =====================================
# 5. JOBS BY CATEGORY
# =====================================

categories = []

for value in df["Categories"].fillna(""):
    categories.extend(
        category.strip()
        for category in value.split(",")
        if category.strip()
    )

category_counts = pd.Series(categories).value_counts().head(10)

if not category_counts.empty:

    plt.figure(figsize=(10, 6))
    category_counts.sort_values().plot(kind="barh")

    plt.title("Top 10 IT Job Categories")
    plt.xlabel("Number of Job Offers")
    plt.ylabel("Category")
    plt.tight_layout()

    plt.savefig("visualizations/jobs_by_category.png")
    plt.close()


# =====================================
# 6. JOBS BY PUBLICATION DATE
# =====================================

df["Publication_Date"] = pd.to_datetime(
    df["Publication_Date"],
    errors="coerce",
    utc=True
)

valid_dates = df.dropna(subset=["Publication_Date"]).copy()

if not valid_dates.empty:

    valid_dates["Month"] = (
        valid_dates["Publication_Date"]
        .dt.to_period("M")
        .astype(str)
    )

    monthly_counts = valid_dates["Month"].value_counts().sort_index()

    plt.figure(figsize=(12, 6))
    monthly_counts.plot(kind="line", marker="o")

    plt.title("IT Job Offers by Publication Month")
    plt.xlabel("Month")
    plt.ylabel("Number of Job Offers")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()

    plt.savefig("visualizations/jobs_by_month.png")
    plt.close()


# =====================================
# 7. VALIDATION RESULTS
# =====================================

validation_counts = df["IT_Relevance"].value_counts()

plt.figure(figsize=(7, 7))
validation_counts.plot(kind="pie", autopct="%1.1f%%")

plt.title("IT Job Relevance Validation")
plt.ylabel("")
plt.tight_layout()

plt.savefig("visualizations/it_validation.png")
plt.close()


# =====================================
# 8. FINAL SUMMARY
# =====================================

print("\n========== VISUALIZATION SUMMARY ==========")

print("Total jobs:", len(df))
print("\nJobs by source:")
print(source_counts)

print("\nTop 10 skills:")
print(skills_counts.head(10))

print("\nTop 10 locations:")
print(location_counts)

print("\nValidation:")
print(validation_counts)

print("\nAll charts saved in the visualizations folder!")
