import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import streamlit as st


st.title("🫀 Heart Disease Predictor 🩺")
st.subheader("Enter Your Vitals And Check Your Heart Health Instantly!")

df = pd.read_csv("heart.csv")


df = df[["Age", "ChestPainType", "RestingBP", "Cholesterol",
         "FastingBS", "RestingECG", "MaxHR", "ExerciseAngina",
         "Oldpeak", "ST_Slope", "HeartDisease"]].dropna().copy()

df["ChestPainType"] = df["ChestPainType"].map({"ATA": 0, "NAP": 1, "ASY": 2, "TA": 3})
df["RestingECG"] = df["RestingECG"].map({"Normal": 0, "ST": 1, "LVH": 2})
df["ExerciseAngina"] = df["ExerciseAngina"].map({"N": 0, "Y": 1})
df["ST_Slope"] = df["ST_Slope"].map({"Up": 0, "Flat": 1, "Down": 2})

x = df.drop("HeartDisease", axis=1)
y = df["HeartDisease"]

model = DecisionTreeClassifier()
model.fit(x, y)

st.header("📝 Patient Information")

age = st.number_input("Enter Your Age:", min_value=0, max_value=120)
CPT = st.selectbox("Chest Pain Type:", ["ATA", "NAP", "ASY", "TA"])
RBP = st.number_input("Resting Blood Pressure (mm Hg):", min_value=0)
CHL = st.number_input("Cholesterol Level (mg/dL):", min_value=0)
FBS = st.number_input("Fasting Blood Sugar (1 if > 120 mg/dL else 0):", min_value=0, max_value=1)
RECG = st.selectbox("Resting ECG Results:", ["Normal", "ST", "LVH"])
MHR = st.number_input("Maximum Heart Rate Achieved:", min_value=0)
EA = st.selectbox("Chest Pain While Exercising:", ["No", "Yes"])
OP = st.number_input("Old Peak (ST Depression):", step=0.01)
SS = st.selectbox("ST Slope:", ["Up", "Flat", "Down"])

CPT = {"ATA": 0, "NAP": 1, "ASY": 2, "TA": 3}[CPT]
RECG = {"Normal": 0, "ST": 1, "LVH": 2}[RECG]
EA = 1 if EA == "Yes" else 0
SS = {"Up": 0, "Flat": 1, "Down": 2}[SS]

UserData = pd.DataFrame([[age, CPT, RBP, CHL, FBS, RECG, MHR, EA, OP, SS]],
                        columns=["Age", "ChestPainType", "RestingBP", "Cholesterol",
                                 "FastingBS", "RestingECG", "MaxHR", "ExerciseAngina", "Oldpeak", "ST_Slope"])

if st.button("🩺 Predict"):
    prediction = model.predict(UserData)
    
    if prediction[0] == 0:
        st.success("🎉 You are not likely to have heart disease.")
    else:
        st.error("⚠️ Risk of heart disease detected. Please consult a healthcare professional.")
