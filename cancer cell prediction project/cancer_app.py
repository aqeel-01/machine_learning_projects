
import pickle
import streamlit as st
import numpy as np
from sklearn.datasets import load_breast_cancer

# Load dataset (for default input values)
data = load_breast_cancer()

# Load the pre-trained model
with open("cancer_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Breast Cancer Prediction")
st.write("Enter the values for the features to get a prediction.")

feature_names = data.feature_names  # safer than hardcoding

user_input = []
for i, feature in enumerate(feature_names):
    val = st.number_input(
        f"{feature}",
        min_value=0.0,
        value=float(np.mean(data.data[:, i]))  
    )
    user_input.append(val)

if st.button("Predict"):
    input_array = np.array(user_input).reshape(1, -1)
    prediction = model.predict(input_array)[0]
    result = "Malignant" if prediction == 0 else "Benign"
    st.success(f"Prediction: {result}")

