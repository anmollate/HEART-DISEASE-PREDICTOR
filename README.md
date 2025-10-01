# Heart Disease Predictor

## Project Description
This project is a machine learning application that predicts the likelihood of heart disease in a patient based on medical parameters like age, blood pressure, cholesterol, chest pain type, and more. The prediction is made using a Decision Tree Classifier built with scikit-learn, and the app is deployed using Streamlit for an interactive user interface.

## Features
- Predicts the risk of heart disease based on input parameters.
- Interactive web app using Streamlit.
- Clean and user-friendly interface.
- Can handle single patient input via form.

## Dataset
The model is trained on a dataset containing patient health metrics. Features used for prediction include:
- Age  
- ChestPainType  
- RestingBP  
- Cholesterol  
- FastingBS  
- RestingECG *(if available)*  
- ExerciseAngina *(if available)*  
- MaxHR  
- Oldpeak  
- ST_Slope  
- HeartDisease  

## Installation / Setup
Clone the repository and install dependencies:

```bash
# Clone the repository
git clone https://github.com/yourusername/heart-disease-predictor.git
cd heart-disease-predictor

# Create a virtual environment (optional but recommended)
python -m venv venv

# Activate the environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
