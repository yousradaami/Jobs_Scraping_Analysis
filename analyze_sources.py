import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the dataset
df = pd.read_csv("jobs_informatique_cleaned.csv")

# 2. Check the data
print("=" * 50)
print("DATA VALIDATION")
print("=" * 50)

print("Total job offers:", len(df))
print("Missing sources:", df["Source"].isna().sum())

# 3. Analyze job sources
source_counts = df["Source"].value_counts()

source_percentages = (
    df["Source"].value_counts(normalize=True) * 100
)

print("\nJOB OFFERS BY SOURCE")
print("=" * 50)

for source, count in source_counts.items():
    percentage = source_percentages[source]

    print(f"{source}: {count} jobs ({percentage:.2f}%)")

print("\nTotal:", source_counts.sum())

# 4. Create a bar chart
plt.figure(figsize=(10, 6))

ax = sns.barplot(
    x=source_counts.index,
    y=source_counts.values
)

# Add values and percentages
for i, (count, percentage) in enumerate(
    zip(source_counts.values, source_percentages.values)
):
    ax.text(
        i,
        count + 15,
        f"{count}\n({percentage:.2f}%)",
        ha="center"
    )

plt.title("Number of Job Offers by Source")
plt.xlabel("Job Source")
plt.ylabel("Number of Job Offers")

plt.xticks(rotation=35)
plt.tight_layout()

# 5. Save the chart
plt.savefig("job_sources_analysis.png", dpi=300)

# 6. Display the chart
plt.show()

print("\nChart saved successfully!")