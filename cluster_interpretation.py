
import os
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# ==========================================
# 1. Configuration
# ==========================================

DATA_FILE = "jobs_informatique_validated_skills.csv"
OUTPUT_DIR = "clustering_results"

K = 20

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ==========================================
# 2. Load dataset
# ==========================================

print("Loading dataset...")

df = pd.read_csv(DATA_FILE)

df["Job_Title"] = df["Job_Title"].fillna("")
df["Skills"] = df["Skills"].fillna("")

text_data = df["Job_Title"] + " " + df["Skills"]

print("Number of jobs:", len(df))

# ==========================================
# 3. TF-IDF
# Same settings as previous experiment
# ==========================================

print("\nApplying TF-IDF...")

vectorizer = TfidfVectorizer(
    stop_words="english",
    max_features=3000,
    min_df=2,
    ngram_range=(1, 2)
)

X = vectorizer.fit_transform(text_data)

feature_names = vectorizer.get_feature_names_out()

print("TF-IDF shape:", X.shape)

# ==========================================
# 4. K-Means with K=20
# ==========================================

print("\nApplying K-Means...")

kmeans = KMeans(
    n_clusters=K,
    random_state=42,
    n_init=10
)

df["Cluster"] = kmeans.fit_predict(X)

# ==========================================
# 5. Cluster distribution
# ==========================================

cluster_counts = (
    df["Cluster"]
    .value_counts()
    .sort_index()
    .reset_index()
)

cluster_counts.columns = ["Cluster", "Number_of_Jobs"]

cluster_counts["Percentage"] = (
    cluster_counts["Number_of_Jobs"] / len(df) * 100
).round(2)

cluster_counts.to_csv(
    os.path.join(OUTPUT_DIR, "cluster_counts_20.csv"),
    index=False
)

# ==========================================
# 6. Extract top keywords
# ==========================================

print("\nExtracting top keywords...")

profiles = []

for cluster_id in range(K):

    center = kmeans.cluster_centers_[cluster_id]

    top_indices = center.argsort()[-10:][::-1]

    top_words = [
        feature_names[i] for i in top_indices
    ]

    profiles.append({
        "Cluster": cluster_id,
        "Number_of_Jobs": int(
            (df["Cluster"] == cluster_id).sum()
        ),
        "Top_Keywords": ", ".join(top_words)
    })

    print(f"\nCluster {cluster_id}:")
    print("Jobs:", (df["Cluster"] == cluster_id).sum())
    print("Keywords:", ", ".join(top_words))

profiles_df = pd.DataFrame(profiles)

profiles_df.to_csv(
    os.path.join(OUTPUT_DIR, "cluster_profiles_20.csv"),
    index=False
)

# ==========================================
# 7. Save classified jobs
# ==========================================

df.to_csv(
    os.path.join(OUTPUT_DIR, "jobs_with_clusters_20.csv"),
    index=False
)

# ==========================================
# 8. Final message
# ==========================================

print("\n================================")
print("CLUSTER INTERPRETATION COMPLETED")
print("================================")

print("\nCluster distribution:")
print(cluster_counts.to_string(index=False))

print("\nFiles saved in:", OUTPUT_DIR)
print("- cluster_counts_20.csv")
print("- cluster_profiles_20.csv")
print("- jobs_with_clusters_20.csv")
