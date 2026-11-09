import pandas as pd

df = pd.read_csv(
    "advanced_analysis/jobs_with_role_categories.csv"
)

other_jobs = df[
    df["Job_Role"] == "Other / Review"
]

print("=" * 50)
print("UNCLASSIFIED JOB TITLES")
print("=" * 50)

print("Total:", len(other_jobs))

print("\nMost frequent job titles:")

print(
    other_jobs["Job_Title"]
    .value_counts()
    .head(50)
)

other_jobs[
    ["Job_Title", "Skills"]
].to_csv(
    "advanced_analysis/unclassified_jobs.csv",
    index=False
)

print("\nSaved: advanced_analysis/unclassified_jobs.csv")