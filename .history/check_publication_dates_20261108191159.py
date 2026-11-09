```python
import pandas as pd

# =====================================
# 1. Load dataset
# =====================================

FILE = "jobs_informatique_cleaned.csv"

df = pd.read_csv(FILE)

print("=" * 50)
print("PUBLICATION DATE CHECK")
print("=" * 50)

# =====================================
# 2. Total rows and missing dates
# =====================================

print("\nTotal rows:")
print(len(df))

print("\nMissing dates:")
print(df["Publication_Date"].isna().sum())

# =====================================
# 3. Convert dates
# =====================================

df["Publication_Date"] = pd.to_datetime(
    df["Publication_Date"],
    format="mixed",
    errors="coerce",
    utc=True
)

print("\nValid dates:")
print(df["Publication_Date"].notna().sum())

print("\nInvalid dates:")
print(df["Publication_Date"].isna().sum())

# =====================================
# 4. Date examples
# =====================================

print("\nDate examples:")
print(df["Publication_Date"].head(20).to_string())

# =====================================
# 5. Earliest and latest dates
# =====================================

print("\nEarliest date:")
print(df["Publication_Date"].min())

print("\nLatest date:")
print(df["Publication_Date"].max())

# =====================================
# 6. Original invalid date values
# =====================================

df_original = pd.read_csv(FILE)

df_converted = pd.to_datetime(
    df_original["Publication_Date"],
    format="mixed",
    errors="coerce",
    utc=True
)

invalid_dates = df_original.loc[
    df_converted.isna(),
    "Publication_Date"
]

print("\nExamples of invalid dates:")
print(invalid_dates.head(30).to_string(index=False))

# =====================================
# 7. Most common invalid dates
# =====================================

print("\nMost common invalid date values:")
print(invalid_dates.value_counts().head(15).to_string())

# =====================================
# 8. Final summary
# =====================================

print("\n" + "=" * 50)
print("DATE CHECK COMPLETED")
print("=" * 50)

print("Total rows:", len(df))
print("Valid dates:", df["Publication_Date"].notna().sum())
print("Invalid dates:", df["Publication_Date"].isna().sum())
