import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 1. Create Synthetic Dataset (For Demo Purpose)
# In a real project, we load data using: df = pd.read_csv('crop_data.csv')
data = {
    'Rainfall': [100, 200, 150, 120, 300, 50, 250, 180, 130, 220],       # mm
    'Temperature': [25, 30, 28, 26, 35, 40, 29, 27, 26, 31],            # Celsius
    'Fertilizer': [50, 70, 60, 55, 80, 20, 75, 65, 58, 72],             # kg/acre
    'Yield_Tons': [2.5, 4.0, 3.2, 2.8, 5.5, 1.2, 5.0, 3.8, 3.0, 4.5]    # Output (Tons)
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

print("--- Sample Training Data ---")
print(df.head())
print("----------------------------")

# 2. Split Data into Features (X) and Target (y)
X = df[['Rainfall', 'Temperature', 'Fertilizer']]  # Input features
y = df['Yield_Tons']                               # Target variable

# Split into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Initialize and Train the Model
model = LinearRegression()

print("Training the model...")
model.fit(X_train, y_train)
print("Model Trained Successfully!")

# 4. Prediction Function
def predict_yield():
    print("\n--- Crop Yield Prediction System ---")
    try:
        # Taking input from user
        rain = float(input("Enter Rainfall (mm): "))
        temp = float(input("Enter Temperature (°C): "))
        fert = float(input("Enter Fertilizer (kg/acre): "))
        
        # Prepare input for prediction
        features = np.array([[rain, temp, fert]])
        
        # Make prediction
        prediction = model.predict(features)
        
        print(f"\nEstimated Yield: {prediction[0]:.2f} Tons per acre")
    except ValueError:
        print("Error: Please enter valid numeric values.")

# Run the function
if __name__ == "__main__":
    predict_yield()