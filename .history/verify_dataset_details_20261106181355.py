import pandas as pd

df = pd.read_csv("jobs_informatique_cleaned.csv")

print("=" * 50)
print("DETAILED DATASET ANALYSIS")
print("=" * 50)

# 1. Job sources
print("\n1. Jobs by Source:")
print(df["Source"].value_counts())

# 2. IT Relevance
print("\n2. IT Relevance:")
print(df["IT_Relevance"].value_counts())

# 3. Publication Dates
df["Publication_Date"] = pd.to_datetime(
    df["Publication_Date"],
    errors="coerce"
)

print("\n3. Invalid Publication Dates:")
print(df["Publication_Date"].isna().sum())

print("\n4. Date Range:")
print("Earliest:", df["Publication_Date"].min())
print("Latest:", df["Publication_Date"].max())

# 4. Skills Count
print("\n5. Skills Count Statistics:")
print(df["Skills_Count"].describe())

# 5. Description Length
df["Description_Length"] = df["Description"].astype(str).str.len()

print("\n6. Description Length:")
print(df["Description_Length"].describe())

print("\nDescriptions shorter than 100 characters:")
print((df["Description_Length"] < 100).sum())

# 6. Categories
print("\n7. Top Categories:")
print(df["Categories"].value_counts().head(10))

print("\nDetailed verification completed!")