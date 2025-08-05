
import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler

# Load model and scaler
model = joblib.load("rainfall_model.pkl")
scaler = joblib.load("scaler.pkl")

st.set_page_config(page_title="Rainfall Prediction App", layout="centered")

st.title("🌧️ Rainfall Prediction App")
st.write("This app predicts **whether it will rain today or not** based on atmospheric data.")

# Input form
with st.form("rainfall_form"):
    pressure = st.number_input("Pressure", min_value=900.0, max_value=1100.0, step=0.1)
    temperature = st.number_input("Temperature", min_value=0.0, max_value=50.0, step=0.1)
    dewpoint = st.number_input("Dew Point", min_value=0.0, max_value=50.0, step=0.1)
    humidity = st.slider("Humidity (%)", 0, 100, 50)
    cloud = st.slider("Cloud Cover (%)", 0, 100, 50)
    sunshine = st.number_input("Sunshine (hours)", 0.0, 15.0, step=0.1)
    winddirection = st.number_input("Wind Direction", 0.0, 360.0, step=1.0)
    windspeed = st.number_input("Wind Speed", 0.0, 100.0, step=0.1)

    submit = st.form_submit_button("Predict")

if submit:
    input_data = np.array([[pressure, temperature, dewpoint, humidity, cloud, sunshine, winddirection, windspeed]])
    scaled_data = scaler.transform(input_data)
    prediction = model.predict(scaled_data)

    if prediction[0] == 1:
        st.success("☔ Yes, it may rain today!")
    else:
        st.info("🌤️ No, it likely won't rain today.")
