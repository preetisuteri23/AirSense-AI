import streamlit as st
from pathlib import Path
from utils.navbar import navbar

st.set_page_config(
    page_title="About AirSense AI",
    page_icon="ℹ️",
    layout="wide"
)

navbar()

# -----------------------------
# Load CSS
# -----------------------------
with open("styles/style.css", "r", encoding="utf-8") as css:
    st.markdown(
        f"<style>{css.read()}</style>",
        unsafe_allow_html=True
    )

# ============================================================
# Hero Section
# ============================================================

st.title("🌍 About AirSense AI")

st.markdown("""
### AI & GIS-Based Pollution Source Identification Platform

AirSense AI is an intelligent environmental analytics platform developed for the
**Economic Times Hackathon 2026**.

The platform integrates **Artificial Intelligence (AI)**, **Geographic Information Systems (GIS)**,
and **geospatial datasets** to identify pollution sources, analyze environmental
patterns, and support data-driven urban planning across Delhi.

By combining interactive visualizations with spatial analysis, AirSense AI helps
transform complex environmental data into meaningful insights for smarter decision-making.
""")

st.divider()

# ============================================================
# Project Overview
# ============================================================

st.header("🎯 Project Overview")

with st.container(border=True):

    st.markdown("""
AirSense AI is designed to support **environmental monitoring and pollution source
identification** by integrating Artificial Intelligence (AI) with Geographic
Information Systems (GIS).

The platform combines multiple geospatial datasets to visualize environmental
conditions, analyze pollution-related infrastructure, and provide meaningful
insights that support sustainable urban planning.

Rather than relying on a single data source, AirSense AI performs integrated
analysis using transportation networks, industrial zones, construction activities,
sensitive locations, and land-use information to build a comprehensive
environmental assessment.
""")

st.divider()

# ============================================================
# Problem Statement
# ============================================================

st.header("❓ Problem Statement")

with st.container(border=True):

    st.markdown("""
Rapid urbanization has increased environmental challenges in Delhi, including
traffic emissions, industrial pollution, construction dust, and pressure on
environmentally sensitive locations.

Although environmental data is available from multiple sources, it is often
distributed across separate datasets, making integrated analysis difficult.

AirSense AI addresses this challenge by combining GIS datasets into a unified
analytics platform that supports pollution source identification, environmental
assessment, and future AI-driven prediction.
""")

# ============================================================
# How AirSense AI Works
# ============================================================

st.divider()

st.header("⚙️ How AirSense AI Works")

st.markdown("""
The workflow below illustrates how AirSense AI transforms raw geospatial datasets into
meaningful environmental insights and AI-assisted decision support.
""")

with st.container(border=True):

    st.subheader("🌍 AirSense AI Workflow")

    st.markdown("""
### 📂 Geospatial Datasets
Road Network • Industrial Areas • Construction & Waste • Sensitive Locations • Land Use

⬇️

### 🧹 Data Cleaning & Preprocessing
Cleaning • Missing Value Handling • Standardization • GeoJSON Processing

⬇️

### 🗺️ GIS-Based Spatial Analysis
Spatial Distribution • Environmental Mapping • Infrastructure Analysis

⬇️

### 📊 Interactive Dashboard & Visual Analytics
Maps • Charts • Environmental Insights • Dataset Exploration

⬇️

### 🧠 AI Environmental Assessment
Integrated Pollution Source Analysis • Pattern Identification • Environmental Interpretation

⬇️

### 🤖 Machine Learning Prediction 
AQI Prediction • Pollution Source Classification • Risk Assessment

⬇️

### 🎯 Decision Support & Smart Urban Planning
Data-Driven Recommendations • Environmental Planning • Sustainable Decision Support
""")

st.divider()


# ============================================================
# Technologies Used
# ============================================================

st.header("🛠 Technologies Used")

st.markdown("""
AirSense AI combines modern data science, GIS, visualization, and machine
learning technologies to build an intelligent environmental analytics platform.
""")

col1, col2 = st.columns(2)

with col1:

    with st.container(border=True):
        st.markdown("""
### 🐍 Python

Core programming language used for data processing,
analytics, and application development.
""")

    with st.container(border=True):
        st.markdown("""
### 🌍 GeoPandas

Used for reading, processing, and analyzing
geospatial datasets.
""")

    with st.container(border=True):
     st.markdown("""
### 🧠 SHAP Explainability

Enhances AI transparency by explaining the
contribution of each feature to the predicted AQI,
making the XGBoost model interpretable and
trustworthy for smart city decision-making.
""")

    with st.container(border=True):
        st.markdown("""
### 🚀 Streamlit

Web framework used to develop the interactive
analytics dashboard.
""")

with col2:

    with st.container(border=True):
        st.markdown("""
### 🗺 OpenStreetMap

Primary source of geospatial datasets
used throughout the project.
""")

    with st.container(border=True):
        st.markdown("""
### 📄 GeoJSON

Standard geospatial format used for
environmental datasets.
""")

    with st.container(border=True):
        st.markdown("""
### 🤖 Machine Learning

Used for pollution prediction,
risk assessment, and future forecasting.
""")

    with st.container(border=True):
        st.markdown("""
### 💻 VS Code & GitHub

Development environment and version
control for collaborative development.
""")

st.divider()


# ============================================================
# Datasets Used
# ============================================================

st.header("🗂 Datasets Used")

st.markdown("""
AirSense AI integrates multiple geospatial and environmental datasets to
provide a comprehensive understanding of pollution sources, air quality,
and environmental conditions across Delhi.
""")

col1, col2 = st.columns(2)

with col1:

    with st.container(border=True):
        st.markdown("""
### 📊 Historical AQI (CPCB)

Historical Air Quality Index data collected from
the Central Pollution Control Board (CPCB) used
for model training and AQI forecasting.
""")

    with st.container(border=True):
        st.markdown("""
### 🌦 Weather (OpenWeather API)

Meteorological parameters including temperature,
humidity, wind speed, and atmospheric conditions
used for environmental analysis.
""")

    with st.container(border=True):
        st.markdown("""
### 🛰 Satellite Data (MODIS / Sentinel-5P)

Satellite-derived Aerosol Optical Depth (AOD) and
atmospheric observations used to monitor regional
air pollution and environmental conditions.
""")

with col2:

    with st.container(border=True):
        st.markdown("""
### 🛣 Road Network

Represents Delhi's transportation infrastructure,
including different road classifications used for
traffic and connectivity analysis.
""")

    with st.container(border=True):
        st.markdown("""
### 🏭 Industrial Areas

Contains industrial locations that may contribute
to stationary air pollution and environmental emissions.
""")

    with st.container(border=True):
        st.markdown("""
### 🚧 Construction & Waste

Identifies construction zones and waste locations
that can generate localized dust and particulate pollution.
""")

st.divider()


# ============================================================
# Future Scope
# ============================================================

st.header("🚀 Future Scope")

st.markdown("""
AirSense AI is designed as a scalable platform that can be extended with
advanced AI models, real-time environmental monitoring, and smart city
technologies to support future urban sustainability initiatives.
""")

col1, col2 = st.columns(2)

with col1:

    with st.container(border=True):

        st.markdown("""
### 🌐 Planned Enhancements

- Live AQI Monitoring
- Advanced Pollution Forecasting
- IoT-based Environmental Sensors
- Real-time Pollution Alerts
""")

with col2:

    with st.container(border=True):

        st.markdown("""
### 🤖 AI Expansion

- Enhanced Prediction Accuracy
- Multi-pollutant Forecasting
- Explainable AI (XAI) Insights
- Smart Decision Support
""")

st.divider()

# ============================================================
# Development Team
# ============================================================

st.header("👨‍💻 Development Team")

with st.container(border=True):

    st.markdown("""
### AirSense AI

Developed as part of the **Economic Times Hackathon 2026**

**Team Members**

- Preeti Suteri
- Arunika Negi

**Project Focus**

AI + GIS Based Pollution Source Identification and Environmental Analytics
""")

st.divider()

st.caption(
    """🌍 AirSense AI | Economic Times Hackathon 2026
AI + GIS Based Pollution Source Identification & Environmental Analytics"""
)