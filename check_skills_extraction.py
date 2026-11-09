
import pandas as pd

# =====================================
# 1. Load dataset
# =====================================

df = pd.read_csv("jobs_informatique_dates_fixed.csv")

# =====================================
# 2. Select jobs with zero skills
# =====================================

zero_skills = df[df["Skills_Count"] == 0].copy()

print("=" * 50)
print("SKILLS EXTRACTION CHECK")
print("=" * 50)

print("\nTotal jobs with zero skills:", len(zero_skills))

# =====================================
# 3. Skills field distribution
# =====================================

print("\nSkills field distribution:")

print(zero_skills["Skills"].value_counts(dropna=False))

# =====================================
# 4. Description length
# =====================================

print("\nDescription length:")

zero_skills["Description_Length"] = (
    zero_skills["Description"]
    .fillna("")
    .astype(str)
    .str.len()
)

print(zero_skills["Description_Length"].describe())

# =====================================
# 5. Display jobs
# =====================================

print("\nJobs with zero extracted skills:")

print(
    zero_skills[
        ["Job_Title", "Company", "Source", "Skills", "Skills_Count"]
    ].to_string(index=False)
)

# =====================================
# 6. Save results
# =====================================

zero_skills.to_csv("jobs_zero_skills.csv", index=False)

print("\nSaved: jobs_zero_skills.csv")
print("\nSKILLS EXTRACTION CHECK COMPLETED!")
