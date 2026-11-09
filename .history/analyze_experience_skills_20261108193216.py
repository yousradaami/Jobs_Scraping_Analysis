```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load dataset
df = pd.read_csv("jobs_informatique_cleaned.csv")

# 2. Validate required columns
required_columns = ["Job_Title", "Skills_Count"]

for column in required_columns:
    if column not in df.columns:
        raise ValueError(f"Missing required column: {column}")

# 3. Clean data
df["Job_Title"] = df["Job_Title"].fillna("").astype(str)

df["Skills_Count"] = pd.to_numeric(
    df["Skills_Count"],
    errors="coerce"
)

# 4. Extract experience level from job title
def get_experience(title):
    title = title.lower()

    if "principal" in title:
        return "Principal"
    elif "staff" in title:
        return "Staff"
    elif "senior" in title:
        return "Senior"
    elif "junior" in title:
        return "Junior"
    elif "mid-level" in title or "mid level" in title:
        return "Mid-level"
    else:
        return "Not specified"


df["Experience_Level"] = df["Job_Title"].apply(get_experience)

# 5. Display experience distribution
experience_counts = df["Experience_Level"].value_counts()

experience_percentages = (
    df["Experience_Level"].value_counts(normalize=True) * 100
)

print("=" * 55)
print("EXPERIENCE LEVEL DISTRIBUTION")
print("=" * 55)

for level, count in experience_counts.items():
    percentage = experience_percentages[level]

    print(f"{level}: {count} jobs ({percentage:.2f}%)")

# 6. Calculate skills statistics
analysis = df.groupby("Experience_Level")["Skills_Count"].agg(
    ["count", "mean", "median"]
).round(2)

print("\n" + "=" * 55)
print("EXPERIENCE LEVEL AND SKILLS ANALYSIS")
print("=" * 55)

print(analysis)

# 7. Create chart
chart_data = analysis.drop(
    index="Not specified",
    errors="ignore"
)["mean"].dropna().sort_values()

if not chart_data.empty:

    plt.figure(figsize=(10, 6))

    ax = sns.barplot(
        x=chart_data.index,
        y=chart_data.values
    )

    plt.title("Average Number of Skills by Experience Level")
    plt.xlabel("Experience Level")
    plt.ylabel("Average Number of Skills")

    plt.xticks(rotation=0)

    # Add values above bars
    for i, value in enumerate(chart_data.values):
        ax.text(
            i,
            value,
            f"{value:.2f}",
            ha="center",
            va="bottom"
        )

    plt.tight_layout()

    plt.savefig(
        "experience_skills_analysis.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()

else:
    print("\nNo experience data available for visualization.")

# 8. Save analysis table
analysis.to_csv("experience_skills_analysis.csv")

# 9. Save dataset with experience levels
df.to_csv(
    "jobs_with_experience_levels.csv",
    index=False
)

print("\nAnalysis saved successfully!")
