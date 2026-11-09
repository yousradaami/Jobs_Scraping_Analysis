import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the dataset
df = pd.read_csv("jobs_informatique_cleaned.csv")

# 2. Analyze job sources
source_counts = df["Source"].value_counts()

print("=" * 50)
print("JOB OFFERS BY SOURCE")
print("=" * 50)

print(source_counts)

# 3. Calculate percentages
source_percentages = df["Source"].value_counts(normalize=True) * 100

print("\nPERCENTAGE BY SOURCE")
print("=" * 50)

print(source_percentages.round(2))

# 4. Create a bar chart
plt.figure(figsize=(10, 6))

sns.barplot(
    x=source_counts.index,
    y=source_counts.values
)

plt.title("Number of Job Offers by Source")
plt.xlabel("Job Source")
plt.ylabel("Number of Job Offers")

plt.xticks(rotation=45)

plt.tight_layout()

# 5. Save the chart
plt.savefig("job_sources_analysis.png", dpi=300)

# 6. Display the chart
plt.show()

print("\nChart saved successfully!")
