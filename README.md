# Breast Cancer Prediction Project

Predicts whether a breast tumour is malignant or benign using machine learning.

GitHub URL : https://github.com/harekrishna10/breast-cancer-prediction

Streamlit Web app Live Demo : https://breast-cancer-prediction-10.streamlit.app/

## Dataset

- `breast_cancer.csv` — 569 rows, 30 tumour measurements + target column
- Target: 0 = malignant, 1 = benign

## Steps

1. Loaded the dataset and inspected it
2. Data cleaning — checked duplicates and missing values
3. Data preparation — split into features (X) and target (y)
4. EDA — target distribution, feature histograms, correlation heatmap
5. Feature selection — kept the top 10 most correlated features
6. Model building — Logistic Regression, Random Forest, Decision Tree algorithm used for finding the best model.
7. Final pipeline — StandardScaler + Logistic Regression, tuned with GridSearchCV (Best C = 10, test accuracy 0.9825), saved as `breast_cancer_model.pkl`
8. Streamlit web app (`app.py`) for live predictions

## Model Results

![Model Comparison](model_comparison.png)

Final tuned model test accuracy: **0.9912**

## How to Run

1. Install packages: `pip install -r requirements.txt`
2. Open `breast_cancer.ipynb` and run all cells
3. Creat new Terminal
4. Start the app: `streamlit run app.py`

## Adding to GitHub

1. git init
2. git add .
3. git commit -m "Breast cancer prediction project"
4. git branch -M main
5. git remote add origin https://github.com/harekrishna10/breast-cancer-prediction.git
6. git push -u origin main

## Adding to Streamlit web app

1. go to https://share.streamlit.io/
2. click on New app
3. Select the github account or sign up with github account
4. Deploy app form will appear
5. In Repo : choose harekrishna10/breast-cancer-prediction
6. In Branch : choose main
7. In Main file path : choose app.py
8. In App URL : give desired url for you live streamlit web app like: breast-cancer-prediction-10
9. click on Deploy button
