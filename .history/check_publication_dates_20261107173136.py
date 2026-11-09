
import pandas as pd

# Load dataset
df = pd.read_csv("jobs_informatique_cleaned.csv")

print("=" * 50)
print("PUBLICATION DATE CHECK")
print("=" * 50)

print("\nTotal rows:")
print(len(df))

print("\nMissing dates:")
print(df["Publication_Date"].isna().sum())

# Convert dates
df["Publication_Date"] = pd.to_datetime(
    df["Publication_Date"],
    errors="coerce",
    utc=True
)

print("\nValid dates:")
print(df["Publication_Date"].notna().sum())

print("\nInvalid dates:")
print(df["Publication_Date"].isna().sum())

print("\nDate examples:")
print(df["Publication_Date"].head(20).to_string())

print("\nEarliest date:")
print(df["Publication_Date"].min())

print("\nLatest date:")
print(df["Publication_Date"].max())

```python
# Show original invalid date values
df_original = pd.read_csv("jobs_informatique_cleaned.csv")

df_converted = pd.to_datetime(
    df_original["Publication_Date"],
    errors="coerce",
    utc=True
)

invalid_dates = df_original.loc[
    df_converted.isna(),
    "Publication_Date"
]

print("\nExamples of invalid dates:")
print(invalid_dates.head(30).to_string(index=False))

print("\nMost common invalid date values:")
print(invalid_dates.value_counts().head(15).to_string())
