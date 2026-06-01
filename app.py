import streamlit as st
import pickle
import numpy as np

# Load model and scaler
model = pickle.load(open("disease_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.title("Disease Prediction System")

st.write("Enter Patient Details")

# Manual Input Fields
pregnancies = st.text_input("Pregnancies")
glucose = st.text_input("Glucose")
bp = st.text_input("Blood Pressure")
skin = st.text_input("Skin Thickness")
insulin = st.text_input("Insulin")
bmi = st.text_input("BMI")
dpf = st.text_input("Diabetes Pedigree Function")
age = st.text_input("Age")

if st.button("Predict"):

    try:
        # Convert inputs to float
        data = np.array([[float(pregnancies),
                          float(glucose),
                          float(bp),
                          float(skin),
                          float(insulin),
                          float(bmi),
                          float(dpf),
                          float(age)]])

        # Scale data
        data = scaler.transform(data)

        # Prediction
        prediction = model.predict(data)

        if prediction[0] == 1:
            st.error("High Chance of Diabetes")
        else:
            st.success("Low Chance of Diabetes")

    except:
        st.warning("Please enter valid numeric values")
