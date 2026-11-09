import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

# 1. Load dataset
df = pd.read_csv("jobs_informatique_cleaned.csv")

print("=" * 55)
print("DATA VALIDATION")
print("=" * 55)

print("Total job offers:", len(df))
print("Missing Skills:", df["Skills"].isna().sum())

# 2. Extract skills without duplicates per job
skill_counts = Counter()

for skills in df["Skills"].dropna():

    skill_list = [
        skill.strip()
        for skill in str(skills).split(",")
        if skill.strip()
        and skill.strip().lower() != "not specified"
    ]

    # Count each skill only once per job
    skill_list = set(skill_list)

    skill_counts.update(skill_list)

# 3. Get top 15 skills
top_skills = skill_counts.most_common(15)

skill_names = [item[0] for item in top_skills]
skill_values = [item[1] for item in top_skills]

print("\nTOP 15 MOST DEMANDED IT SKILLS")
print("=" * 55)

for skill, count in top_skills:
    percentage = (count / len(df)) * 100
    print(f"{skill:<25} {count:>5} jobs ({percentage:.2f}%)")

# 4. Create bar chart
plt.figure(figsize=(12, 8))

ax = sns.barplot(
    x=skill_values,
    y=skill_names
)

# Add values
for i, value in enumerate(skill_values):
    ax.text(value + 5, i, str(value), va="center")

plt.title("Top 15 Most Demanded IT Skills")
plt.xlabel("Number of Job Offers")
plt.ylabel("IT Skills")

plt.tight_layout()

# 5. Save chart
plt.savefig("top_15_it_skills.png", dpi=300)

# 6. Save results
results = pd.DataFrame({
    "Skill": skill_names,
    "Job_Count": skill_values,
    "Percentage": [
        round(value / len(df) * 100, 2)
        for value in skill_values
    ]
})

results.to_csv("skills_frequency.csv", index=False)

plt.show()

print("\nChart and results saved successfully!")