import pandas as pd

df = pd.read_csv("jobs_informatique_dates_fixed.csv")

zero_skills = df[df["Skills_Count"] == 0]

print("=" * 50)
print("ZERO SKILLS ANALYSIS")
print("=" * 50)

print("\nNumber of jobs with zero skills:")
print(len(zero_skills))

print("\nPercentage:")
print(round(len(zero_skills) / len(df) * 100, 2), "%")

print("\nJobs with zero skills:")

print(
    zero_skills[
        ["Job_Title", "Company", "Source", "Skills", "Description"]
    ].head(10).to_string(index=False)
)

print("\nSkills analysis completed!")