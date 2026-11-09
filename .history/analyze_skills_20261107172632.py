```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load dataset
df = pd.read_csv("jobs_informatique_cleaned.csv")

# 2. Calculate skill frequencies
all_skills = df["Skills"].dropna().str.split(", ")

skills_list = all_skills.explode()

skill_counts = skills_list.value_counts().head(15)

print("=" * 50)
print("TOP 15 MOST DEMANDED IT SKILLS")
print("=" * 50)

print(skill_counts)

# 3. Create bar chart
plt.figure(figsize=(12, 8))

sns.barplot(
    x=skill_counts.values,
    y=skill_counts.index
)

plt.title("Top 15 Most Demanded IT Skills")
plt.xlabel("Number of Job Offers")
plt.ylabel("IT Skills")

plt.tight_layout()

# 4. Save chart
plt.savefig("top_15_it_skills.png", dpi=300)

# 5. Display chart
plt.show()

print("\nChart saved successfully!")
