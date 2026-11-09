```python
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
