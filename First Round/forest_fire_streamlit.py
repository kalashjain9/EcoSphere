import streamlit as st
import os
import numpy as np
import tensorflow as tf
import folium
import pandas as pd
from streamlit_folium import folium_static

# Load the fire detection model
@st.cache_resource
def load_fire_detection_model():
    return tf.keras.models.load_model(r'new/fire_detection_model (1).h5')

# Image prediction function
def predict_fire(image):
    model = load_fire_detection_model()
    img_height, img_width = 224, 224
    
    # Convert uploaded file to image
    img = tf.keras.preprocessing.image.load_img(
        image, 
        target_size=(img_height, img_width)
    )
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)
    
    prediction = model.predict(img_array)
    prediction_result = 'Fire Detected' if prediction[0] > 0.5 else 'No Fire'
    return prediction_result

# Mapping functions remain the same as in the previous implementation
def load_data():
    data_path = 'new/fire_nrt_M6_107977.csv'
    return pd.read_csv(data_path)

def create_fire_map(data):
    # Create a base map centered on India
    india_map = folium.Map(
        location=[22.5937, 78.9629], 
        zoom_start=5, 
        tiles='OpenStreetMap',
        attr='Map data © OpenStreetMap contributors'
    )

    # Iterate through the dataset and add markers to the map
    for _, row in data.iterrows():
        # Create tooltip text with key information
        tooltip = f"""
        <b>Brightness:</b> {row['brightness']}<br>
        <b>Latitude:</b> {row['latitude']}<br>
        <b>Longitude:</b> {row['longitude']}<br>
        <b>Date:</b> {row['acq_date']}<br>
        <b>Confidence:</b> {row['confidence']}<br>
        <b>FRP:</b> {row['frp']}<br>
        <b>Day/Night:</b> {row['daynight']}
        """
    
        # Determine marker color based on confidence level
        confidence = row['confidence']
        if confidence >= 80:
            color = 'red'
        elif confidence >= 50:
            color = 'orange'
        else:
            color = 'green'
    
        # Add marker to the map
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=5,
            color=color,
            fill=True,
            fill_opacity=0.7,
            tooltip=tooltip
        ).add_to(india_map)
    
    return india_map

def main():
    st.sidebar.title('Forest Fire Analysis')
    
    # Sidebar navigation
    app_mode = st.sidebar.selectbox(
        'Choose Application Mode',
        ['Image Detection', 'Fire Incidents Map']
    )
    
    if app_mode == 'Image Detection':
        # Image Detection Mode
        st.title('Forest Fire Detection')
        
        # File uploader
        uploaded_file = st.file_uploader(
            "Choose an image...", 
            type=["jpg", "jpeg", "png"]
        )
        
        if uploaded_file is not None:
            # Display uploaded image
            st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
            
            # Perform prediction
            try:
                prediction = predict_fire(uploaded_file)
                
                # Display prediction results
                if prediction == 'Fire Detected':
                    st.error(f'🔥 {prediction}')
                else:
                    st.success(f'✅ {prediction}')
            
            except Exception as e:
                st.error(f'An error occurred: {str(e)}')
    
    else:
        # Fire Incidents Map Mode
        st.title('India Wildfire Map')
        
        # Load data
        data = load_data()
        
        # Sidebar filters
        st.sidebar.header('Map Filters')
        
        # Confidence level filter
        confidence_filter = st.sidebar.slider(
            'Minimum Confidence Level', 
            min_value=0, 
            max_value=100, 
            value=0
        )
        
        # Date range filter
        min_date = pd.to_datetime(data['acq_date']).min()
        max_date = pd.to_datetime(data['acq_date']).max()
        
        date_range = st.sidebar.date_input(
            'Select Date Range', 
            value=[min_date, max_date],
            min_value=min_date,
            max_value=max_date
        )
        
        # Apply filters
        filtered_data = data[
            (pd.to_datetime(data['acq_date']).dt.date >= date_range[0]) & 
            (pd.to_datetime(data['acq_date']).dt.date <= date_range[1]) & 
            (data['confidence'] >= confidence_filter)
        ]
        
        # Create and display map
        fire_map = create_fire_map(filtered_data)
        folium_static(fire_map)
        
        # Display data summary
        st.subheader('Fire Incidents Summary')
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric('Total Incidents', len(filtered_data))
        
        with col2:
            st.metric('High Confidence Incidents', 
                      len(filtered_data[filtered_data['confidence'] >= 80]))
        
        with col3:
            st.metric('Date Range', 
                      f"{date_range[0]} to {date_range[1]}")

if __name__ == '__main__':
    main()