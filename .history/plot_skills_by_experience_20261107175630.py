import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

# Load original dataset
df = pd.read_csv("jobs_informatique_cleaned.csv")

# Classify experience level
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

levels = ["Junior", "Mid-level", "Senior", "Staff", "Principal"]

all_results = []

# Count all skills in each level
for level in levels:

    group = df[df["Experience_Level"] == level]
    counter = Counter()

    for skills in group["Skills"].dropna():

        skill_list = [
            s.strip()
            for s in str(skills).split(",")
            if s.strip() and s.strip() != "Not specified"
        ]

        counter.update(set(skill_list))

    for skill, count in counter.items():

        percentage = count / len(group) * 100

        all_results.append({
            "Experience_Level": level,
            "Skill": skill,
            "Job_Count": count,
            "Percentage": percentage
        })

# Create complete DataFrame
results = pd.DataFrame(all_results)

# Select top 10 skills across all levels
top_skills = (
    results.groupby("Skill")["Job_Count"]
    .sum()
    .nlargest(10)
    .index
)

plot_data = results[
    results["Skill"].isin(top_skills)
]

# Create chart
plt.figure(figsize=(14, 8))

sns.barplot(
    data=plot_data,
    x="Skill",
    y="Percentage",
    hue="Experience_Level"
)

plt.title("Top 10 IT Skills by Experience Level")
plt.xlabel("IT Skills")
plt.ylabel("Percentage of Job Offers (%)")

plt.xticks(rotation=45, ha="right")
plt.legend(title="Experience Level")

plt.tight_layout()

plt.savefig(
    "skills_comparison_by_experience_corrected.png",
    dpi=300
)

plt.show()

# Save complete results
results.to_csv(
    "all_skills_by_experience.csv",
    index=False
)

print("Corrected chart saved successfully!")
