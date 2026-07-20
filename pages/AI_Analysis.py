import streamlit as st
import geopandas as gpd
import pandas as pd
from pathlib import Path
import plotly.express as px
from utils.navbar import navbar

st.set_page_config(
    page_title="AI Pollution Source Analysis",
    page_icon="🤖",
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

# -----------------------------
# Paths
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "DATA" / "CLEANED"

# -----------------------------
# Load datasets
# -----------------------------
@st.cache_data
def load_data():

    industrial = gpd.read_file(
        DATA_DIR / "cleaned_industrial.geojson"
    )

    sensitive = gpd.read_file(
        DATA_DIR / "cleaned_sensitive_locations.geojson"
    )

    construction = gpd.read_file(
        DATA_DIR / "cleaned_construction_waste.geojson"
    )

    roads = gpd.read_file(
        DATA_DIR / "Delhi_Road_Network_cleaned.geojson"
    )

    landuse = gpd.read_file(
        DATA_DIR / "Delhi_Land_Use_cleaned.geojson"
    )

    return (
        industrial,
        sensitive,
        construction,
        roads,
        landuse
    )


industrial, sensitive, construction, roads, landuse = load_data()


# ============================================================
# Hero Section
# ============================================================

st.title("🤖 AI Pollution Source Analysis")

st.markdown("""
### AI-Powered Environmental Intelligence for Delhi

AirSense AI integrates **Artificial Intelligence (AI)** and **Geographic Information Systems (GIS)**
to analyze environmental datasets, identify major pollution sources, and support informed
urban planning.

This dashboard combines multiple geospatial datasets—including road networks,
industrial zones, construction activities, sensitive locations, and land use—to
provide meaningful environmental insights and support pollution source identification, environmental assessment, and future pollution prediction.
""")

st.divider()


st.header("📊 Integrated Dataset Overview")

st.markdown("""
AirSense AI integrates five geospatial datasets to analyze pollution sources, environmental conditions, and urban infrastructure across Delhi. Together, these datasets provide the spatial foundation for AI-driven environmental assessment and decision-making.
""")


st.write("")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        label="🛣 Roads",
        value=f"{len(roads):,}"
    )

with col2:
    st.metric(
        label="🏭 Industrial Areas",
        value=f"{len(industrial):,}"
    )

with col3:
    st.metric(
        label="🚧 Construction & Waste",
        value=f"{len(construction):,}"
    )

with col4:
    st.metric(
        label="🏥 Sensitive Locations",
        value=f"{len(sensitive):,}"
    )

with col5:
    st.metric(
        label="🌳 Land Parcels",
        value=f"{len(landuse):,}"
    )

st.divider()

st.header("🌍 Environmental Analytics")

st.markdown("""
AirSense AI analyzes integrated geospatial datasets to understand the spatial
distribution of pollution sources, urban infrastructure, and environmentally
sensitive regions across Delhi.

The visualizations below summarize key characteristics of each dataset,
providing the analytical foundation for AI-assisted environmental assessment.
""")

# ============================================================
# Environmental Analytics Charts
# ============================================================

col1, col2 = st.columns(2)

# ------------------------------------------------------------
# Road Network Distribution
# ------------------------------------------------------------
with col1:
    with st.container(border=True):

        st.subheader("🛣 Road Network Distribution")

        if "highway" in roads.columns:

            road_counts = (
                roads["highway"]
                .astype(str)
                .str.replace("[", "", regex=False)
                .str.replace("]", "", regex=False)
                .str.replace("'", "", regex=False)
                .str.title()
                .str.replace("Living Street", "Living Street")
                .str.replace("Unclassified", "Unclassified")
                .value_counts()
                .head(6)
                .reset_index()
            )
            road_counts.columns = ["Road Type", "Count"]

            road_counts["Road Type"] = (
                    road_counts["Road Type"]
                    .str.replace("_", " ")
            )

            

            fig = px.bar(
                road_counts,
                x="Road Type",
                y="Count",
                text="Count"
            )

            fig.update_traces(
                marker_color="#29B6F6",
                textposition="auto"
            )

            fig.update_layout(
                template="plotly_dark",
                height=450,
                showlegend=False,
                margin=dict(l=20, r=20, t=5, b=20),
                xaxis_title="Road Type",
                yaxis_title="Number of Roads",
                plot_bgcolor="rgba(0,0,0,0)",
                paper_bgcolor="rgba(0,0,0,0)",
                font=dict(size=13)
            )

            st.plotly_chart(
                fig,
                use_container_width=True,
                config={
                        "displayModeBar": False
                 }
            )


# ------------------------------------------------------------
# Sensitive Location Distribution
# ------------------------------------------------------------
with col2:
    with st.container(border=True):

        st.subheader("🏥 Sensitive Location Distribution")

        sensitive_counts = (
            sensitive["amenity"]
            .astype(str)
            .str.title()
            .value_counts()
            .reset_index()
        )

        sensitive_counts.columns = ["Location Type", "Count"]

        fig = px.bar(
            sensitive_counts,
            x="Count",
            y="Location Type",
            orientation="h",
            text="Count"
        )

        fig.update_traces(
            marker_color="#29B6F6",
            textposition="auto"
        )

        fig.update_layout(
            template="plotly_dark",
            height=450,
            showlegend=False,
            margin=dict(l=20, r=20, t=5, b=20),
            xaxis_title="Number of Locations",
            yaxis_title="",
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            font=dict(size=13),
            xaxis=dict(showgrid=True),
            yaxis=dict(categoryorder="total ascending")
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
            config={
                "displayModeBar": False
            }
        )

        # ============================================================
# Second Row
# ============================================================

st.write("")

col3, col4 = st.columns(2)

# ------------------------------------------------------------
# Construction & Waste Distribution
# ------------------------------------------------------------
with col3:
    with st.container(border=True):

        st.subheader("🚧 Construction & Waste Distribution")

        construction_count = construction[
            construction["construction"].notna()
        ].shape[0]

        waste_count = construction[
            construction["waste"].notna()
        ].shape[0]

        construction_df = pd.DataFrame({
            "Category": ["Construction Sites", "Waste Sites"],
            "Count": [construction_count, waste_count]
        })

        fig = px.bar(
            construction_df,
            x="Count",
            y="Category",
            orientation="h",
            text="Count"
        )

        fig.update_traces(
            marker_color="#29B6F6",
            textposition="auto"
        )

        fig.update_layout(
            template="plotly_dark",
            height=450,
            showlegend=False,
            margin=dict(l=20, r=20, t=5, b=20),
            xaxis_title="Number of Locations",
            yaxis_title="",
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            font=dict(size=13),
            xaxis=dict(showgrid=True),
            yaxis=dict(categoryorder="total ascending")
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
            config={
                "displayModeBar": False
            }
        )

# ------------------------------------------------------------
# Land Use Distribution
# ------------------------------------------------------------
with col4:
    with st.container(border=True):

        st.subheader("🌳 Land Type Distribution")

        land_counts = (
            landuse["Land_Type"]
            .astype(str)
            .str.replace("_", " ")
            .str.title()
            .value_counts()
            .head(6)
            .reset_index()
        )

        land_counts.columns = ["Land Type", "Count"]

        fig = px.bar(
            land_counts,
            x="Count",
            y="Land Type",
            orientation="h",
            text="Count"
        )

        fig.update_traces(
            marker_color="#29B6F6",
            textposition="auto"
        )

        fig.update_layout(
            template="plotly_dark",
            height=450,
            showlegend=False,
            margin=dict(l=20, r=20, t=5, b=20),
            xaxis_title="Number of Locations",
            yaxis_title="",
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            font=dict(size=13),
            xaxis=dict(showgrid=True),
            yaxis=dict(categoryorder="total ascending")
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
            config={
                "displayModeBar": False
            }
        )

# ============================================================
# AI Environmental Assessment
# ============================================================

st.divider()

st.header("🧠 AI Environmental Assessment")

with st.container(border=True):

    st.markdown("""
### Overall Assessment

AirSense AI integrates geospatial datasets to identify spatial patterns that influence
environmental conditions across Delhi.

The combined analysis of transportation networks, industrial areas, construction
activities, sensitive locations, and land types indicates multiple potential
contributors to urban air pollution. These datasets provide the spatial foundation
for pollution source identification, environmental assessment, and future AI-based
prediction.
""")

    st.markdown("---")

    st.markdown("### 🧠 AI Insights")

    st.markdown("""
#### 🛣 Transportation Network

The road network is dominated by residential roads, indicating dense urban
connectivity and widespread vehicular movement. Transportation corridors are
likely to contribute significantly to traffic-related emissions.
""")

    st.markdown("""
#### 🏭 Industrial Areas

Industrial locations are fewer in number but represent concentrated stationary
pollution sources that require continuous environmental monitoring and emission
control.
""")

    st.markdown("""
#### 🚧 Construction & Waste

Construction and waste locations indicate localized sources of dust and particulate
matter, emphasizing the importance of dust suppression and proper waste management.
""")

    st.markdown("""
#### 🏥 Sensitive Locations

Hospitals and schools are distributed throughout Delhi, highlighting the need for
continuous air quality monitoring around environmentally sensitive areas.
""")

    st.markdown("""
#### 🌳 Land Type

The land type distribution reflects a mix of residential, commercial, institutional,
and green areas. These spatial characteristics influence pollution dispersion and
support urban environmental planning.
""")
    
# ============================================================
# AI Recommendations
# ============================================================

st.divider()

st.header("🎯 AI Recommendations")

st.markdown("""
Based on the integrated GIS analysis, AirSense AI recommends the following
strategies to improve environmental sustainability and reduce pollution risks
across Delhi.
""")

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):

        st.success("""
### 🚍 Sustainable Transportation

Promote public transportation, electric vehicles, and
non-motorized transport to reduce traffic-related emissions.
""")

        st.success("""
### 🏭 Industrial Emission Control

Strengthen emission monitoring systems and encourage
cleaner industrial technologies in major industrial zones.
""")

        st.success("""
### 🚧 Construction Management

Implement dust suppression measures, cover construction
materials, and improve waste disposal practices.
""")

with col2:
    with st.container(border=True):

        st.success("""
### 🏥 Protect Sensitive Areas

Increase AQI monitoring around schools and hospitals to
protect vulnerable populations.
""")

        st.success("""
### 🌳 Urban Green Infrastructure

Expand green belts, roadside plantations, and urban parks
to improve air quality and ecological balance.
""")

        st.success("""
### 📡 Smart Environmental Monitoring

Deploy additional IoT-based air quality sensors for
real-time environmental monitoring and AI-driven decision making.
""")
        
# ============================================================
# AI Prediction Module
# ============================================================

st.divider()

st.header("🤖 AI Prediction Module")

with st.container(border=True):

    st.success("""
### ✅ Integrated Machine Learning Model

AirSense AI integrates an XGBoost Machine Learning model with multiple
GIS-based environmental datasets to forecast Air Quality Index (AQI).

The prediction model combines historical air quality, meteorological,
satellite-derived, and environmental features to support pollution
forecasting, early warning generation, and smart-city decision making.
""")

    st.markdown("### AI Capabilities")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
✅ AQI Forecasting

✅ Pollution Trend Prediction

✅ Feature Importance Analysis

✅ Environmental Risk Assessment
""")

    with col2:

        st.markdown("""
✅ Smart City Decision Support

✅ Pollution Monitoring

✅ Environmental Pattern Recognition

✅ AI-driven Recommendations
""")

    st.page_link(
        "pages/Prediction.py",
        label="🚀 Open AQI Prediction Dashboard",
        icon="🎯"
    )

st.divider()

st.caption(
    "🌍 AirSense AI | Economic Times Hackathon 2026 | AI + GIS Based Pollution Source Identification"
)