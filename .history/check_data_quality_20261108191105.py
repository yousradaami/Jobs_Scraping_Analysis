
import pandas as pd
import os

# =====================================
# 1. Load dataset
# =====================================

FILE = "jobs_informatique_validated_skills.csv"
OUTPUT_FOLDER = "data_quality_results"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

df = pd.read_csv(FILE)

print("=" * 55)
print("        DATA QUALITY CHECK")
print("=" * 55)

# =====================================
# 2. General information
# =====================================

print("\n1. GENERAL INFORMATION")
print("-" * 40)

print("Number of rows:", len(df))
print("Number of columns:", len(df.columns))
print("\nColumns:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

# =====================================
# 3. Missing values
# =====================================

print("\n2. MISSING VALUES")
print("-" * 40)

missing = pd.DataFrame({
    "Column": df.columns,
    "Missing_Values": df.isnull().sum().values,
    "Missing_Percentage": (
        df.isnull().mean().values * 100
    ).round(2)
})

print(missing.to_string(index=False))

missing.to_csv(
    f"{OUTPUT_FOLDER}/missing_values.csv",
    index=False
)

# =====================================
# 4. Empty text values
# =====================================

print("\n3. EMPTY TEXT VALUES")
print("-" * 40)

text_columns = df.select_dtypes(
    include=["object", "string"]
).columns

empty_results = []

for col in text_columns:
    empty_count = (
        df[col].fillna("").astype(str).str.strip().eq("")
    ).sum()

    empty_results.append({
        "Column": col,
        "Empty_Values": empty_count
    })

empty_df = pd.DataFrame(empty_results)

print(empty_df.to_string(index=False))

empty_df.to_csv(
    f"{OUTPUT_FOLDER}/empty_values.csv",
    index=False
)

# =====================================
# 5. Duplicate rows
# =====================================

print("\n4. DUPLICATE ROWS")
print("-" * 40)

duplicate_rows = df.duplicated().sum()

print("Exact duplicate rows:", duplicate_rows)

# =====================================
```python
# =====================================
# 6. Duplicate URLs
# =====================================

print("\n5. DUPLICATE URLS")
print("-" * 40)

if "Job_URL" in df.columns:
    valid_urls = (
        df["Job_URL"]
        .dropna()
        .astype(str)
        .str.strip()
    )

    valid_urls = valid_urls[valid_urls != ""]

    # Normalize URLs for comparison
    normalized_urls = valid_urls.str.lower()

    duplicate_urls = normalized_urls.duplicated().sum()

    print("Duplicate URLs:", duplicate_urls)

else:
    duplicate_urls = None
    print("Job_URL column not found.")


# =====================================
# 7. Text formatting
# =====================================

print("\n6. TEXT FORMATTING")
print("-" * 40)

format_results = []

for col in text_columns:
    values = df[col].dropna().astype(str)

    leading_trailing = (
        values != values.str.strip()
    ).sum()

    repeated_spaces = (
        values.str.contains(r"\s{2,}", regex=True)
    ).sum()

    format_results.append({
        "Column": col,
        "Leading_or_Trailing_Spaces": leading_trailing,
        "Repeated_Spaces": repeated_spaces
    })

format_df = pd.DataFrame(format_results)

print(format_df.to_string(index=False))

format_df.to_csv(
    f"{OUTPUT_FOLDER}/text_formatting.csv",
    index=False
)

# =====================================
# 8. Important columns check
# =====================================

print("\n7. IMPORTANT COLUMNS")
print("-" * 40)

for col in ["Job_Title", "Skills"]:
    if col in df.columns:
        empty = (
            df[col].fillna("").astype(str).str.strip().eq("")
        ).sum()

        print(f"{col}: {empty} empty values")

# =====================================
# 9. Final summary
# =====================================

print("\n8. FINAL SUMMARY")
print("-" * 40)

print("Total jobs:", len(df))
print("Total columns:", len(df.columns))
print("Exact duplicate rows:", duplicate_rows)
print("Duplicate URLs:", duplicate_urls)

print("\nMissing values by column:")
print(missing[["Column", "Missing_Values"]].to_string(index=False))

print("\nDiagnostic files saved in:", OUTPUT_FOLDER)

print("\nDATA QUALITY CHECK COMPLETED!")
