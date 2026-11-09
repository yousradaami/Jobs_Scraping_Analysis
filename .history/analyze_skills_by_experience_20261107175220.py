import pandas as pd
from collections import Counter

# Load dataset
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

# Analyze skills for each experience level
all_results = []

levels = ["Junior", "Mid-level", "Senior", "Staff", "Principal"]

for level in levels:

    group = df[df["Experience_Level"] == level]

    skill_counts = Counter()

    for skills in group["Skills"].dropna():

        skill_list = [
            skill.strip()
            for skill in str(skills).split(",")
            if skill.strip()
            and skill.strip() != "Not specified"
        ]

        skill_counts.update(set(skill_list))

    print("\n" + "=" * 55)
    print(f"TOP 10 SKILLS - {level}")
    print("=" * 55)

    for skill, count in skill_counts.most_common(10):

        percentage = (count / len(group)) * 100

        print(
            f"{skill:<25} {count:>5} jobs "
            f"({percentage:.2f}%)"
        )

        all_results.append({
            "Experience_Level": level,
            "Skill": skill,
            "Job_Count": count,
            "Percentage": round(percentage, 2)
        })

# Save results
results = pd.DataFrame(all_results)

results.to_csv(
    "skills_by_experience.csv",
    index=False
)

print("\nResults saved to skills_by_experience.csv")