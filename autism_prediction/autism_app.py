
# app.py

import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load the trained models and scaler
with open('all_models.pkl', 'rb') as f:
    trained_models = pickle.load(f)

scaler = pickle.load(open('scaler.pkl', 'rb'))  # Assuming you saved it separately

# Streamlit App Title
st.title('🧠 Autism Spectrum Disorder (ASD) Prediction App')
st.markdown('Select a model, fill the information, and predict ASD!')

# Model Selection
model_choice = st.selectbox(
    'Choose the Model for Prediction:',
    ('Logistic Regression', 'XGBoost', 'Support Vector Machine')
)

# Map selection to model key
model_map = {
    'Logistic Regression': 'logistic_regression',
    'XGBoost': 'xgboost',
    'Support Vector Machine': 'svc_rbf'
}

selected_model = trained_models[model_map[model_choice]]

# Form layout
with st.form("autism_form"):
    st.subheader("Fill the Required Information:")

    col1, col2 = st.columns(2)

    with col1:
        A1_Score = st.selectbox('A1 Score', [0, 1])
        A2_Score = st.selectbox('A2 Score', [0, 1])
        A3_Score = st.selectbox('A3 Score', [0, 1])
        A4_Score = st.selectbox('A4 Score', [0, 1])
        A5_Score = st.selectbox('A5 Score', [0, 1])

    with col2:
        A6_Score = st.selectbox('A6 Score', [0, 1])
        A7_Score = st.selectbox('A7 Score', [0, 1])
        A8_Score = st.selectbox('A8 Score', [0, 1])
        A9_Score = st.selectbox('A9 Score', [0, 1])
        A10_Score = st.selectbox('A10 Score', [0, 1])

    age = st.number_input('Age (Years)', min_value=1, max_value=100)
    jaundice = st.selectbox('History of Jaundice (0: No, 1: Yes)', [0, 1])
    family_history = st.selectbox('Family History of ASD (0: No, 1: Yes)', [0, 1])
    result = st.number_input('Screening Test Result', min_value=-10.0, max_value=30.0, step=1.0)

    submitted = st.form_submit_button("Predict")

# On Predict
if submitted:
    # Calculate additional features
    sum_score = A1_Score + A2_Score + A3_Score + A4_Score + A5_Score + A6_Score + A7_Score + A8_Score + A9_Score + A10_Score
    ind = jaundice + family_history  # No 'used_app_before' in form, so just these two

    # Create input data in the exact format used for training
    input_data = pd.DataFrame({
        'A1_Score': [A1_Score],
        'A2_Score': [A2_Score],
        'A3_Score': [A3_Score],
        'A4_Score': [A4_Score],
        'A5_Score': [A5_Score],
        'A6_Score': [A6_Score],
        'A7_Score': [A7_Score],
        'A8_Score': [A8_Score],
        'A9_Score': [A9_Score],
        'A10_Score': [A10_Score],
        'age': [np.log(age)],           # Log transformation
        'jaundice': [jaundice],
        'result': [result],
        'sum_score': [sum_score],
        'ind': [ind]
    })

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Predict
    prediction = selected_model.predict(input_scaled)[0]

    # Display result
    st.subheader("Prediction Result:")
    if prediction == 1:
        st.error(f"⚠️ Based on {model_choice}, the person is **Positive for ASD**.")
    else:
        st.success(f"✅ Based on {model_choice}, the person is **Negative for ASD**.")
