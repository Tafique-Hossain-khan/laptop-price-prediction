import streamlit as st
import numpy as np
import pandas as pd
import joblib  # Assuming your model is saved with joblib

from src.utils import load_object
from src.pipeline.prediction_pipeling import CustomInputLaptop
from src.utils import load_object

# Load the trained model
model = load_object('artifacts\model_laptop.pkl')# Replace with your model's filename
preprocessor = load_object('artifacts\preprocessor_laptop.pkl')

st.title("Laptop Price Prediction")
st.write("Enter the details of the laptop to predict its price:")

# Input fields
company = st.selectbox("Company", 
                       ['Apple', 'HP', 'Acer', 'Asus', 'Dell', 'Lenovo', 'Chuwi', 'MSI', 'Microsoft', 'Toshiba', 'Huawei', 'Xiaomi', 'Vero', 'Razer', 'Mediacom', 'Samsung', 'Google', 'Fujitsu', 'LG'])

typename = st.selectbox("Type", 
                        ['Ultrabook', 'Notebook', 'Netbook', 'Gaming', '2 in 1 Convertible', 'Workstation'])

ram = st.selectbox("RAM (GB)", [8, 16, 4, 2, 12, 6, 32, 24, 64])

weight = st.number_input("Weight (kg)", min_value=0.0, step=0.1)

touchscreen = st.selectbox("Touchscreen", [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')

ips = st.selectbox("IPS", [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
# PPI Calculation
st.write("To calculate PPI, you need to provide X Resoluntion Y resolution and the Screen inches.")
with st.expander("Click to calculate PPI"):
    x_res = st.number_input("X Resolution", min_value=0)
    y_res = st.number_input("Y Resolution", min_value=0)
    inches = st.number_input("Screen Size (inches)", min_value=0.0, step=0.1)
    if inches > 0:
        ppi = (((x_res ** 2) + (y_res ** 2)) ** 0.5 / inches)
        st.write(f"Calculated PPI: {ppi:.2f}")
    


cpu_brand = st.selectbox("CPU Brand", 
                         ['Intel Core i5', 'Intel Core i7', 'AMD Processor', 'Intel Core i3', 'Other Intel Processor'])

gpu_brand = st.selectbox("GPU Brand", 
                         ['Nvidia', 'AMD', 'Intel', 'Other'])  


hdd = st.selectbox("HDD (GB)", [0, 500, 1000, 2000, 32, 128], format_func=lambda x: f"{x} GB" if x < 1000 else f"{x//1000} TB")

ssd = st.selectbox("SSD (GB)", [128, 0, 256, 512, 32, 64, 1000, 1024, 16, 768, 180, 240, 8])

os = st.selectbox("Operating System", ['Mac', 'Others/No OS/Linux', 'Windows'])

# Prediction
if st.button("Predict Price"):
    laptop_input = CustomInputLaptop(company, typename, ram, weight, touchscreen, ips, ppi, cpu_brand, hdd, ssd, gpu_brand, os)
    input_df = laptop_input.custom_dataset()
    data_scaled = preprocessor.transform(input_df)
    prediction = model.predict(data_scaled)
    st.success(f"The predicted price of the laptop is RS {prediction[0]:,.2f}")

# Customize the app appearance
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f0f5;
        padding: 10px;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True
)
