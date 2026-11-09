import pandas as pd

df = pd.read_csv("jobs_informatique_dates_fixed.csv")

zero_skills = df[df["Skills_Count"] == 0]

print("=" * 50)
print("SKILLS EXTRACTION CHECK")
print("=" * 50)

print("\nTotal jobs with zero skills:", len(zero_skills))

# Check Skills values
print("\nSkills field distribution:")

print(zero_skills["Skills"].value_counts(dropna=False))

# Check description length
print("\nDescription length:")

zero_skills["Description_Length"] = (
    zero_skills["Description"].astype(str).str.len()
)

print(zero_skills["Description_Length"].describe())

# Display job titles and sources
print("\nJobs with zero extracted skills:")

print(
    zero_skills[
        ["Job_Title", "Company", "Source", "Skills", "Skills_Count"]
    ].to_string(index=False)
)

# Save results
zero_skills.to_csv("jobs_zero_skills.csv", index=False)

print("\nSaved: jobs_zero_skills.csv")