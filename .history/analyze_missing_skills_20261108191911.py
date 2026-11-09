
# ==========================================
# 5. CREATE RESULTS DATAFRAME
# ==========================================

results_df = pd.DataFrame(results)

jobs_with_candidates = results_df[
    results_df["Potential_Skills_Count"] > 0
]

print("\nJobs containing potential missing skills:")
print(len(jobs_with_candidates))

print("\nPotential missing skills frequency:")

all_found_skills = []

for skills_text in results_df["Potential_Missing_Skills"]:
    if skills_text:
        all_found_skills.extend(skills_text.split(", "))

frequency = pd.Series(all_found_skills).value_counts()

frequency_df = frequency.rename_axis(
    "Potential_Skill"
).reset_index(name="Frequency")

print(frequency_df.to_string(index=False))

# ==========================================
# 6. SAVE RESULTS
# ==========================================

results_df.to_csv(
    "potential_missing_skills_by_job.csv",
    index=False,
    encoding="utf-8-sig"
)

frequency_df.to_csv(
    "potential_missing_skills_frequency.csv",
    index=False,
    encoding="utf-8-sig"
)
