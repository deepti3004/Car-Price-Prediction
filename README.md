# 🚗 Car Price Prediction

A machine learning project that predicts the **selling price of a used car** based on its characteristics. The project includes exploratory data analysis, preprocessing, model comparison, hyperparameter tuning, and a Streamlit web application for making predictions.

## 📌 Project Overview

The goal of this project is to build a machine learning model that can estimate the selling price of a used car.

The project follows a complete machine learning workflow:

**Data Collection → EDA → Data Preprocessing → Feature Engineering → Model Training → Model Evaluation → Hyperparameter Tuning → Model Selection → Deployment**

## 📊 Dataset

The project uses a used-car dataset containing information such as:

* Car Name
* Year
* Selling Price
* Present Price
* Driven Kilometers
* Fuel Type
* Selling Type
* Transmission
* Number of Previous Owners

## 🔍 Exploratory Data Analysis

The dataset was explored using:

* Dataset shape and information
* Descriptive statistics
* Missing-value checking
* Duplicate-value checking
* Unique-value analysis
* Univariate analysis
* Categorical feature analysis
* Scatter plots
* Box plots
* Correlation analysis

Duplicate records were removed during preprocessing.

## ⚙️ Data Preprocessing

The following preprocessing steps were performed:

* Removed duplicate records
* Applied one-hot encoding to categorical features:

  * Fuel Type
  * Transmission
  * Selling Type
* Created a new feature:

  * `Car_Age`
* Removed:

  * `Car_Name`
  * `Driven_kms`
* Split the data into training and testing sets using an 80/20 split.
* Applied `StandardScaler` for models that require feature scaling.

## 🤖 Models Compared

The following regression models were trained and evaluated:

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor
* K-Nearest Neighbors (KNN) Regressor

The models were evaluated using:

* R² Score
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* Mean Absolute Error (MAE)

## 🎯 Hyperparameter Tuning

KNN was selected for further tuning.

Different values of `n_neighbors` from **1 to 20** were tested using the R² score.

The best-performing value was:

```text
n_neighbors = 1
```

The final KNN model was trained using this value.

## 💾 Saved Model

The trained model and scaler were saved using Joblib:

```text
car_price_model.pkl
scaler.pkl
```

These files are used by the Streamlit application to make predictions.

## 🖥️ Streamlit Application

The project includes an interactive Streamlit web application.

Users can enter:

* Year
* Present Price
* Owner
* Selling Type
* Fuel Type
* Transmission

The application calculates the car's age and uses the trained model to estimate its selling price.

The predicted valuation is displayed in **Lakhs**.

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Joblib
* Streamlit
* Jupyter Notebook

## 📁 Project Structure

```text
Car-Price-Prediction/
│
├── app.py
├── car sales.ipynb
├── car_price_model.pkl
├── scaler.pkl
├── requirements.txt
├── README.md
├── car.png
└── car_icon.png
```

## ▶️ Run Locally

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd Car-Price-Prediction
```

### 2. Create and activate a virtual environment

```bash
py -3.12 -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
python -m streamlit run streamlit_app.py
```

## 🌐 Deployment

The application can be deployed using **Streamlit Community Cloud**.

Make sure the GitHub repository contains:

```text
app.py
car_price_model.pkl
scaler.pkl
requirements.txt
```

along with any image assets used by the application.

## 📈 Future Improvements

* Improve model performance through additional feature engineering.
* Experiment with additional regression algorithms.
* Perform more extensive hyperparameter tuning.
* Add prediction confidence or price ranges.
* Improve the deployed application's user experience.
