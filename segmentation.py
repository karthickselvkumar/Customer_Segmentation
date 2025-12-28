import streamlit as st
import pandas as pd
import joblib

# Load models
kmeans = joblib.load("kmean_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("CUSTOMER SEGMENTATION")
st.subheader("Enter the details to predict the segmentation")

# Input fields
age = st.number_input('AGE', min_value=18, max_value=75, value=30)
income = st.number_input("INCOME", min_value=0, max_value=200000, value=50000)
total_spending = st.number_input("TOTAL SPENDING", min_value=0, max_value=500000, value=1000)
num_web_purchases = st.number_input("TOTAL WEB PURCHASES", min_value=0, max_value=500, value=5)
num_store_purchases = st.number_input("TOTAL STORE PURCHASES", min_value=0, max_value=500, value=5)
num_web_visits_month = st.number_input("NO OF WEBSITE VISITS PER MONTH", min_value=0, max_value=100, value=10)
recency = st.number_input("RECENCY", min_value=0, max_value=500, value=30)

# Create input dataframe - Keys now match your list exactly
input_data = pd.DataFrame({
    'age': [age],
    'Income': [income],
    'total_spending': [total_spending],
    'NumWebPurchases': [num_web_purchases],
    'NumStorePurchases': [num_store_purchases],
    'NumWebVisitsMonth': [num_web_visits_month],
    'Recency': [recency]
})

# Scaling and Prediction
if st.button("Predict Segment"):
    try:
        # Scale the input using the loaded scaler
        input_scaled = scaler.transform(input_data)
        
        # Predict using the loaded KMeans model
        cluster = kmeans.predict(input_scaled)[0]
        
        # UI Feedback
        st.divider()
        st.success(f"### Predicted Segment: **Cluster {cluster}**")
        
        # Optional: Add a brief description or visual
        st.info(f"This customer belongs to group {cluster} based on their spending and browsing habits.")
        
    except ValueError as e:
        st.error("Column Mismatch Error")
        st.write("The scaler expects specific features. Ensure the order and names match your training set.")
        st.exception(e)