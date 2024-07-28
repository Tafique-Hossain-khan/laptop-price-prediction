# Laptop Price Prediction

[Check out the web app here!](http://your-web-app-url.com)

## Project Description
This project aims to predict the price of a laptop based on various features such as company, type, screen size, resolution, CPU, RAM, memory, GPU, operating system, and weight. The goal is to provide an estimated price for a laptop given these attributes.

## Features
- **Company**: The manufacturer of the laptop.
- **TypeName**: The type or category of the laptop (e.g., Ultrabook, Gaming).
- **Inches**: The screen size of the laptop in inches.
- **ScreenResolution**: The resolution of the laptop's screen.
- **Cpu**: The processor model of the laptop.
- **Ram**: The amount of RAM in the laptop.
- **Memory**: The storage capacity of the laptop.
- **Gpu**: The graphics card model of the laptop.
- **OpSys**: The operating system of the laptop.
- **Weight**: The weight of the laptop.
- **Price**: The output feature, representing the price of the laptop.

## Technologies Used
- **Python**: Programming language.
- **Pandas**: Data manipulation and analysis.
- **Scikit-learn**: Machine learning library.
- **Streamlit**: Web application framework for deploying the model.
- **Matplotlib**: Plotting and visualization.
- **NumPy**: Numerical computing.

## Installation Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/laptop-price-prediction.git
   cd laptop-price-prediction

## Installation Instructions
2. Create a virtual environment:
   ```bash
   python -m venv env

3. Activate the virtual environment:
   - On Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source env/bin/activate
     ```
4. Install the required packages:

```bash
pip install -r requirements.txt


## Usage Instructions

1. Run the Streamlit app:

   ```bash
   streamlit run app.py
Open your web browser and go to the provided URL (usually http://localhost:8501).

Enter the required features for the laptop (Company, TypeName, Inches, ScreenResolution, Cpu, Ram, Memory, Gpu, OpSys, Weight) and click the "Predict" button to get the estimated price.

## Model Details

- **Model Used**: RandomForestRegressor
- **Performance**: Achieved an R² score of 85% with just 1106 rows of data.
