import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load dataset
df = pd.read_csv("jobs_informatique_cleaned.csv")

print("=" * 50)
print("DATA VALIDATION")
print("=" * 50)

print("Total job offers:", len(df))
print("Missing job titles:", df["Job_Title"].isna().sum())

# 2. Clean job titles
df["Job_Title"] = (
    df["Job_Title"]
    .astype("string")
    .str.strip()
    .str.replace(r"\s+", " ", regex=True)
)

# 3. Count job titles
job_counts = df["Job_Title"].value_counts().head(10)

print("\nTOP 10 MOST COMMON JOB TITLES")
print("=" * 50)

print(job_counts)

print("\nTotal offers in top 10:", job_counts.sum())

# 4. Create bar chart
plt.figure(figsize=(12, 7))

ax = sns.barplot(
    x=job_counts.values,
    y=job_counts.index
)

# Add values to bars
for i, value in enumerate(job_counts.values):
    ax.text(value + 0.5, i, str(value), va="center")

plt.title("Top 10 Most Common Job Titles")
plt.xlabel("Number of Job Offers")
plt.ylabel("Job Title")

plt.tight_layout()

# 5. Save chart
plt.savefig("top_10_job_titles.png", dpi=300)

# 6. Display chart
plt.show()

print("\nChart saved successfully!")