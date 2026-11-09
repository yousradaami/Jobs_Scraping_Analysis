import pandas as pd

# Load dataset
df = pd.read_csv("jobs_informatique_cleaned.csv")

# Keep original dates
original_dates = df["Publication_Date"].copy()

# Convert dates using mixed format
df["Publication_Date"] = pd.to_datetime(
    df["Publication_Date"],
    format="mixed",
    errors="coerce",
    utc=True
)

# Check results
print("=" * 50)
print("PUBLICATION DATE FIX")
print("=" * 50)

print("\nOriginal dates:", len(original_dates))

print("Valid dates:", df["Publication_Date"].notna().sum())

print("Invalid dates:", df["Publication_Date"].isna().sum())

print("\nDate range:")
print("Earliest:", df["Publication_Date"].min())
print("Latest:", df["Publication_Date"].max())

# Display invalid dates
invalid_dates = original_dates[df["Publication_Date"].isna()]

print("\nInvalid date examples:")
print(invalid_dates.head(20).to_string(index=False))

# Save corrected dataset to a NEW file
df.to_csv("jobs_informatique_dates_fixed.csv", index=False)

print("\nCorrected dataset saved!")