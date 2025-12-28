Customer Segmentation Project Summary

Overview:
This project performs customer segmentation using KMeans clustering to categorize customers based on their demographic information, spending patterns, and website interactions. It helps businesses understand customer behavior and target campaigns more effectively.

Notebook Highlights (analysis_model.ipynb):

Data Cleaning & Preprocessing: Handling missing values, creating new features like age, total_children, total_spending, and customer_since.

Exploratory Data Analysis (EDA): Visualizations for age, income, total spending, and campaign acceptance patterns.

Feature Engineering: Aggregating campaign responses into a single accepted column, creating age_groups.

Clustering: Scaling features and applying KMeans clustering to segment customers into 6 groups.

PCA Visualization: Reducing dimensions to 2D for visualizing cluster distribution.

Model Saving: Saved KMeans and StandardScaler models using joblib for reuse.

Streamlit App (segmentation.py):

Interactive Interface: Users can input customer details like age, income, spending, web/store purchases, website visits, and recency.

Prediction: Inputs are scaled using the saved StandardScaler, and the cluster is predicted using the trained KMeans model.

User Feedback: Shows predicted segment along with a brief description of the cluster’s characteristics.

Ease of Use: Simple web interface for non-technical users to quickly classify customers.

Impact:

Allows businesses to identify high-value customers, tailor marketing campaigns, and optimize resource allocation.

Provides a ready-to-deploy solution for customer segmentation using Python, Pandas, Scikit-learn, and Streamlit.
