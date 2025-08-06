
# Credit Card Fraud Detection with Random Forest

This project is a machine learning-based solution to detect fraudulent credit card transactions using the **Random Forest Classifier**. The dataset used is highly imbalanced, mimicking real-world scenarios where fraud is rare but important to detect.

##  Overview

- **Dataset**: [Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud) from Kaggle
- **Goal**: Build and evaluate a model to accurately detect fraudulent transactions
- **Tech Stack**: Python, Pandas, Scikit-learn, Matplotlib, Seaborn

---

##  Dataset Description

The dataset contains transactions made by credit cards in September 2013 by European cardholders. It contains 284,807 transactions, out of which only 492 are fraudulent (about 0.17%).

### Features:

- `Time`, `Amount`: Not anonymized
- `V1` to `V28`: Principal Components (PCA transformed features)
- `Class`: Target variable (0 = valid, 1 = fraud)

---

##  Steps Performed

### 1. **Importing Libraries**


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

### 2. Loading and Exploring Data
Loaded creditcard.csv using pandas

Printed head and described dataset

Observed 0.17% fraud cases, confirming class imbalance

### 3. Analyzing Class Distribution

fraud = data[data['Class'] == 1]
valid = data[data['Class'] == 0]
outlierFraction = len(fraud)/ float(len(valid))
Fraud Cases: 492

Valid Transactions: 284,315

Outlier fraction ≈ 0.00173

### 4. Transaction Amount Analysis
Visual comparison of Amount between fraud and normal transactions using .describe():

Fraudulent transactions tend to have higher average amounts

### 5. Correlation Heatmap
A heatmap was generated to examine feature correlation:

corr_matrix = data.corr()
sns.heatmap(corr_matrix, vmax=0.8, square=True)

### 6. Data Preparation
Features (X) and labels (Y) separated

Split into training/testing sets (80/20)

Checked and handled missing values using SimpleImputer

### 7. Model Training
Model used:

from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier()
rfc.fit(xTrain, yTrain)
### 8. Evaluation
Confusion Matrix

Feature Importance

Classification Report

ROC-AUC Curve

##  Classification Report

              precision    recall  f1-score   support

           0       1.00      1.00      1.00     56864
           1       0.97      0.79      0.87        98

    accuracy                           1.00     56962
   macro avg       0.99      0.89      0.93     56962
weighted avg       1.00      1.00      1.00     56962


## Model Saving
The trained model is saved using pickle:

with open("fraud_model.pkl", "wb") as file:
    pickle.dump(rfc, file)
## Conclusions
Random Forest performs excellently on this dataset with nearly perfect accuracy for normal transactions.

Precision and recall for fraudulent transactions are reasonably high despite the imbalanced data.

ROC-AUC confirms the model's ability to distinguish between classes effectively.

## Requirements

pip install pandas numpy matplotlib seaborn scikit-learn

