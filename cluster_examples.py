
import pandas as pd
import os

# =====================================
# 1. Load clustered dataset
# =====================================

INPUT_FILE = "clustering_results/jobs_with_clusters_20.csv"

OUTPUT_DIR = "clustering_results"

df = pd.read_csv(INPUT_FILE)

print("Dataset loaded:", df.shape)

# =====================================
# 2. Extract examples from each cluster
# =====================================

examples = []

for cluster_id in sorted(df["Cluster"].unique()):

    cluster_data = df[df["Cluster"] == cluster_id]

    sample = cluster_data.sample(
        n=min(5, len(cluster_data)),
        random_state=42
    )

    for _, row in sample.iterrows():

        examples.append({
            "Cluster": cluster_id,
            "Job_Title": row.get("Job_Title", ""),
            "Skills": row.get("Skills", "")
        })

# =====================================
# 3. Save examples
# =====================================

examples_df = pd.DataFrame(examples)

output_file = os.path.join(
    OUTPUT_DIR,
    "cluster_examples_20.csv"
)

examples_df.to_csv(output_file, index=False)

# =====================================
# 4. Display results
# =====================================

print("\nCLUSTER EXAMPLES")

for cluster_id in sorted(examples_df["Cluster"].unique()):

    print(f"\n========== CLUSTER {cluster_id} ==========")

    cluster_examples = examples_df[
        examples_df["Cluster"] == cluster_id
    ]

    for _, row in cluster_examples.iterrows():

        print("Job:", row["Job_Title"])
        print("Skills:", row["Skills"])
        print("--------------------------")

print("\nExamples extracted successfully!")
print("Saved in:", output_file)
