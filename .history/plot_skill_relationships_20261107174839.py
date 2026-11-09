import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load skill relationships
df = pd.read_csv("skill_relationships.csv")

# Create labels
df["Skill_Pair"] = df["Skill_1"] + " + " + df["Skill_2"]

# Create figure
plt.figure(figsize=(12, 9))

sns.barplot(
    data=df,
    x="Job_Count",
    y="Skill_Pair"
)

plt.title("Top 20 Skill Combinations in IT Job Offers")
plt.xlabel("Number of Job Offers")
plt.ylabel("Skill Combinations")

plt.tight_layout()

plt.savefig("top_20_skill_relationships.png", dpi=300)

plt.show()

print("Chart saved successfully!")