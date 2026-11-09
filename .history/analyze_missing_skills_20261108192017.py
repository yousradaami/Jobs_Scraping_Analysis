import pandas as pd
import re

# ==========================================
# 1. LOAD JOBS WITH ZERO EXTRACTED SKILLS
# ==========================================

input_file = "jobs_zero_skills.csv"

df = pd.read_csv(input_file)

print("=" * 60)
print("MISSING SKILLS ANALYSIS")
print("=" * 60)

print("Jobs to analyze:", len(df))


# ==========================================
# 2. POSSIBLE MISSING TECHNICAL SKILLS
# ==========================================

candidate_skills = [
    "Rust",
    "COBOL",
    "IDMS",
    "CICS",
    "Oracle",
    "PowerShell",
    "Bash",
    "Assembly",
    "Perl",
    "Scala",
    "MATLAB",
    "Fortran",
    "Swift",
    "Kotlin",
    "Ruby",
    "Rails",
    "SQL Server",
    "PL/SQL",
    "T-SQL",
    "SAP",
    "Unix",
    "Shell Scripting",
    "Embedded C",
    "CMake",
    "Solidity",
    "Elixir",
    "Erlang",
    "Dart",
    "React Native",
    "OpenGL",
    "CUDA",
    "Jenkins",
    "Power BI",
    "VBA",
    "R Programming",
    "Jupyter",
    "Pandas",
    "NumPy",
    "TensorFlow",
    "PyTorch",
    "OpenAI API",
    "LLM",
    "Generative AI",
    "Blockchain",
    "Cryptography",
    "Microcontroller",
    "Firmware",
    "SAP HANA",
    "Mainframe"
]


# ==========================================
# 3. PREPARE TEXT
# ==========================================

text_columns = ["Job_Title", "Categories", "Description"]

for col in text_columns:
    if col not in df.columns:
        df[col] = ""

    df[col] = df[col].fillna("").astype(str)

df["Analysis_Text"] = (
    df["Job_Title"] + " " +
    df["Categories"] + " " +
    df["Description"]
).str.lower()


# ==========================================
# 4. SEARCH FOR CANDIDATE SKILLS
# ==========================================

results = []

for index, row in df.iterrows():

    text = row["Analysis_Text"]

    found_skills = []

    for skill in candidate_skills:

        pattern = (
            r"(?<!\w)" +
            re.escape(skill.lower()) +
            r"(?!\w)"
        )

        if re.search(pattern, text):
            found_skills.append(skill)

    results.append({
        "Job_Title": row["Job_Title"],
        "Company": row.get("Company", "Unknown"),
        "Source": row.get("Source", "Unknown"),
        "Potential_Missing_Skills": ", ".join(found_skills),
        "Potential_Skills_Count": len(found_skills)
    })


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



# ==========================================
# 7. FINAL SUMMARY
# ==========================================

print("\n" + "=" * 60)
print("ANALYSIS COMPLETED")
print("=" * 60)

print("Total jobs analyzed:", len(df))
print("Jobs with potential missing skills:", len(jobs_with_candidates))

print("\nGenerated files:")
print("1. potential_missing_skills_by_job.csv")
print("2. potential_missing_skills_frequency.csv")