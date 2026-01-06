import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# 1. Create Synthetic Data (For Demonstration)
# In a real project, you would load this from a CSV file (e.g., pd.read_csv('heart.csv'))
data = {
    'Age': [25, 30, 45, 50, 60, 35, 65, 55, 40, 70, 22, 48, 52, 58, 62],
    'Cholesterol': [150, 180, 240, 260, 300, 190, 310, 270, 200, 320, 140, 250, 265, 290, 305],
    'Blood_Pressure': [110, 120, 140, 150, 160, 120, 165, 155, 130, 170, 110, 145, 148, 158, 162],
    'Heart_Disease': [0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1]  # 0: Healthy, 1: At Risk
}

df = pd.DataFrame(data)

# 2. Split Data and Train Model
X = df[['Age', 'Cholesterol', 'Blood_Pressure']]
y = df['Heart_Disease']

# Using Logistic Regression (Good for binary classification)
model = LogisticRegression()
model.fit(X, y)

# 3. Streamlit Web App Interface
st.set_page_config(page_title="Heart Health AI", page_icon="❤️")

st.title("❤️ AI Heart Disease Prediction System")
st.write("""
This app predicts the **probability of heart disease** based on patient data.
*Note: This utilizes a machine learning model for educational purposes.*
""")
st.write("---")

# Sidebar for User Inputs
st.sidebar.header("Patient Input Features")

def user_input_features():
    # Sliders for input (Min, Max, Default)
    age = st.sidebar.slider('Age', 18, 100, 30)
    cholesterol = st.sidebar.slider('Cholesterol Level (mg/dL)', 100, 400, 180)
    bp = st.sidebar.slider('Blood Pressure (mm Hg)', 90, 200, 120)
    
    # Store inputs in a dictionary
    data = {'Age': age,
            'Cholesterol': cholesterol,
            'Blood_Pressure': bp}
    features = pd.DataFrame(data, index=[0])
    return features

# Get input from sidebar
input_df = user_input_features()

# Display the user inputs
st.subheader('Patient Details:')
st.write(input_df)

# 4. Prediction Logic
if st.button('Predict Health Status'):
    # Make prediction
    prediction = model.predict(input_df)
    probability = model.predict_proba(input_df)
    
    st.subheader('Prediction Result:')
    
    if prediction[0] == 1:
        st.error("⚠️ **High Risk:** The model detects a potential risk of heart disease.")
        st.write("Please consult a cardiologist for further checkups.")
    else:
        st.success("✅ **Low Risk:** The heart seems healthy.")
        st.write("Keep maintaining a healthy lifestyle!")
        
    # Show confidence score
    confidence = probability[0][prediction[0]] * 100
    st.info(f"Model Confidence: **{confidence:.2f}%**")

st.markdown("---")
st.caption("Disclaimer: This is a demo project using synthetic data. Do not use for actual medical diagnosis.")