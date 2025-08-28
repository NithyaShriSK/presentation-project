import streamlit as st
import pickle
import numpy as np



model = pickle.load(open('model.sav', 'rb'))


st.title("Student Performance")

st.write("Enter the details below to predict the student performance.")
#Gender,Study_Hours_per_Week,Attendance_Rate,Past_Exam_Scores,Parental_Education_Level
# Internet_Access_at_Home,Extracurricular_Activities,Final_Exam_Score,Pass_Fail

import streamlit as st
import numpy as np

# Dropdown for Education Level (example categories)
Internet_Access_at_Home = st.selectbox(
    "Tnternat_Access_at_Home:",
    options=["Yes", "No"],
    index=1
)

# Numeric input for Experience
Study_Hours_per_Week= st.number_input("Study_Hours_per_Week", min_value=0, max_value=90, value=2)
Past_Exam_Scores= st.number_input("Past_Exam_Scores", min_value=0, max_value=90, value=2)
Final_Exam_Scores= st.number_input("Final_Exam_Scores", min_value=0, max_value=90, value=2)
Attendance_Rate= st.number_input("Attendance_Rate", min_value=0, max_value=90, value=2)

Extracurricular_Activities = st.selectbox(
    "Extracurricular_Activities:",
    options=["Yes", "No"],
    index=1
)

# Dropdown for Job Title
parental_education_level = st.selectbox(
    "Parental Education Level",
    options=["High School","PhD","Bachelors","Masters"],
    index=0
)

# Dropdown for Gender
Gender = st.radio(
    "Gender:",
    options=["Male", "Female","Other"],
    index=0
)

# --- Encoding categorical values ---
Parental= {"High School":1,"PhD":3,"Bachelors":0,"Masters":2}
Internet= {"Yes":1,"No":0}
Extracurricular= {"Yes":1,"No":0}
gender_map = {"Male": 1, "Female": 0,"Other":2}

features = np.array([[
    Parental[parental_education_level],
    Internet[Internet_Access_at_Home],
    Extracurricular[Extracurricular_Activities],
    gender_map[Gender],
    Study_Hours_per_Week,Past_Exam_Scores,Final_Exam_Scores,Attendance_Rate
]])


if st.button("Result"):
    prediction = model.predict(features)
    st.success(f"Result(Pass/Fail): {prediction[0]:,.2f}")
    
    