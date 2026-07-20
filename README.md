# 🌍 AirSense AI

> **AI + GIS Powered Pollution Source Identification and AQI Prediction System**

AirSense AI is an AI-driven environmental intelligence platform developed for the **Economic Times Hackathon 2026**. The platform integrates Artificial Intelligence (AI), Geographic Information Systems (GIS), and multiple environmental datasets to identify potential pollution sources, visualize environmental information, forecast Air Quality Index (AQI), and support data-driven urban decision-making.

---

# 📌 Problem Statement

Urban air pollution is influenced by multiple environmental and anthropogenic factors such as industrial activities, transportation networks, construction sites, land use, and meteorological conditions. Environmental datasets are often scattered across different sources, making pollution analysis difficult.

AirSense AI addresses this challenge by integrating AI and GIS technologies into a unified platform for pollution source identification and environmental intelligence.

---

# 🎯 Objectives

- Identify potential pollution sources using AI and GIS
- Integrate multiple environmental datasets
- Visualize pollution-related information spatially
- Forecast Air Quality Index (AQI) using Machine Learning
- Support smarter environmental monitoring and decision-making

---

# ✨ Features

- 📊 Environmental Dashboard
- 🗺 Interactive GIS Mapping
- 🤖 AI Environmental Analysis
- 📈 AQI Prediction using XGBoost
- 📉 Historical AQI Trend Analysis
- 🌫 Pollution Source Identification
- 📍 Multi-source Environmental Data Integration
- 💡 Smart Environmental Recommendations

---

# 🛰 Datasets Used

- Historical AQI Data
- Weather Data
- MODIS Satellite Aerosol Optical Depth (AOD)
- Industrial Areas
- Construction & Waste Sites
- Road Network
- Land Use
- Sensitive Locations (Schools & Hospitals)

---

# 🏗 System Workflow

```text
Environmental Datasets
        │
        ▼
Data Cleaning & Integration
        │
        ▼
GIS Visualization
        │
        ▼
AI Environmental Analysis
        │
        ▼
Pollution Source Identification
        │
        ▼
AQI Prediction (XGBoost)
        │
        ▼
Smart City Recommendations
```

---

# 🤖 Machine Learning Model

Model Used:

- XGBoost Regressor

Performance Metrics:

- RMSE: 18.75
- MAE: 14.38
- R² Score: 0.954
- AQI Category Accuracy: 86.26%

---

# 🛠 Tech Stack

### Frontend

- Streamlit
- HTML
- CSS
- Plotly

### Backend

- Python

### GIS

- GeoPandas
- Folium
- OpenStreetMap

### Machine Learning

- XGBoost
- Scikit-learn

### Data Processing

- Pandas
- NumPy

---

# 📂 Project Structure

```text
AirSenseAI/

├── assets/
├── DATA/
├── models/
├── pages/
├── styles/
├── utils/
├── Home.py
├── requirements.txt
└── README.md
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/your-username/AirSenseAI.git
```

Move into the project directory

```bash
cd AirSenseAI
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run Home.py
```

---

# 🎯 Project Modules

## Home

Project overview and navigation.

## Dashboard

Environmental monitoring and analytics.

## GIS Map

Interactive visualization of environmental datasets.

## AI Analysis

AI-based pollution source assessment and environmental insights.

## Prediction

Machine learning-based AQI forecasting using XGBoost.

## About

Project documentation and methodology.

---

# 🌱 Future Enhancements

- Real-time AQI monitoring
- Live traffic data integration
- IoT sensor connectivity
- Mobile application
- Early warning notifications
- Smart city integration

---

# 👥 Team

Economic Times Hackathon 2026

Project:
**AirSense AI**

---

# 📄 License

This project was developed for educational and hackathon purposes.
