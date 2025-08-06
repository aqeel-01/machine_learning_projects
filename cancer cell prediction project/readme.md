

#  Breast Cancer Prediction App

A **Streamlit** web application that uses a **Naive Bayes classifier** to predict whether a breast tumor is **malignant** (cancerous) or **benign** (non-cancerous) based on the input features from the **Breast Cancer Wisconsin Dataset**.

---

##  Project Structure

cancer-cell-prediction-project/
├── cancer_app.py                     # Streamlit web app for cancer prediction
├── cancer_model.pkl                  # Trained Gaussian Naive Bayes model
├── cancer_cell_classification.ipynb # Jupyter Notebook with data analysis, model training, evaluation
├── README.md                         # Project documentation


---

##  Dataset

- **Source:** `sklearn.datasets.load_breast_cancer`
- **Samples:** 569
- **Features:** 30
- **Target Classes:** 
  - `0`: Malignant (Cancerous)
  - `1`: Benign (Non-cancerous)

---

##  Features Used

Includes 30 numeric features like:
- `mean radius`, `mean texture`, `mean perimeter`, `mean area`
- `worst smoothness`, `worst concavity`, `mean fractal dimension`, etc.

---

##  Model Details

- **Algorithm:** Gaussian Naive Bayes
- **Train/Test Split:** 70% training, 30% testing
- **Accuracy:** ~94%

---

##  How It Works

1. User enters values for each of the 30 features via input fields.
2. The app loads the pre-trained Naive Bayes model (`cancer_model.pkl`).
3. The model makes a prediction.
4. Output is shown as:
   -  **Benign** or
   -  **Malignant**

---

## How to Run the App

### 1. Install Requirements

pip install streamlit scikit-learn matplotlib pandas numpy


2. Run the App

streamlit run cancer_app.py
