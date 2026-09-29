# Importing Libraries
import streamlit as st
import pickle
import pandas as pd

# Load the saved model
with open("breast_cancer_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Breast Cancer Prediction")
st.write("Enter the tumour measurements to predict malignant or benign.")

# The 10 selected features from Step 5
features = ['worst concave points', 'worst perimeter', 'mean concave points',
            'worst radius', 'mean perimeter', 'worst area', 'mean radius',
            'mean area', 'mean concavity', 'worst concavity']

# Take user input for each feature
values = []
for feature in features:
    val = st.number_input(feature, min_value=0.0, value=0.0)
    values.append(val)

# Predict on button click
if st.button("Predict"):
    input_df = pd.DataFrame([values], columns=features)
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0].max() * 100
    if prediction == 1:
        st.success(f"Benign (non-cancerous) : {probability:.1f}% confidence")
    else:
        st.error(f"Malignant (cancerous) : {probability:.1f}% confidence")
