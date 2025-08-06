# 🌧️ Rainfall Prediction Project

A machine learning-powered web application that predicts **whether it will rain today** based on real-world meteorological data. Built using Python, Scikit‑learn, XGBoost, and Streamlit.

---

## 📌 Table of Contents

- [Overview](#overview)  
- [Dataset](#dataset)  
- [Project Pipeline](#project-pipeline)  
- [Model Performance](#model-performance)  
- [App Demo](#app-demo)  
- [Screenshots](#screenshots)  
- [How to Run Locally](#how-to-run-locally)  
- [Project Structure](#project-structure)  
- [Dependencies](#dependencies)  
- [License](#license)

---

## 📖 Overview

This project explores a rainfall dataset with the goal of classifying days into **rainy** or **non-rainy**. It includes:

- Data cleaning and preprocessing  
- Exploratory Data Analysis (EDA)  
- Feature selection & correlation analysis  
- Model training and evaluation (Logistic Regression, XGBoost, SVM)  
- Deployment via a simple Streamlit web application

---

## 📊 Dataset

- File: `Rainfall.csv`  
- Records: 366 days of weather data  
- Features include:  
  - Pressure, Temperature, Dew Point  
  - Humidity, Cloud Cover, Sunshine  
  - Wind Direction, Wind Speed  
  - Rainfall (`yes` / `no`)

---

## 🔁 Project Pipeline

1. **Import & Inspect Data**  
   - Clean column names  
   - Handle missing values (mean imputation)  

2. **EDA & Visualization**  
   - Distribution plots, boxplots  
   - Rainfall ratio (Pie chart)  
   - Correlation heatmap  

3. **Data Preprocessing**  
   - Convert categorical `rainfall` to binary  
   - Drop redundant features (`maxtemp`, `mintemp`)  
   - Balance imbalanced classes using `RandomOverSampler`  
   - Normalize features using `StandardScaler`  

4. **Modeling**  
   - Logistic Regression  
   - XGBoost Classifier  
   - Support Vector Classifier (SVC)  

5. **Evaluation**  
   - ROC-AUC scores  
   - Confusion matrix  
   - Classification report  

6. **Deployment**  
   - Save best model (`LogisticRegression`)  
   - Build interactive UI using Streamlit  

---

## ✅ Model Performance

| Model               | Training ROC-AUC | Validation ROC-AUC |
|--------------------|------------------|---------------------|
| Logistic Regression | 0.889            | 0.896               |
| XGBoost             | 1.000            | 0.839               |
| SVC (RBF kernel)    | 0.903            | 0.886               |

🔍 **Logistic Regression** was selected due to balanced performance on both training and validation data.

---

## 🚀 App Demo

Experience the app live in your browser:

[**☁️ Live Rainfall Prediction Demo**](https://machinelearningprojects-4wqpwslbgksmpjwjlzo8vb.streamlit.app/)

---

## 🖼️ Screenshots

### ☀️ No Rain Predicted
<img src="screenshots/no_rain_prediction.png" alt="No Rain Prediction" width="600"/>

### 🌧️ Rain Predicted
<img src="screenshots/rain_prediction.png" alt="Rain Prediction" width="600"/>

---

## 💻 How to Run Locally

1. **Clone the repository**
    ```bash
    git clone https://github.com/yourusername/rainfall-prediction-app.git
    cd rainfall-prediction-app
    ```

2. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3. **Ensure model files are present**
    - `rainfall_model.pkl`
    - `scaler.pkl`

4. **Run the Streamlit app**
    ```bash
    streamlit run app.py
    ```

---

## 📁 Project Structure

rainfall-prediction-app/
├── Rainfall.csv
├── rainfall_model.pkl
├── scaler.pkl
├── app.py
├── screenshots/
│ ├── no_rain_prediction.png
│ └── rain_prediction.png
├── README.md
└── requirements.txt



---

## 🧩 Dependencies

- numpy  
- pandas  
- matplotlib  
- seaborn  
- scikit-learn  
- xgboost  
- imbalanced-learn  
- joblib  
- streamlit  

Install all with:
```bash
pip install -r requirements.txt

