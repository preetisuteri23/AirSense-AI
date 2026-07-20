import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json
from pathlib import Path
from utils.navbar import navbar


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Prediction | AirSense AI",
    page_icon="🔮",
    layout="wide"
)
navbar()

# ==========================================================
# LOAD CUSTOM CSS
# ==========================================================

with open("styles/style.css") as css:
    st.markdown(
        f"<style>{css.read()}</style>",
        unsafe_allow_html=True
    )

# ==========================================================
# PROJECT PATHS
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "models"

# ==========================================================
# LOAD MODEL OUTPUTS
# ==========================================================

@st.cache_data
def load_data():

    performance = pd.read_csv(
        MODEL_DIR / "Final_Model_Performance.csv"
    )

    feature_importance = pd.read_csv(
        MODEL_DIR / "Final_Feature_Importance.csv"
    )

    with open(
        MODEL_DIR / "AQI_Forecast_Output.json",
        "r"
    ) as f:
        forecast = json.load(f)

    with open(
        MODEL_DIR / "Frontend_Model_Output.json",
        "r"
    ) as f:
        summary = json.load(f)

    return (
        performance,
        feature_importance,
        forecast,
        summary
    )


performance, feature_importance, forecast, summary = load_data()
# ==========================================================
# HERO SECTION
# ==========================================================

st.markdown("""
<div class="hero">

<h1>🔮 AQI Prediction & Forecasting</h1>

<p>
AirSense AI leverages an advanced XGBoost machine learning model to
predict Air Quality Index (AQI) using environmental, meteorological,
and satellite-derived features. The model enables proactive pollution
monitoring, early warning generation, and data-driven decision-making
for sustainable smart cities.
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================================
# MODEL OVERVIEW
# ==========================================================

st.markdown("## 📊 Model Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="🤖 Model",
        value="XGBoost"
    )

with col2:
    st.metric(
        label="🧠 Features",
        value="30"
    )

with col3:
    st.metric(
        label="📈 Predictions",
        value=summary["prediction_count"]
    )

with col4:
    st.metric(
        label="✅ Status",
        value="Ready"
    )

st.markdown("""
The XGBoost regression model was trained using 30 selected environmental,
meteorological, and satellite-derived features to accurately forecast the
Air Quality Index (AQI). The model provides reliable predictions that can
support pollution monitoring and smart-city decision-making.
""")

st.divider()


# ==========================================================
# FORECAST SUMMARY
# ==========================================================

st.markdown("## 📈 Forecast Summary")

st.markdown("""
The trained XGBoost model generated predictions for the evaluation dataset.
The summary below provides a quick overview of the predicted Air Quality
Index (AQI) values.
""")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="📊 Average AQI",
        value=f"{summary['average_predicted_AQI']:.1f}"
    )

with col2:
    st.metric(
        label="🔺 Highest AQI",
        value=f"{summary['highest_predicted_AQI']:.1f}"
    )

with col3:
    st.metric(
        label="🔻 Lowest AQI",
        value=f"{summary['lowest_predicted_AQI']:.1f}"
    )

with col4:
    st.metric(
        label="📈 Forecast Samples",
        value=summary["prediction_count"]
    )

st.divider()

# ==========================================================
# ACTUAL VS PREDICTED AQI
# ==========================================================

st.markdown("## 📉 Actual vs Predicted AQI")

st.markdown("""
The chart below compares the actual AQI values with the AQI predicted by
the trained XGBoost model. The close alignment between both curves
demonstrates the model's ability to accurately forecast air quality.
""")

forecast_df = pd.DataFrame(forecast)

fig = go.Figure()

# Actual AQI
fig.add_trace(
    go.Scatter(
        x=forecast_df["Prediction_ID"],
        y=forecast_df["Actual_AQI"],
        mode="lines",
        name="Actual AQI",
        line=dict(color="#4FC3F7", width=3)
    )
)

# Predicted AQI
fig.add_trace(
    go.Scatter(
        x=forecast_df["Prediction_ID"],
        y=forecast_df["Predicted_AQI"],
        mode="lines",
        name="Predicted AQI",
        line=dict(color="#00E676", width=3, dash="dash")
    )
)

fig.update_layout(
    template="plotly_dark",
    height=520,
    title="Actual vs Predicted Air Quality Index",
    xaxis_title="Prediction Sample",
    yaxis_title="AQI",
    hovermode="x unified",
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="center",
        x=0.5
    ),
    margin=dict(l=20, r=20, t=60, b=20)
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ==========================================================
# MODEL PERFORMANCE
# ==========================================================

st.markdown("## 🎯 Model Performance")

st.markdown("""
The trained XGBoost model was evaluated using standard regression metrics.
The results indicate high prediction accuracy and strong generalization
across different AQI levels.
""")

metrics = dict(zip(
    performance["Metric"],
    performance["Value"]
))

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        label="📉 RMSE",
        value=f"{metrics['RMSE']:.2f}"
    )

with c2:
    st.metric(
        label="📊 MAE",
        value=f"{metrics['MAE']:.2f}"
    )

with c3:
    st.metric(
        label="🎯 R² Score",
        value=f"{metrics['R2']:.3f}"
    )

with c4:
    st.metric(
        label="✅ AQI Accuracy",
        value=f"{metrics['AQI Category Accuracy']*100:.2f}%"
    )

st.info("""
**Performance Interpretation**

• **RMSE (18.75):** The prediction error remains low, indicating that the model closely follows actual AQI values.

• **MAE (14.38):** On average, predictions differ from the actual AQI by approximately 14 points.

• **R² Score (95.42%):** The model explains over 95% of the variability in AQI, demonstrating excellent predictive capability.

• **AQI Category Accuracy (86.26%):** Most predicted AQI values fall into the correct pollution category, making the model suitable for practical decision support.
""")

st.divider()


# ==========================================================
# FEATURE IMPORTANCE
# ==========================================================

st.markdown("## 🧠 Feature Importance")

st.markdown("""
Feature importance represents the contribution of each input variable
towards AQI prediction. Higher importance indicates that the feature has
a greater influence on the model's decision-making process.
""")

top_features = (
    feature_importance
    .sort_values("Importance", ascending=False)
    .head(10)
)

fig = px.bar(
    top_features,
    x="Importance",
    y="Feature",
    orientation="h",
    text="Importance",
    color="Importance",
    color_continuous_scale="Tealgrn"
)

fig.update_traces(
    texttemplate="%{text:.3f}",
    textposition="outside"
)

fig.update_layout(
    template="plotly_dark",
    height=550,
    yaxis=dict(autorange="reversed"),
    coloraxis_showscale=False,
    xaxis_title="Importance Score",
    yaxis_title="",
    margin=dict(l=20, r=20, t=50, b=20)
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.success("""
**Key Insight**

The model identifies **PM2.5**, **historical AQI**, **PM10**, moving averages,
and meteorological variables as the strongest predictors of future air quality.
This demonstrates that both current pollution levels and historical environmental
patterns significantly influence AQI forecasting.
""")

st.divider()

# ==========================================================
# SMART CITY RECOMMENDATIONS
# ==========================================================

st.markdown("## 💡 AI-Powered Smart City Recommendations")

st.markdown("""
Based on the prediction results and feature importance analysis, the
following recommendations can help city authorities proactively improve
air quality and reduce pollution risks.
""")

col1, col2 = st.columns(2)

with col1:

    st.success("""
### 🚗 Traffic Emission Control

Since **PM2.5** is the most influential feature, reducing vehicular
emissions through cleaner public transport, EV adoption, and stricter
emission checks can significantly improve air quality.
""")

    st.info("""
### 🌳 Urban Green Infrastructure

Increase roadside plantations, green belts, and urban forests in
high-risk pollution zones to naturally absorb airborne pollutants.
""")

with col2:

    st.warning("""
### 🏭 Industrial Pollution Monitoring

Deploy continuous monitoring around industrial areas and enforce
real-time emission compliance to reduce harmful pollutants.
""")

    st.error("""
### 🚨 Early Warning & Decision Support

Use AQI forecasts to issue early public health advisories, regulate
traffic during severe pollution events, and support proactive
environmental planning.
""")

st.divider()


# ==========================================================
# MODEL INFORMATION
# ==========================================================

st.markdown("## ℹ️ Model Information")

st.markdown("""
This section summarizes the machine learning model, the data used for
training, and the overall objective of the prediction system.
""")

left, right = st.columns(2)

with left:

    st.markdown("""
### 🤖 Model Details

| Property | Value |
|:---------|:------|
| **Algorithm** | XGBoost Regressor |
| **Learning Type** | Supervised Machine Learning |
| **Prediction Target** | Air Quality Index (AQI) |
| **Selected Features** | 30 |
| **Evaluation Samples** | 182 |
| **Prediction Type** | Regression |
""")

with right:

    st.markdown("""
### 📂 Training Information

| Property | Value |
|:---------|:------|
| **Primary Dataset** | CPCB Delhi Air Quality Dataset |
| **Weather Data** | NASA POWER Weather Dataset |
| **Satellite Data** | MODIS Aerosol Optical Depth (AOD) |
| **Feature Engineering** | Lag Features, Moving Averages, Ratios & Environmental Indicators |
| **Objective** | Accurate AQI Forecasting for Smart City Decision Support |
""")

st.success("""
### 🎯 Project Outcome

AirSense AI successfully demonstrates how Artificial Intelligence can
forecast Air Quality Index using environmental, meteorological, and
satellite-derived data. The developed XGBoost model achieves high
prediction accuracy while providing interpretable insights through
feature importance analysis. The system can support pollution
monitoring, early warning generation, and data-driven smart city
planning.
""")

st.markdown("---")

st.markdown(
    "<center><b>🌍 AirSense AI | AI-Powered Smart City Air Quality Forecasting System</b></center>",
    unsafe_allow_html=True
)