## Disease Prediction Using Ensemble Machine Learning
This project predicts diseases based on patient symptoms using machine learning models like Random Forest, Naive Bayes, and SVM. Final predictions are made via majority voting to improve robustness.

## Dataset
Filename: improved_disease_dataset.csv

Samples: 2,000

## Features:

Symptoms: fever, headache, nausea, vomiting, fatigue, joint_pain, skin_rash, cough, weight_loss, yellow_eyes

Target: disease (encoded using LabelEncoder)

## Installation

pip install numpy pandas matplotlib seaborn scikit-learn imbalanced-learn

##  Project Workflow

Step 1: Data Preprocessing
Loaded the dataset using pandas.

Encoded target variable (disease) using LabelEncoder.

 Step 2: Handling Class Imbalance
 Applied RandomOverSampler from imblearn to balance disease distribution.

Step 3: Cross-Validation
Performed 5-fold Stratified K-Fold Cross-Validation on 4 models:

Model	Mean Accuracy
Decision Tree	53.89%
Random Forest	54.36%
Naive Bayes	32.25%
SVM	50.00%

Step 4: Evaluation on Test Data

Random Forest

Accuracy: 53.51%
F1 Score: 0.5239

Naive Bayes

Accuracy: 16.23%
F1 Score: 0.1713

SVM

Accuracy: 48.98%
F1 Score: 0.4834

All models were evaluated using accuracy, F1 score, and confusion matrices.

Step 5: Ensemble Voting Classifier

Combined predictions from all models using mode() for majority voting.

Combined Accuracy: 48.83%
Combined F1 Score: 0.4810

Step 6: Disease Prediction from Symptoms

Function predict_disease() takes comma-separated symptoms and returns predicted diseases from each model + final majority vote.

Example:

predict_disease("fever, headache, skin_rash")

Sample Output:
{
  'Random Forest Prediction': 'Tuberculosis',
  'Naive Bayes Prediction': 'Urinary tract infection',
  'SVM Prediction': 'Peptic ulcer disease',
  'Final Prediction (Majority Vote)': 'Tuberculosis'
}

##  Features Used for Prediction

fever
headache
nausea
vomiting
fatigue
joint_pain
skin_rash
cough
weight_loss
yellow_eyes

## How to Run

Install required libraries:

pip install numpy pandas matplotlib seaborn scikit-learn imbalanced-learn
