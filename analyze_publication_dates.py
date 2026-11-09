
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load dataset
df = pd.read_csv("jobs_informatique_cleaned.csv")

# 2. Convert publication dates
df["Publication_Date"] = pd.to_datetime(
    df["Publication_Date"],
    format="mixed",
    errors="coerce",
    utc=True
)

# 3. Display data validation
print("=" * 50)
print("PUBLICATION DATE ANALYSIS")
print("=" * 50)

total_jobs = len(df)
valid_dates = df["Publication_Date"].notna().sum()
invalid_dates = df["Publication_Date"].isna().sum()

print("\nTotal job offers:", total_jobs)
print("Valid dates:", valid_dates)
print("Invalid dates:", invalid_dates)

# 4. Display invalid date examples
if invalid_dates > 0:
    print("\nINVALID DATE EXAMPLES")
    print("=" * 50)

    invalid_examples = df.loc[
        df["Publication_Date"].isna(),
        ["Job_Title", "Publication_Date"]
    ]

    print(invalid_examples.head(10))

# 5. Display date range
valid_publication_dates = df["Publication_Date"].dropna()

if not valid_publication_dates.empty:
    print("\nPUBLICATION DATE RANGE")
    print("=" * 50)
    print("Earliest date:", valid_publication_dates.min())
    print("Latest date:", valid_publication_dates.max())

# 6. Extract publication month
df["Month"] = df["Publication_Date"].dt.strftime("%Y-%m")

# 7. Count job offers by month
monthly_counts = (
    df["Month"]
    .dropna()
    .value_counts()
    .sort_index()
)

print("\nJOB OFFERS BY MONTH")
print("=" * 50)
print(monthly_counts)

print("\nTotal offers with valid dates:", monthly_counts.sum())

# 8. Create line chart
plt.figure(figsize=(12, 6))

sns.lineplot(
    x=monthly_counts.index,
    y=monthly_counts.values,
    marker="o",
    linewidth=2
)

plt.title("Monthly Distribution of IT Job Offers")
plt.xlabel("Publication Month")
plt.ylabel("Number of Job Offers")

plt.grid(True, linestyle="--", alpha=0.5)
plt.xticks(rotation=45)

plt.tight_layout()

# 9. Save chart
plt.savefig(
    "job_offers_by_month.png",
    dpi=300,
    bbox_inches="tight"
)

# 10. Display chart
plt.show()

print("\nChart saved successfully!")
