# Rainfall Prediction Project

This is a machine learning web application that predicts whether it will rain today based on atmospheric data. It includes model training, evaluation, and deployment using Streamlit.

## Table of Contents

- [Overview](#overview)  
- [Dataset](#dataset)  
- [Project Pipeline](#project-pipeline)  
- [Model Performance](#model-performance)  
- [Live Demo](#live-demo)  
- [Screenshots](#screenshots)  
- [How to Run Locally](#how-to-run-locally)  
- [Project Structure](#project-structure)  
- [Dependencies](#dependencies)  
- [License](#license)

## Overview

This project uses weather features such as temperature, humidity, pressure, and wind to classify whether rainfall will occur. The dataset is preprocessed, visualized, and modeled using multiple classifiers. The best-performing model is deployed via a Streamlit web app.

## Dataset

- File: `Rainfall.csv`  
- Total records: 366  
- Features include:
  - Pressure, Temperature, Dew Point  
  - Humidity, Cloud Cover, Sunshine  
  - Wind Direction, Wind Speed  
  - Target: Rainfall (`yes` / `no`)

## Project Pipeline

1. Load and clean data (fix column names, handle missing values)
2. Perform exploratory data analysis (distribution, boxplots, correlation)
3. Convert categorical target to binary
4. Drop redundant features
5. Handle class imbalance using oversampling
6. Normalize features using StandardScaler
7. Train multiple models (Logistic Regression, XGBoost, SVC)
8. Evaluate and compare model performance
9. Save the best model and scaler
10. Deploy using Streamlit

## Model Performance

| Model               | Training ROC-AUC | Validation ROC-AUC |
|--------------------|------------------|---------------------|
| Logistic Regression | 0.889            | 0.896               |
| XGBoost             | 1.000            | 0.839               |
| SVC (RBF kernel)    | 0.903            | 0.886               |

The Logistic Regression model was selected for deployment due to its strong and balanced performance.

## Live Demo

You can access the deployed application here:  
[https://machinelearningprojects-4wqpwslbgksmpjwjlzo8vb.streamlit.app/](https://machinelearningprojects-4wqpwslbgksmpjwjlzo8vb.streamlit.app/)

## Screenshots

### No Rain Predicted

![No Rain](screenshots/no%20rain.PNG)

### Rain Predicted

![Rain](screenshots/yes%20rain.PNG)

## How to Run Locally

1. Clone the repository:

```bash
git clone https://github.com/yourusername/rainfall-prediction-app.git
cd rainfall-prediction-app

2. Install dependencies:
 pip install -r requirements.txt

3. Ensure model files are in place:
   rainfall_model.pkl
   scaler.pkl
4. Run the Streamlit app:
    streamlit run rainfall_pred_app.py


Project Structure
rainfall-prediction-app/
├── Rainfall.csv
├── rainfall_model.pkl
├── scaler.pkl
├── rainfall_pred_app.py
├── screenshots/
│   ├── no rain.png
│   └── yes rain.png
├── README.md
└── requirements.txt


