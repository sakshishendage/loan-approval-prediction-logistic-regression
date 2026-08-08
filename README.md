# 🏦 Loan Approval Prediction using Logistic Regression

A Machine Learning project that predicts whether a loan application will be **Approved or Rejected** using **Logistic Regression**.

## 📌 Project Overview

This project uses applicant information such as **Age, Income, and Employment Status** to predict loan approval.

The trained Logistic Regression model is saved as `loan_model.pkl` and integrated with a **Streamlit web application** for real-time predictions.

## 🚀 Features

* 🤖 Logistic Regression classification
* 📊 Loan approval prediction
* 🧹 Data preprocessing and model training
* 💾 Saved trained model using Pickle
* 🌐 Interactive Streamlit web application
* ⚡ Real-time predictions

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Pickle
* Streamlit

## 📂 Project Structure

```text
loan-approval-prediction-logistic-regression/
│
├── app.py              # Streamlit application
├── train_model.py      # Model training code
├── loan_model.pkl      # Trained ML model
├── README.md           # Project documentation
```

##  Machine Learning

### Algorithm

**Logistic Regression**

Logistic Regression is a supervised Machine Learning classification algorithm used to predict categorical outcomes.

### Input Features

* Age
* Income
* Employment Status

### Output

* ✅ Loan Approved
* ❌ Loan Rejected

  

## ⚙️ **Installation**

Clone the repository:

```bash
git clone https://github.com/sakshishendage/loan-approval-prediction-logistic-regression.git
```

Navigate to the project folder:

```bash
cd loan-approval-prediction-logistic-regression
```

Install the required libraries:

```bash
pip install pandas numpy scikit-learn streamlit
```

## ▶️ Run the Application

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

## 🔄 How It Works

```text
User Input
    ↓
Age / Income / Employment Status
    ↓
Machine Learning Model
    ↓
Logistic Regression
    ↓
Loan Approval Prediction
    ↓
Approved / Rejected
```

##  Model Workflow

1. Load and prepare the dataset.
2. Select the required features.
3. Split the data into training and testing sets.
4. Train the Logistic Regression model.
5. Evaluate the model.
6. Save the trained model as `loan_model.pkl`.
7. Load the model in the Streamlit application.
8. Generate loan approval predictions.

##  Model File

`loan_model.pkl` contains the trained Logistic Regression model. It is loaded by `app.py` to generate predictions without retraining the model every time.

##  Objective

To develop a Machine Learning-based loan approval prediction system using Logistic Regression and provide an interactive interface for generating real-time predictions.

##  Educational Purpose

This project is developed for **educational and learning purposes** to understand the fundamentals of Machine Learning classification, Logistic Regression, model training, and deployment using Streamlit.

It demonstrates how a trained Machine Learning model can be integrated into a simple web application to make predictions.

##  Instructions

1. Install the required Python libraries.
2. Make sure `loan_model.pkl` is present in the project folder.
3. Run the application using:

```bash
streamlit run app.py
```

4. Enter the applicant's **Age, Income, and Employment Status**.
5. Click the prediction button.
6. View the predicted loan approval result.

To retrain the model:

```bash
python train_model.py
```

---

