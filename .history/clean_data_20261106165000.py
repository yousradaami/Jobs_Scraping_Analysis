
import pandas as pd
import os

# 1. Load original dataset
input_file = "jobs_informatique_validated_skills.csv"
output_file = "jobs_informatique_cleaned.csv"

df = pd.read_csv(input_file)

print("BEFORE CLEANING")
print("Rows:", len(df))

# 2. Clean text formatting
text_columns = df.select_dtypes(
    include=["object", "string"]
).columns

for col in text_columns:
    df[col] = (
        df[col]
        .astype("string")
        .str.strip()
        .str.replace(r"\s+", " ", regex=True)
    )

# 3. Handle missing Job_ID
missing_ids = df["Job_ID"].isna()

existing_ids = set(df["Job_ID"].dropna().astype(str))

counter = 1

for index in df[missing_ids].index:
    while f"GENERATED_{counter:04d}" in existing_ids:
        counter += 1

    new_id = f"GENERATED_{counter:04d}"

    df.at[index, "Job_ID"] = new_id
    existing_ids.add(new_id)
    counter += 1

# 4. Handle missing Location
df["Location"] = df["Location"].fillna("Unknown")

# 5. Handle missing Skills
df["Skills"] = df["Skills"].fillna("Not specified")

# 6. Save cleaned dataset
df.to_csv(output_file, index=False, encoding="utf-8-sig")

# 7. Validate cleaned dataset
print("\nAFTER CLEANING")
print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\nMissing values:")
print(df.isna().sum())

print("\nEmpty values:")
for col in ["Job_ID", "Location", "Skills"]:
    empty = df[col].fillna("").astype(str).str.strip().eq("").sum()
    print(f"{col}: {empty}")

print("\nDuplicate rows:", df.duplicated().sum())
print("Duplicate URLs:", df["Job_URL"].dropna().duplicated().sum())
print("Duplicate Job_ID:", df["Job_ID"].duplicated().sum())

print("\nCleaned dataset saved successfully!")
print("File:", output_file)
