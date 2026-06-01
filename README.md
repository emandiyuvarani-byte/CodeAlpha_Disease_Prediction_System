# Disease Prediction System Using Machine Learning

## 📌 Overview

This project was developed as part of the **CodeAlpha Internship Program**. The objective of this project is to predict the likelihood of diabetes based on patient health information using Machine Learning techniques. The system uses a trained **Random Forest Classifier** and provides predictions through a user-friendly **Streamlit web application**.

---

## 🚀 Features

* Disease Prediction using Machine Learning
* Diabetes Risk Analysis
* Streamlit Web Interface
* User Input-Based Prediction
* Feature Scaling with StandardScaler
* Random Forest Classification Model
* Real-Time Prediction Results
* Model and Scaler Serialization using Pickle

---

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Streamlit
* Random Forest Classifier
* Pickle

---

## 📂 Dataset Information

The dataset contains medical information used for diabetes prediction.

### Features Used

* Pregnancies
* Glucose
* Blood Pressure
* Skin Thickness
* Insulin
* BMI
* Diabetes Pedigree Function
* Age

### Target Variable

* Diabetes Status

  * Tested Negative = 0
  * Tested Positive = 1

---

## 🧠 Machine Learning Workflow

### Step 1: Load Dataset

The diabetes dataset is loaded using Pandas.

### Step 2: Data Preprocessing

* Clean column names
* Convert target labels into numerical values
* Separate input and output variables

### Step 3: Train-Test Split

Dataset is divided into:

* Training Data: 80%
* Testing Data: 20%

### Step 4: Feature Scaling

StandardScaler is applied to normalize input features.

### Step 5: Model Training

A Random Forest Classifier with 200 estimators is trained on the dataset.

### Step 6: Model Evaluation

Model performance is evaluated using Accuracy Score.

### Step 7: Save Model

The trained model and scaler are saved as:

```text
disease_model.pkl
scaler.pkl
```

### Step 8: Deploy with Streamlit

A web application is created using Streamlit where users can enter patient details and receive disease predictions instantly.

---

## 📊 Results

### Model Performance

* Accuracy: **73.38%**

### Prediction Output

* High Chance of Diabetes
* Low Chance of Diabetes

The system successfully predicts diabetes risk based on patient medical information.

---

## 🖥 Application Interface

The Streamlit application accepts:

* Pregnancies
* Glucose
* Blood Pressure
* Skin Thickness
* Insulin
* BMI
* Diabetes Pedigree Function
* Age

After entering values and clicking **Predict**, the system displays the prediction result.

---

## 🎯 Applications

* Healthcare Monitoring
* Early Disease Detection
* Clinical Decision Support
* Medical Data Analysis
* Patient Risk Assessment

---

## 📁 Project Structure

```text
Disease-Prediction-System/
│
├── app.py
├── model.py
├── disease_model.pkl
├── scaler.pkl
├── csv_result-diabetes.csv
├── README.md
└── screenshots/
```

---

## 🎓 Learning Outcomes

Through this project, I learned:

* Data Preprocessing
* Feature Scaling
* Random Forest Classification
* Model Serialization
* Streamlit Deployment
* Healthcare Analytics
* Machine Learning Workflow

---

## ✅ Conclusion

This project successfully implemented a Disease Prediction System using Machine Learning. The Random Forest model achieved an accuracy of approximately **73.38%** and was integrated with a Streamlit web application for real-time predictions. The project demonstrates how Machine Learning can be applied in healthcare to support disease risk assessment and early diagnosis.

---

## 👩‍💻 Author

**Emandi Yuvarani**

### Internship

**CodeAlpha Internship Program**
