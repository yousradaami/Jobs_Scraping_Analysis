import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("jobs_informatique_cleaned.csv")

# Extract experience level from job title
def get_experience(title):
    title = str(title).lower()

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

# Calculate average skills count
analysis = df[
    df["Experience_Level"] != "Not specified"
].groupby("Experience_Level")["Skills_Count"].agg(
    ["count", "mean", "median"]
).round(2)

print("=" * 55)
print("EXPERIENCE LEVEL AND SKILLS ANALYSIS")
print("=" * 55)

print(analysis)

# Create chart
analysis["mean"].sort_values().plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Average Number of Skills by Experience Level")
plt.xlabel("Experience Level")
plt.ylabel("Average Number of Skills")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("experience_skills_analysis.png", dpi=300)
plt.show()

# Save table
analysis.to_csv("experience_skills_analysis.csv")

print("\nAnalysis saved successfully!")