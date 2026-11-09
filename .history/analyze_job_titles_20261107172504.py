```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load dataset
df = pd.read_csv("jobs_informatique_cleaned.csv")

# 2. Count job titles
job_counts = df["Job_Title"].value_counts().head(10)

print("=" * 50)
print("TOP 10 MOST COMMON JOB TITLES")
print("=" * 50)

print(job_counts)

# 3. Create bar chart
plt.figure(figsize=(12, 7))

sns.barplot(
    x=job_counts.values,
    y=job_counts.index
)

plt.title("Top 10 Most Common Job Titles")
plt.xlabel("Number of Job Offers")
plt.ylabel("Job Title")

plt.tight_layout()

# 4. Save chart
plt.savefig("top_10_job_titles.png", dpi=300)

# 5. Display chart
plt.show()

print("\nChart saved successfull