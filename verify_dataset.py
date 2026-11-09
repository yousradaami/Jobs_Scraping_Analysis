import pandas as pd

# ==========================================
# 1. LOAD CLEANED DATASET
# ==========================================

file_path = "jobs_informatique_cleaned.csv"

df = pd.read_csv(file_path)

print("=" * 50)
print("DATASET VERIFICATION")
print("=" * 50)


# ==========================================
# 2. DATASET SIZE
# ==========================================

print("\n1. Dataset Shape:")

print("Rows:", df.shape[0])

print("Columns:", df.shape[1])


# ==========================================
# 3. COLUMN NAMES
# ==========================================

print("\n2. Columns:")

print(df.columns.tolist())


# ==========================================
# 4. MISSING VALUES
# ==========================================

print("\n3. Missing Values:")

print(df.isnull().sum())


# ==========================================
# 5. DUPLICATE ROWS
# ==========================================

print("\n4. Duplicate Rows:")

print(df.duplicated().sum())


# ==========================================
# 6. DUPLICATE JOB IDS
# ==========================================

if "Job_ID" in df.columns:

    print("\n5. Duplicate Job IDs:")

    print(df["Job_ID"].duplicated().sum())


# ==========================================
# 7. DUPLICATE JOB URLS
# ==========================================

if "Job_URL" in df.columns:

    print("\n6. Duplicate Job URLs:")

    print(df["Job_URL"].dropna().duplicated().sum())


# ==========================================
# 8. JOBS BY DATA SOURCE
# ==========================================

if "Source" in df.columns:

    print("\n7. Jobs by Data Source:")

    print(df["Source"].value_counts())


# ==========================================
# 9. JOBS BY IT RELEVANCE
# ==========================================

if "IT_Relevance" in df.columns:

    print("\n8. IT Relevance Distribution:")

    print(df["IT_Relevance"].value_counts())


# ==========================================
# 10. SAVE MISSING VALUES REPORT
# ==========================================

missing_report = df.isnull().sum()

missing_report.to_csv(
    "missing_values_report.csv",
    encoding="utf-8-sig"
)


# ==========================================
# 11. FINAL RESULT
# ==========================================

print("\nVerification completed!")

print("Report saved: missing_values_report.csv")
