import pandas as pd

# Load the cleaned dataset
file_path = "jobs_informatique_cleaned.csv"

df = pd.read_csv(file_path)

print("=" * 50)
print("DATASET VERIFICATION")
print("=" * 50)

# 1. Dataset size
print("\n1. Dataset Shape:")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# 2. Column names
print("\n2. Columns:")
print(df.columns.tolist())

# 3. Missing values
print("\n3. Missing Values:")
print(df.isnull().sum())

# 4. Duplicate rows
print("\n4. Duplicate Rows:")
print(df.duplicated().sum())

# 5. Duplicate Job IDs
if "Job_ID" in df.columns:
    print("\n5. Duplicate Job IDs:")
    print(df["Job_ID"].duplicated().sum())

# 6. Duplicate URLs
if "Job_URL" in df.columns:
    print("\n6. Duplicate Job URLs:")
    print(df["Job_URL"].duplicated().sum())

# 7. Data sources
if "Data_Source" in df.columns:
    print("\n7. Jobs by Data Source:")
    print(df["Data_Source"].value_counts())

# 8. Save report
df.isnull().sum().to_csv("missing_values_report.csv")

print("\nVerification completed!")