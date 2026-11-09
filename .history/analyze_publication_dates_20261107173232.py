```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load dataset
df = pd.read_csv("jobs_informatique_cleaned.csv")

# 2. Convert dates using mixed format
df["Publication_Date"] = pd.to_datetime(
    df["Publication_Date"],
    format="mixed",
    errors="coerce",
    utc=True
)

# 3. Check date conversion
print("=" * 50)
print("PUBLICATION DATE ANALYSIS")
print("=" * 50)

print("\nTotal job offers:", len(df))
print("Valid dates:", df["Publication_Date"].notna().sum())
print("Invalid dates:", df["Publication_Date"].isna().sum())

# 4. Extract month
df["Month"] = df["Publication_Date"].dt.strftime("%Y-%m")

# 5. Count job offers by month
monthly_counts = df["Month"].value_counts().sort_index()

print("\nJOB OFFERS BY MONTH")
print("=" * 50)

print(monthly_counts)

# 6. Create line chart
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

# 7. Save chart
plt.savefig("job_offers_by_month.png", dpi=300)

# 8. Display chart
plt.show()

print("\nChart saved successfully!")
```