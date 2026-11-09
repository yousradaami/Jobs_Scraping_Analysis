import pandas as pd
from itertools import combinations
from collections import Counter

# Load dataset
df = pd.read_csv("jobs_informatique_cleaned.csv")

# Store skill pairs
pair_counts = Counter()

# Analyze skills in each job offer
for skills in df["Skills"].dropna():

    skill_list = [
        skill.strip()
        for skill in skills.split(",")
        if skill.strip() and skill.strip() != "Not specified"
    ]

    # Remove duplicate skills within the same job
    skill_list = sorted(set(skill_list))

    # Generate all pairs
    for pair in combinations(skill_list, 2):
        pair_counts[pair] += 1

# Convert results to DataFrame
results = pd.DataFrame(
    [
        {
            "Skill_1": pair[0],
            "Skill_2": pair[1],
            "Job_Count": count
        }
        for pair, count in pair_counts.most_common(20)
    ]
)

# Display results
print("=" * 55)
print("TOP 20 SKILL PAIRS")
print("=" * 55)

print(results.to_string(index=False))

# Save results
results.to_csv("skill_relationships.csv", index=False)

print("\nResults saved to skill_relationships.csv")