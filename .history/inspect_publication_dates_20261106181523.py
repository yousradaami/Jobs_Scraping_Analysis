import pandas as pd

df = pd.read_csv("jobs_informatique_cleaned.csv")

print("=" * 50)
print("PUBLICATION DATE INSPECTION")
print("=" * 50)

print("\n1. Original Publication Date Examples:")

print(df["Publication_Date"].head(30).to_string(index=False))

print("\n2. Unique Date Formats / Examples:")

print(df["Publication_Date"].sample(30, random_state=42).to_string(index=False))

print("\n3. Missing or Empty Dates:")

print("Missing:", df["Publication_Date"].isnull().sum())

print("Empty strings:", (df["Publication_Date"].astype(str).str.strip() == "").sum())

print("\n4. Skills_Count = 0:")

print((df["Skills_Count"] == 0).sum())

print("\n5. Jobs requiring review:")

review_jobs = df[df["IT_Relevance"] == "Needs review"]

print(review_jobs[["Job_Title", "Company", "Source", "IT_Relevance"]].to_string(index=False))

print("\nInspection completed!")