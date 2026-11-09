import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load results
df = pd.read_csv("skills_by_experience.csv")

# Select the 10 most frequent skills overall
top_skills = (
    df.groupby("Skill")["Job_Count"]
    .sum()
    .nlargest(10)
    .index
)

# Filter selected skills
plot_data = df[df["Skill"].isin(top_skills)]

# Create comparison chart
plt.figure(figsize=(14, 8))

sns.barplot(
    data=plot_data,
    x="Skill",
    y="Percentage",
    hue="Experience_Level"
)

plt.title("Top IT Skills by Experience Level")
plt.xlabel("IT Skills")
plt.ylabel("Percentage of Job Offers (%)")

plt.xticks(rotation=45, ha="right")
plt.legend(title="Experience Level")

plt.tight_layout()

plt.savefig(
    "skills_comparison_by_experience.png",
    dpi=300
)

plt.show()

print("Chart saved successfully!")