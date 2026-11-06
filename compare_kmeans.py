
import pandas as pd
import matplotlib.pyplot as plt
import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# ==========================================
# 1. LOAD CLEANED DATASET
# ==========================================

INPUT_FILE = "jobs_informatique_cleaned.csv"
OUTPUT_FOLDER = "clustering_comparison"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

df = pd.read_csv(INPUT_FILE)

print("=" * 60)
print("       K-MEANS CLUSTERING COMPARISON")
print("=" * 60)

print("\nDataset loaded successfully!")
print("Number of jobs:", len(df))
print("Number of columns:", len(df.columns))

# ==========================================
# 2. PREPARE TEXT DATA
# ==========================================

df["Job_Title"] = df["Job_Title"].fillna("").astype(str)
df["Skills"] = df["Skills"].fillna("").astype(str)

# Remove the placeholder from clustering text
skills = df["Skills"].replace("Not specified", "")

df["Text"] = df["Job_Title"] + " " + skills

# ==========================================
# 3. TF-IDF VECTORIZATION
# ==========================================

print("\nApplying TF-IDF...")

vectorizer = TfidfVectorizer(
    stop_words="english",
    max_features=3000,
    min_df=2,
    ngram_range=(1, 2)
)

X = vectorizer.fit_transform(df["Text"])

terms = vectorizer.get_feature_names_out()

print("TF-IDF matrix shape:", X.shape)

# ==========================================
# 4. COMPARE K = 10, 15, 20
# ==========================================

k_values = [10, 15, 20]

comparison_results = []

for k in k_values:

    print("\n" + "=" * 50)
    print(f"PROCESSING K = {k}")
    print("=" * 50)

    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    labels = model.fit_predict(X)

    # Silhouette Score
    score = silhouette_score(X, labels)

    # Inertia
    inertia = model.inertia_

    print("Silhouette Score:", round(score, 5))
    print("Inertia:", round(inertia, 3))

    comparison_results.append({
        "K": k,
        "Silhouette_Score": score,
        "Inertia": inertia
    })

    # ======================================
    # 5. CLUSTER COUNTS
    # ======================================

    counts = pd.Series(labels).value_counts().sort_index()

    counts_df = pd.DataFrame({
        "Cluster": counts.index,
        "Number_of_Jobs": counts.values,
        "Percentage": (
            counts.values / len(df) * 100
        ).round(2)
    })

    counts_df.to_csv(
        f"{OUTPUT_FOLDER}/cluster_counts_K{k}.csv",
        index=False
    )

    # ======================================
    # 6. CLUSTER PROFILES
    # ======================================

    profiles = []

    for cluster_id in range(k):

        center = model.cluster_centers_[cluster_id]

        top_indices = center.argsort()[-10:][::-1]

        top_words = [
            terms[i] for i in top_indices
        ]

        profiles.append({
            "Cluster": cluster_id,
            "Number_of_Jobs": int(counts.get(cluster_id, 0)),
            "Top_Keywords": ", ".join(top_words)
        })

    profiles_df = pd.DataFrame(profiles)

    profiles_df.to_csv(
        f"{OUTPUT_FOLDER}/cluster_profiles_K{k}.csv",
        index=False
    )

    # ======================================
    # 7. SAVE JOBS WITH CLUSTER LABELS
    # ======================================

    result_df = df.copy()
    result_df["Cluster"] = labels

    result_df.drop(columns=["Text"]).to_csv(
        f"{OUTPUT_FOLDER}/jobs_with_clusters_K{k}.csv",
        index=False,
        encoding="utf-8-sig"
    )

    print(f"Files for K={k} saved successfully!")

# ==========================================
# 8. FINAL COMPARISON TABLE
# ==========================================

comparison_df = pd.DataFrame(comparison_results)

comparison_df["Silhouette_Score"] = (
    comparison_df["Silhouette_Score"].round(6)
)

comparison_df["Inertia"] = (
    comparison_df["Inertia"].round(3)
)

comparison_df.to_csv(
    f"{OUTPUT_FOLDER}/kmeans_final_comparison.csv",
    index=False
)

print("\n" + "=" * 60)
print("FINAL COMPARISON")
print("=" * 60)

print(comparison_df.to_string(index=False))

# ==========================================
# 9. SILHOUETTE COMPARISON GRAPH
# ==========================================

plt.figure(figsize=(9, 5))

plt.plot(
    comparison_df["K"],
    comparison_df["Silhouette_Score"],
    marker="o",
    linewidth=2
)

plt.title("K-Means Silhouette Score Comparison")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Silhouette Score")

plt.xticks(k_values)
plt.grid(True)

plt.savefig(
    f"{OUTPUT_FOLDER}/silhouette_comparison.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

# ==========================================
# 10. INERTIA COMPARISON GRAPH
# ==========================================

plt.figure(figsize=(9, 5))

plt.plot(
    comparison_df["K"],
    comparison_df["Inertia"],
    marker="o",
    linewidth=2
)

plt.title("K-Means Inertia Comparison")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia")

plt.xticks(k_values)
plt.grid(True)

plt.savefig(
    f"{OUTPUT_FOLDER}/inertia_comparison.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

# ==========================================
# 11. BEST SILHOUETTE RESULT
# ==========================================

best_row = comparison_df.loc[
    comparison_df["Silhouette_Score"].idxmax()
]

print("\nBEST SILHOUETTE RESULT")
print("Best K:", int(best_row["K"]))
print("Best Score:", best_row["Silhouette_Score"])

print("\n" + "=" * 60)
print("ALL OPERATIONS COMPLETED SUCCESSFULLY!")
print("Results folder:", OUTPUT_FOLDER)
print("=" * 60)
