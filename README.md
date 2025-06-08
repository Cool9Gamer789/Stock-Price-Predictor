# 📈 Stock Price Prediction using SVR (Support Vector Regression)

This Python script allows users to **predict stock prices** based on historical data using three SVR models:
- **Linear**
- **Polynomial (degree 2)**
- **RBF (Radial Basis Function)**

It visualizes the predictions and returns model-specific forecasts for a user-specified date.

---

## 🔧 Requirements

Before running the script, install the required Python libraries using `pip`:

```bash
pip install numpy scikit-learn matplotlib
```

## ✅ CSV Format
Your CSV file must follow this structure:
```bash
Date,Price
1/2/2014,555.12
1/3/2014,556.89
```
- **Date format must be MM/DD/YYYY**
- **Your CSV file must be placed in the same directory as the main Python script.**

## 📊 How to Generate the CSV using Google Sheets

Use the GOOGLEFINANCE function in Google Sheets to generate daily stock prices.
```bash
=GOOGLEFINANCE("NASDAQ:GOOG", "price", DATE(2014,1,1), DATE(2014,12,31), "DAILY")
```
## ▶️ How to Run
Run the script using Python:
```bash
python main.py
```
When prompted:
```
What is your date?
```
Enter a date in the format: MM/DD/YYYY (e.g. 06/08/2025)
The script will:
- Plot your data and predictions from each model
- Print out the predicted prices for that date
