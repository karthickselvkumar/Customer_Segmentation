 # **Customer Segmentation Project**

## **Overview**
This project performs **customer segmentation** using **KMeans clustering** to categorize customers based on demographic information, spending behavior, and website interactions. It helps businesses understand customer behavior and target marketing campaigns effectively.

---

## **Notebook Highlights (`analysis_model.ipynb`)**
- **Data Cleaning & Preprocessing:** Handled missing values, created features like `age`, `total_children`, `total_spending`, and `customer_since`.
- **Exploratory Data Analysis (EDA):** Visualized age, income, total spending, and campaign acceptance patterns.
- **Feature Engineering:** Aggregated campaign responses into a single `accepted` column and created `age_groups`.
- **Clustering:** Scaled features and applied **KMeans clustering** to segment customers into 6 clusters.
- **PCA Visualization:** Reduced dimensions to 2D for cluster visualization.
- **Model Saving:** Saved `KMeans` and `StandardScaler` models using `joblib` for future predictions.

---

## **Streamlit App (`segmentation.py`)**
- **Interactive Interface:** Users can input customer details such as age, income, total spending, web/store purchases, website visits, and recency.
- **Prediction:** Inputs are scaled using the saved `StandardScaler`, and clusters are predicted using the trained `KMeans` model.
- **User Feedback:** Shows predicted cluster along with a brief description of its characteristics.
- **Ease of Use:** Simple web interface for non-technical users to quickly classify customers.

---

## **Impact**
- Enables businesses to **identify high-value customers** and optimize marketing strategies.
- Provides a **ready-to-deploy solution** for customer segmentation using Python, Pandas, Scikit-learn, and Streamlit.

