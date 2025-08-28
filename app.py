import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('model.sav', 'rb'))

st.title("Student Performance Prediction")
st.write("Enter the details below to predict the student performance.")

# Inputs
Internet_Access_at_Home = st.selectbox(
    "Internet Access at Home:",
    options=["Yes", "No"],
    index=1
)

Study_Hours_per_Week = st.number_input("Study Hours per Week", min_value=0, max_value=90, value=2)
Past_Exam_Scores = st.number_input("Past Exam Scores", min_value=0, max_value=90, value=2)
Final_Exam_Scores = st.number_input("Final Exam Scores", min_value=0, max_value=90, value=2)
Attendance_Rate = st.number_input("Attendance Rate", min_value=0, max_value=100, value=50)

Extracurricular_Activities = st.selectbox(
    "Extracurricular Activities:",
    options=["Yes", "No"],
    index=1
)

parental_education_level = st.selectbox(
    "Parental Education Level",
    options=["High School", "PhD", "Bachelors", "Masters"],
    index=0
)

Gender = st.radio(
    "Gender:",
    options=["Male", "Female"],
    index=0
)

# Encoding categorical values
Parental = {"High School": 1, "PhD": 3, "Bachelors": 0, "Masters": 2}
Internet = {"Yes": 1, "No": 0}
Extracurricular = {"Yes": 1, "No": 0}
gender_map = {"Male": 1, "Female": 0}

features = np.array([[
    Parental[parental_education_level],
    Internet[Internet_Access_at_Home],
    Extracurricular[Extracurricular_Activities],
    gender_map[Gender],
    Study_Hours_per_Week,
    Past_Exam_Scores,
    Final_Exam_Scores,
    Attendance_Rate
]])

# Prediction
if st.button("Result"):
    prediction = model.predict(features)
    if prediction[0] == 1:
        st.success("Result (Pass/Fail): Pass ✅")
    else:
        st.error("Result (Pass/Fail): Fail ❌")