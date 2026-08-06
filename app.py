import streamlit as st
import pandas as pd
import pickle

# Load model
with open("loan_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Loan Approval Prediction")

age = st.number_input("Age", min_value=18, max_value=100, value=25)

income = st.number_input(
    "Monthly Income",
    min_value=1000,
    value=50000
)

employment = st.selectbox(
    "Employment Status",
    ["Employed", "Self-Employed", "Unemployed"]
)

if st.button("Predict"):

    input_data = pd.DataFrame({
        "Age": [age],
        "Income": [income],
        "Employment": [employment]
    })

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1] * 100

    if prediction == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")

    st.write(f"Approval Probability: {probability:.2f}%")