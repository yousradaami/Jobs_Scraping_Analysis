
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Clean locations
df["Location"] = (
    df["Location"]
    .fillna("Unknown")
    .astype(str)
    .str.strip()
    .str.replace(r"\s+", " ", regex=True)
)

# Count job offers by location
location_counts = df["Location"].value_counts().head(10)


print("=" * 50)
print("TOP 10 JOB LOCATIONS")
print("=" * 50)

print(location_counts)

# 3. Create bar chart
plt.figure(figsize=(12, 7))

sns.barplot(
    x=location_counts.values,
    y=location_counts.index
)

plt.title("Top 10 Job Locations")
plt.xlabel("Number of Job Offers")
plt.ylabel("Location")

plt.tight_layout()

# 4. Save chart
plt.savefig("top_10_job_locations.png", dpi=300)

# 5. Display chart
plt.show()

print("\nChart saved successfully!")
