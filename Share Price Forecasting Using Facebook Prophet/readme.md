#  Amazon Stock Price Forecasting with Facebook Prophet

This project explores **time series forecasting** of Amazon (AMZN) stock prices using **Facebook Prophet**.  
The goal is to model historical stock data (2015–2024) and forecast future price trends.  

---

##  Project Overview
- **Dataset**: Amazon stock prices (daily, 2015–2024, downloaded from Kaggle)  
- **Model**: Facebook Prophet (trend + seasonality forecasting)  
- **Tasks**:  
  1. Preprocess stock data  
  2. Train Prophet model  
  3. Forecast test period (for evaluation)  
  4. Forecast into the future (2 years ahead)  
  5. Evaluate using multiple error metrics  

---

##  Results & Performance

Evaluation on test set:  

- **MSE**: 1494.98  
- **MAE**: 32.14  
- **MAPE**: 25.44%  
- **SMAPE**: 28.90%  

 **Interpretation**: Prophet successfully captures the **long-term trend**,  
but struggles with **short-term fluctuations**, which is expected for volatile stock prices.  

---

##  Key Insights
- Prophet is strong in detecting **trend and seasonality**, but short-term stock prediction remains challenging.  
- The model is more suitable for **broad forecasting** than precise daily predictions.  
- Accuracy may improve with:  
  - Hyperparameter tuning  
  - Adding external regressors (volume, indices, macroeconomic data)  
  - Using hybrid models (Prophet + ML/Deep Learning)  

---

##  How to Run

**Clone this repo**  
  
Install dependencies

pip install pandas numpy matplotlib seaborn prophet scikit-learn
Download dataset

Get the Amazon stock dataset from Kaggle

Place the file (e.g., AMZN.csv) in the project root directory

Run the Jupyter Notebook

jupyter notebook Stock_Forecast_AMZN.ipynb
Explore results, plots, and forecasts

 Future Work
Parameter tuning (changepoint_prior_scale, seasonality_prior_scale)

Incorporating regressors like trading volume, NASDAQ index

Exploring hybrid ML approaches (e.g., Prophet + XGBoost/LSTM)
