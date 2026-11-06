

import os
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# ==========================================
# 1. Configuration
# ==========================================

DATA_FILE = "jobs_informatique_validated_skills.csv"
OUTPUT_DIR = "clustering_results"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ==========================================
# 2. Load dataset
# ==========================================

print("Loading dataset...")

df = pd.read_csv(DATA_FILE)

print("Dataset shape:", df.shape)

# ==========================================
# 3. Prepare text data
# ==========================================

df["Job_Title"] = df["Job_Title"].fillna("")
df["Skills"] = df["Skills"].fillna("")

text_data = df["Job_Title"] + " " + df["Skills"]

# ==========================================
# 4. TF-IDF Vectorization
# Keep previous settings
# ==========================================

print("\nApplying TF-IDF...")

vectorizer = TfidfVectorizer(
    stop_words="english",
    max_features=3000,
    min_df=2,
    ngram_range=(1, 2)
)

X = vectorizer.fit_transform(text_data)

print("TF-IDF matrix shape:", X.shape)

# ==========================================
# 5. Test K from 2 to 20
# ==========================================

results = []

print("\nTesting K values from 2 to 20...\n")

for k in range(2, 21):

    print(f"Testing K = {k}...")

    kmeans = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    labels = kmeans.fit_predict(X)

    score = silhouette_score(X, labels)

    inertia = kmeans.inertia_

    results.append({
        "K": k,
        "Silhouette_Score": score,
        "Inertia": inertia
    })

    print(f"K = {k} | Silhouette Score = {score:.4f}")
    print(f"Inertia = {inertia:.2f}\n")

# ==========================================
# 6. Save comparison results
# ==========================================

results_df = pd.DataFrame(results)

results_path = os.path.join(
    OUTPUT_DIR,
    "k_comparison.csv"
)

results_df.to_csv(results_path, index=False)

# ==========================================
# 7. Find best K
# ==========================================

best_result = results_df.loc[
    results_df["Silhouette_Score"].idxmax()
]

print("===================================")
print("BEST CLUSTERING RESULT")
print("===================================")

print("Best K:", int(best_result["K"]))

print(
    "Best Silhouette Score:",
    round(best_result["Silhouette_Score"], 4)
)

# ==========================================
# 8. Plot Silhouette Scores
# ==========================================

plt.figure(figsize=(11, 6))

plt.plot(
    results_df["K"],
    results_df["Silhouette_Score"],
    marker="o",
    linewidth=2
)

plt.xticks(range(2, 21))
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Silhouette Score")
plt.title("Silhouette Score Comparison (K = 2 to 20)")
plt.grid(True, alpha=0.3)

plt.savefig(
    os.path.join(OUTPUT_DIR, "k_comparison.png"),
    dpi=300,
    bbox_inches="tight"
)

plt.close()

# ==========================================
# 9. Plot Elbow Method
# ==========================================

plt.figure(figsize=(11, 6))

plt.plot(
    results_df["K"],
    results_df["Inertia"],
    marker="o",
    linewidth=2
)

plt.xticks(range(2, 21))
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia")
plt.title("Elbow Method (K = 2 to 20)")
plt.grid(True, alpha=0.3)

plt.savefig(
    os.path.join(OUTPUT_DIR, "elbow_method.png"),
    dpi=300,
    bbox_inches="tight"
)

plt.close()

# ==========================================
# 10. Display final results
# ==========================================

print("\n========== ALL RESULTS ==========")
print(results_df.to_string(index=False))

print("\nClustering comparison completed successfully!")

print("Results saved in:", OUTPUT_DIR)
print("- k_comparison.csv")
print("- k_comparison.png")
print("- elbow_method.png")
