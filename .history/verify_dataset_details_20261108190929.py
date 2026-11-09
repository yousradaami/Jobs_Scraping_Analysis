```python
import pandas as pd

# ==========================================
# 1. LOAD DATASET
# ==========================================

file_path = "jobs_informatique_cleaned.csv"

df = pd.read_csv(file_path)

print("=" * 50)
print("DETAILED DATASET ANALYSIS")
print("=" * 50)


# ==========================================
# 2. JOB SOURCES
# ==========================================

if "Source" in df.columns:

    print("\n1. Jobs by Source:")

    print(df["Source"].value_counts())


# ==========================================
# 3. IT RELEVANCE
# ==========================================

if "IT_Relevance" in df.columns:

    print("\n2. IT Relevance:")

    print(df["IT_Relevance"].value_counts())


# ==========================================
# 4. PUBLICATION DATES
# ==========================================

if "Publication_Date" in df.columns:

    df["Publication_Date"] = pd.to_datetime(
        df["Publication_Date"],
        format="mixed",
        errors="coerce",
        utc=True
    )

    print("\n3. Invalid Publication Dates:")

    print(df["Publication_Date"].isna().sum())

    print("\n4. Date Range:")

    print("Earliest:", df["Publication_Date"].min())

    print("Latest:", df["Publication_Date"].max())


# ==========================================
# 5. SKILLS COUNT
# ==========================================

if "Skills_Count" in df.columns:

    print("\n5. Skills Count Statistics:")

    print(df["Skills_Count"].describe())


# ==========================================
# 6. DESCRIPTION LENGTH
# ==========================================

if "Description" in df.columns:

    df["Description_Length"] = (
        df["Description"]
        .fillna("")
        .astype(str)
        .str.len()
    )

    print("\n6. Description Length:")

    print(df["Description_Length"].describe())

    print("\nDescriptions shorter than 100 characters:")

    print((df["Description_Length"] < 100).sum())


# ==========================================
# 7. TOP CATEGORIES
# ==========================================

if "Categories" in df.columns:

    print("\n7. Top Categories:")

    print(df["Categories"].value_counts().head(10))


# ==========================================
# 8. FINAL RESULT
# ==========================================

print("\nDetailed verification completed!")
