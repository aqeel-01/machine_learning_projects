##  Autism Spectrum Disorder (ASD) Prediction App

This project is a Machine Learning-powered web application built using **Streamlit** that predicts whether a person is likely to have Autism Spectrum Disorder (ASD) based on their responses to behavioral and medical questions.

##  Project Overview

The goal of this project is to:
- Explore and clean ASD screening data.
- Train classification models to predict ASD.
- Build a user-friendly web app using **Streamlit** for public interaction.

---

##  Dataset

The dataset used is based on ASD screening responses and demographic details. Key features include:

- 10 behavioral screening scores: `A1_Score` to `A10_Score` (binary: 0 or 1)
- `Age` (log-transformed for normalization)
- Medical history: `Jaundice`, `Family History of ASD`
- Screening test result: `result`
- Target variable: `Class/ASD` (1 = Positive, 0 = Negative)

The original dataset had 800 records and 22 columns.

---

##  Data Preprocessing & Feature Engineering

- Missing values and ambiguous categories (e.g., "?") replaced with `"Others"`.
- Categorical variables encoded using **Label Encoding**.
- Added features:
  - `sum_score`: Total score from A1 to A10
  - `ind`: Sum of binary indicators (`jaundice`, `used_app_before`, `austim`)
- Applied **log transformation** on age to remove skewness.
- Balanced the dataset using **RandomOverSampler** (from `imblearn`) due to class imbalance.
- Feature scaling performed using **StandardScaler**.

---

##  Model Training

Three models were trained using **scikit-learn** and **XGBoost**:

| Model                 | Training ROC AUC | Validation ROC AUC |
|----------------------|------------------|---------------------|
| Logistic Regression  | 0.865            | 0.774               |
| XGBoost Classifier   | 1.000            | 0.745               |
| SVM (RBF Kernel)     | 0.920            | 0.796               |

Trained models and the scaler were saved as:
- `all_models.pkl`
- `scaler.pkl`

---

##  Web App (Streamlit)

The app allows users to select a model and enter the required information to receive an ASD prediction.

### Features:
- Model selection: Logistic Regression, XGBoost, SVM
- Inputs: Scores A1–A10, Age, Jaundice History, Family History, Screening Result
- Output: Prediction (Positive or Negative for ASD)

### How to Run:

1. Clone the repository or copy the code.
2. Ensure required libraries are installed:
   ```bash
   pip install streamlit numpy pandas scikit-learn xgboost imbalanced-learn

3. streamlit run autism_app.py

## Screenshot

Below is a sample output for a negative ASD prediction:

![ASD Negative Prediction](screenshots/autism_neg.png)

## File Structure

```text
autism_predictor/
│
├── autism_app.py             # Streamlit application
├── autism_prediction.ipynb   # EDA and model training notebook
├── all_models.pkl            # Serialized machine learning models
├── scaler.pkl                # StandardScaler object for input features
├── train.csv                 # Dataset used for training and analysis
├── README.md                 # Project documentation (this file)
├── screenshots/
│   └── autism_neg.png        # Screenshot showing a negative ASD prediction

