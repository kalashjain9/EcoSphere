import streamlit as st
import joblib
import numpy as np
import pandas as pd

class CropPredictionApp:
    def __init__(self):
        """Initialize Crop Prediction Streamlit App"""
        st.set_page_config(page_title="Crop Recommendation System", page_icon="🌱")
        self.load_model()
    
    def load_model(self):
        """Load pre-trained machine learning model"""
        try:
            self.model = joblib.load('model_storage\crop_random_forest.joblib')
            st.sidebar.success("Model loaded successfully!")
        except FileNotFoundError:
            st.sidebar.error("Model file not found. Please train a model first.")
            self.model = None
    
    def input_features(self):
        """Collect input features from user"""
        st.header("Crop Recommendation Input")
        
        col1, col2 = st.columns(2)
        
        with col1:
            nitrogen = st.number_input("Nitrogen (N) Content", min_value=0.0, step=1.0)
            phosphorus = st.number_input("Phosphorus (P) Content", min_value=0.0, step=1.0)
            potassium = st.number_input("Potassium (K) Content", min_value=0.0, step=1.0)
        
        with col2:
            temperature = st.number_input("Temperature (°C)", min_value=0.0, step=0.1)
            humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, step=1.0)
        
        ph_value = st.slider("Soil pH Value", min_value=0.0, max_value=14.0, value=7.0, step=0.1)
        rainfall = st.number_input("Rainfall (mm)", min_value=0.0, step=1.0)
        
        return [nitrogen, phosphorus, potassium, temperature, humidity, ph_value, rainfall]
    
    def predict_crop(self, features):
        """Predict crop based on input features"""
        if self.model is None:
            st.error("Model not loaded. Cannot make predictions.")
            return None
        
        prediction = self.model.predict([features])
        return prediction[0]
    
    def run(self):
        """Main application workflow"""
        st.title("🌾 Crop Recommendation System")
        
        # Input features
        input_features = self.input_features()
        
        # Prediction button
        if st.button("Predict Crop"):
            if self.model is not None:
                crop = self.predict_crop(input_features)
                st.success(f"Recommended Crop: {crop}")
                
                # Optional: Display input features for transparency
                input_df = pd.DataFrame([input_features], 
                    columns=['Nitrogen', 'Phosphorus', 'Potassium', 
                             'Temperature', 'Humidity', 'pH Value', 'Rainfall'])
                st.write("Input Features:", input_df)
            else:
                st.error("Cannot predict without a loaded model.")

def main():
    app = CropPredictionApp()
    app.run()

if __name__ == "__main__":
    main()