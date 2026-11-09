```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load dataset
df = pd.read_csv("jobs_informatique_cleaned.csv")

# 2. Convert Publication_Date to datetime
df["Publication_Date"] = pd.to_datetime(
    df["Publication_Date"],
    errors="coerce",
    utc=True
)

# 3. Extract month
df["Month"] = df["Publication_Date"].dt.to_period("M").astype(str)

# 4. Count job offers by month
monthly_counts = df["Month"].value_counts().sort_index()

print("=" * 50)
print("JOB OFFERS BY MONTH")
print("=" * 50)

print(monthly_counts)

# 5. Create line chart
plt.figure(figsize=(12, 6))

sns.lineplot(
    x=monthly_counts.index,
    y=monthly_counts.values,
    marker="o"
)

plt.title("Job Offers by Publication Month")
plt.xlabel("Publication Month")
plt.ylabel("Number of Job Offers")

plt.xticks(rotation=45)

plt.tight_layout()

# 6. Save chart
plt.savefig("job_offers_by_month.png", dpi=300)

# 7. Display chart
plt.show()

print("\nChart saved successfully!")
