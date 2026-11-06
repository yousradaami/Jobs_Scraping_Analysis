# Global IT Job Market Analysis

## 1. Project Overview

This project aims to analyze the global job market in the Information Technology (IT) field, with a particular focus on remote job opportunities.

The study is based on collecting, cleaning, preprocessing, analyzing, and visualizing job advertisements from several international recruitment platforms.

A dataset containing **2,000 real job advertisements** was collected for this project.

## 2. Project Objectives

The main objectives of this project are:

- Collect real IT job advertisements from multiple websites.
- Build a dataset containing at least 2,000 job advertisements.
- Clean and preprocess the collected data.
- Identify the most in-demand IT skills.
- Analyze job titles and IT job categories.
- Study the geographical distribution of job opportunities.
- Apply Machine Learning algorithms to group similar job advertisements.
- Visualize and interpret the results.

## 3. Data Sources

The dataset was collected from the following platforms:

- Himalayas
- We Work Remotely
- Remote OK
- Remotive

**Total number of collected job advertisements: 2,000.**

## 4. Technologies and Libraries

The project uses the following technologies and Python libraries:

- Python
- Requests
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- TF-IDF
- K-Means Clustering

## 5. Web Scraping

Web scraping was performed using Python scripts to collect job advertisements from different international recruitment platforms.

The collected information includes:

- Job ID
- Job Title
- Company
- Location
- Publication Date
- Categories
- Required Skills
- Job Description
- Job URL
- Application URL
- Data Source

The collected data was stored in CSV format for further processing and analysis.

## 6. Data Cleaning and Preprocessing

Several data cleaning operations were performed to improve dataset quality:

- Detection and treatment of missing values.
- Generation of new IDs for advertisements with missing identifiers.
- Replacement of missing locations with "Unknown".
- Replacement of missing skills with "Not specified".
- Detection and verification of duplicate records.
- Correction of text formatting and extra spaces.
- Text preprocessing for further analysis.

The cleaned dataset is stored in:

`jobs_informatique_cleaned.csv`

### Data Quality Results

- Total records: 2,000
- Missing values after cleaning: 0
- Duplicate rows: 0
- Duplicate URLs: 0
- Duplicate Job IDs: 0

## 7. Data Analysis and Machine Learning

The project focuses on analyzing several aspects of the global IT job market.

### 7.1 Skills Analysis

Identifying the most frequently requested technical skills in IT job advertisements, such as:

- React
- JavaScript
- TypeScript
- Python
- API
- CSS
- Git
- CI/CD

### 7.2 Job Titles Analysis

Analyzing job titles to identify the most common IT positions and professional categories.

### 7.3 Location Analysis

Studying the geographical distribution of IT job opportunities across different countries.

### 7.4 Machine Learning: K-Means Clustering

The K-Means algorithm is applied to group similar job advertisements based on their textual characteristics.

TF-IDF (Term Frequency–Inverse Document Frequency) is used to transform textual data into numerical features.

Three different values of K are compared:

- K = 10
- K = 15
- K = 20

The clustering performance is evaluated using:

- Silhouette Score
- Inertia

The final model selection will be based on both evaluation metrics and the interpretation of the resulting clusters.

## 8. Project Progress

- [x] Web scraping and data collection.
- [x] Creation of a dataset containing 2,000 job advertisements.
- [x] Data quality assessment.
- [x] Data cleaning and preprocessing.
- [x] Initial analysis of skills, job titles, and locations.
- [x] TF-IDF text representation.
- [x] Application of K-Means clustering.
- [x] Comparison of K = 10, K = 15, and K = 20.
- [ ] Final interpretation of clusters and model selection.
- [ ] Completion of data analysis.
- [ ] Final data visualizations.
- [ ] Completion of the final report.

## 9. Project Structure

The project contains Python scripts, datasets, and analysis results.

Main files include:

- `scraping_jobs.py` – Collects job advertisements.
- `check_data_quality.py` – Checks dataset quality.
- `clean_data.py` – Cleans the dataset.
- `compare_kmeans.py` – Compares different K-Means configurations.
- `jobs_informatique_cleaned.csv` – Cleaned dataset.
- `clustering_comparison/` – Contains clustering comparison results.

Additional scripts and output files are included in the project repository.

## 10. Installation and Execution

### Requirements

- Python 3
- Visual Studio Code or another Python IDE.

### Install the required libraries

```bash
pip install pandas numpy requests scikit-learn matplotlib
```

### Run the scripts

Execute the scripts from the project directory:

```bash
python scraping_jobs.py
python check_data_quality.py
python clean_data.py
python compare_kmeans.py
```

The analysis and visualization scripts can then be executed according to the project workflow.

## 11. Conclusion

This project provides an overview of the global IT job market using real job advertisements collected from multiple international platforms.

It aims to identify in-demand technical skills, analyze job opportunities across different countries, and discover groups of similar IT positions using Machine Learning techniques.

The final findings and visualizations will provide a better understanding of current trends in the global IT employment market.

---

**Academic Data Analysis Project**

**Topic:** Global IT Job Market Analysis, with a Focus on Remote Jobs.