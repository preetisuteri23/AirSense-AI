import streamlit as st
import pandas as pd
import geopandas as gpd
import plotly.express as px
from pathlib import Path
from utils.navbar import navbar

st.set_page_config(
    page_title="AirSense AI Dashboard",
    page_icon="📊",
    layout="wide"
)

navbar()

BASE_DIR = Path(__file__).resolve().parent.parent

# ==========================================
# LOAD CSS
# ==========================================

css_path = BASE_DIR / "styles" / "style.css"

with open(css_path) as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)
DATA_DIR = BASE_DIR / "DATA" / "CLEANED"

# Load datasets
aqi_df = pd.read_csv(DATA_DIR / "city_day_clean.csv")

weather_df = pd.read_csv(DATA_DIR / "Delhi_NASA_weather_cleaned.csv")

industrial_gdf = gpd.read_file(DATA_DIR / "cleaned_industrial.geojson")

sensitive_gdf = gpd.read_file(DATA_DIR / "cleaned_sensitive_locations.geojson")

construction_gdf = gpd.read_file(DATA_DIR / "cleaned_construction_waste.geojson")

road_gdf = gpd.read_file(DATA_DIR / "Delhi_Road_Network_cleaned.geojson")

landuse_gdf = gpd.read_file(DATA_DIR / "Delhi_Land_Use_cleaned.geojson")

industrial_count = len(industrial_gdf)

sensitive_count = len(sensitive_gdf)

construction_count = len(construction_gdf)

road_count = len(road_gdf)

landuse_count = len(landuse_gdf)

st.title("📊 AirSense AI Dashboard")

st.write(
    "Explore historical air quality trends, environmental datasets, and key pollution indicators through integrated AI and GIS analytics"
)

st.divider()

st.subheader("📈 Environmental Overview")

col1, col2, col3, col4, col5 = st.columns(5)

average_aqi = round(aqi_df["AQI"].mean())


with col1:
    st.metric(
    "🌫 Average AQI",
    average_aqi,
    delta="Poor",
    delta_color="inverse"
)
with col2:
    st.metric(
    "🏭 Industrial Zones",
    len(industrial_gdf)
)

with col3:
    st.metric(
    "🏥 Sensitive Locations",
    len(sensitive_gdf)
)
    
with col4:
    st.metric(
    "🚧 Construction Sites",
    len(construction_gdf)
)
with col5:
    st.metric("🤖 Prediction Engine", "Ready")

st.divider()

st.subheader("📈 Historical Air Quality Trend")

aqi_df["Date"] = pd.to_datetime(aqi_df["Date"])

daily_aqi = (
    aqi_df.groupby("Date")["AQI"]
    .mean()
    .reset_index()
)

fig = px.line(
    daily_aqi,
    x="Date",
    y="AQI",
    title="Historical AQI Trend (2015-2020)",
    template="plotly_dark"
)

fig.update_traces(line=dict(width=3))

fig.update_layout(
    height=500,
    hovermode="x unified",
    title_x=0.5,
    font=dict(size=16)
)


st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

st.divider()

st.subheader("🥧 Air Quality Category Distribution")

bucket_counts = (
    aqi_df["AQI_Bucket"]
    .value_counts()
    .reset_index()
)

bucket_counts.columns = ["Category", "Count"]

fig = px.pie(
    bucket_counts,
    names="Category",
    values="Count",
    hole=0.60,
    template="plotly_dark",
    title="Distribution of AQI Categories"
)

fig.update_traces(textposition="inside", textinfo="percent+label")

fig.update_layout(
    legend_title="AQI Categories"
)

fig.update_layout(
    height=500,
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)"
)

st.plotly_chart(fig, use_container_width=True,config={"displayModeBar": False})

st.divider()

st.subheader("🚨 Pollution Monitoring Summary")

avg_aqi = round(aqi_df["AQI"].mean())

if avg_aqi <= 50:
    status = "🟢 Good"
    recommendation = (
        "Air quality is excellent. Outdoor activities are safe for everyone."
    )

elif avg_aqi <= 100:
    status = "🟡 Satisfactory"
    recommendation = (
        "Air quality is acceptable. Sensitive individuals should monitor symptoms."
    )

elif avg_aqi <= 200:
    status = "🟠 Moderate"
    recommendation = (
        "Sensitive groups should limit prolonged outdoor exposure."
    )

elif avg_aqi <= 300:
    status = "🔴 Poor"
    recommendation = (
        "Reduce outdoor activities. Wear an N95 mask if travelling for long periods."
    )

elif avg_aqi <= 400:
    status = "🚨 Very Poor"
    recommendation = (
        "Avoid outdoor exercise. Children, elderly, and people with respiratory conditions should remain indoors."
    )

else:
    status = "☠️ Severe"
    recommendation = (
        "Health emergency. Stay indoors, avoid unnecessary travel, and follow official air quality advisories."
    )

st.metric("Overall Historical AQI Category", status)

st.info(f"**Average AQI(Historical):** {avg_aqi}")

col1, col2, col3 = st.columns(3)

with col1:
    st.info(f"🏭 Industrial Areas: {industrial_count}")

with col2:
    st.info(f"🚧 Construction Sites: {construction_count}")

with col3:
    st.info(f"🏥 Sensitive Locations: {sensitive_count}")

st.markdown("#### Recommendation")
if avg_aqi <= 100:
    st.success(recommendation)

elif avg_aqi <= 200:
    st.info(recommendation)

elif avg_aqi <= 300:
    st.warning(recommendation)

else:
    st.error(recommendation)
st.divider()

st.subheader("📂 Dataset Summary")
st.caption(
    "Overview of environmental datasets integrated into the AirSense AI platform."
)
summary = pd.DataFrame({
    "Dataset": [
        "Historical AQI",
        "Industrial Areas",
        "Sensitive Locations",
        "Construction Sites",
        "Road Network",
        "Land Use"
    ],
    "Records": [
    len(aqi_df),
    industrial_count,
    sensitive_count,
    construction_count,
    road_count,
    landuse_count
]
    
})

st.dataframe(summary, use_container_width=True)