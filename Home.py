import streamlit as st
import geopandas as gpd
import folium
from streamlit_folium import st_folium
from utils.navbar import navbar
# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="AirSense AI",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# LOAD CSS
# ==========================================

with open("styles/style.css") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)


# ==========================================
# LOAD GEOJSON DATASETS
# ==========================================

roads = gpd.read_file("DATA/CLEANED/Delhi_Road_Network_cleaned.geojson")
industrial = gpd.read_file("DATA/CLEANED/cleaned_industrial.geojson")
construction = gpd.read_file("DATA/CLEANED/cleaned_construction_waste.geojson")
sensitive = gpd.read_file("DATA/CLEANED/cleaned_sensitive_locations.geojson")
landuse = gpd.read_file("DATA/CLEANED/Delhi_Land_Use_cleaned.geojson")

navbar()

# =====================================================
# HERO SECTION
# =====================================================

left, right = st.columns([1.45, 1], gap="large")

# -----------------------------------------------------
# LEFT
# -----------------------------------------------------

with left:

    st.markdown("""
    <p style="
        color:#4CAF50;
        font-size:15px;
        font-weight:600;
        letter-spacing:1px;
        margin-bottom:0;">
        ENVIRONMENTAL INTELLIGENCE PLATFORM
    </p>
    """, unsafe_allow_html=True)

    st.markdown("""
    <h1 style="
        font-size:60px;
        margin-top:0px;
        margin-bottom:5px;">
        AirSense AI
    </h1>
    """, unsafe_allow_html=True)

    st.markdown("""
    <h3 style="
        color:#4CAF50;
        font-weight:600;
        margin-top:0;">
        AI + GIS Powered Pollution Source Identification
    </h3>
    """, unsafe_allow_html=True)

    st.markdown("""
**Transform environmental data into actionable intelligence.**

AirSense AI integrates Artificial Intelligence (AI), Geographic Information
Systems (GIS), and multi-source environmental datasets to identify pollution
sources, support sustainable urban planning, and enable future AI-driven
environmental prediction.
""")

    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

    c1, c2 = st.columns([1,1])

    with c1:
        st.page_link(
            "pages/Dashboard.py",
            label="📊 Explore Dashboard →"
        )

    with c2:
        st.page_link(
            "pages/About.py",
            label="📖 Learn More →"
        )
# -----------------------------------------------------
# RIGHT
# -----------------------------------------------------

with right:

    with st.container(border=True):

        st.markdown("## 🌿 Environmental Intelligence")
        st.divider()

        st.markdown("🗺 **GIS Spatial Analysis**")
        st.caption("Interactive mapping of environmental datasets")

        st.markdown("📊 **Multi-Source Data Integration**")
        st.caption("Roads • Land Use • Industry • AQI • Weather • Satellite")
        
        st.markdown("🤖 **AI Environmental Assessment**")
        st.caption("Identify potential pollution sources")

        st.markdown("📈 **Prediction Module**")
        st.caption("Machine learning-based pollution forecasting.")


# =====================================================
# INTEGRATED ENVIRONMENTAL INTELLIGENCE
# =====================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<h2 style="text-align:center;">
Integrated Environmental Intelligence
</h2>
""", unsafe_allow_html=True)

st.markdown("""
<p style="
text-align:center;
color:#B8C5D6;
font-size:18px;
max-width:900px;
margin:auto;
">
AirSense AI integrates geospatial intelligence with environmental data to
provide a comprehensive understanding of urban pollution and support
evidence-based environmental decision making.
</p>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

geo_col, env_col = st.columns([1,1], gap="large")

# =====================================================
# GEOSPATIAL INTELLIGENCE
# =====================================================

with geo_col:

    with st.container(border=True):

        st.subheader("🗺 Geospatial Intelligence")

        st.caption("Core GIS datasets powering the platform")

        st.divider()

        data = [
            ("🛣", "Road Network", len(roads)),
            ("🏭", "Industrial Areas", len(industrial)),
            ("🏥", "Sensitive Locations", len(sensitive)),
            ("🚧", "Construction & Waste", len(construction)),
            ("🌳", "Land Use", len(landuse)),
        ]

        for icon, name, value in data:

            c1, c2 = st.columns([4,1])

            with c1:
                st.markdown(f"**{icon} {name}**")

            with c2:
                st.markdown(
                    f"<div style='text-align:right; font-weight:700; color:#27C2FF;'>{value:,}</div>",
                    unsafe_allow_html=True,
                )

            st.divider()

# =====================================================
# ENVIRONMENTAL INTELLIGENCE
# =====================================================

with env_col:

    with st.container(border=True):

        st.subheader("🌍 Environmental Intelligence")

        st.caption("Integrated environmental information")

        st.divider()

        st.markdown("""
##### 🌫 Historical AQI

Long-term air quality observations used for environmental analysis.
""")

        st.markdown("""
##### 🛣 Transportation Network

Road network information supporting pollution source analysis.
""")

        st.markdown("""
##### 🌦 Weather Conditions

Meteorological variables influencing air quality patterns.
""")

        st.markdown("""
##### 🛰 Satellite Observations

Remote sensing information for environmental monitoring.
""")

        st.markdown("""
##### 🤖 Machine Learning

Machine learning models for pollution forecasting and environmental intelligence.

""")

        st.info(
            "Supporting smarter environmental monitoring, sustainable urban planning, and evidence-based decision making."
        )

# =====================================================
# WHAT AIRSENSE AI CAN DO
# =====================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<h2 style="text-align:center;">
What AirSense AI Can Do
</h2>
""", unsafe_allow_html=True)

st.markdown("""
<p style="
text-align:center;
color:#B8C5D6;
font-size:18px;
max-width:850px;
margin:auto;
">
AirSense AI transforms geospatial and environmental datasets into actionable
insights that support pollution monitoring, environmental analysis, and
smarter urban decision making.
</p>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# -----------------------------------------------------
# FEATURE CARDS
# -----------------------------------------------------

col1, col2, col3 = st.columns(3, gap="large")

# ---------------- CARD 1 ----------------

with col1:

    with st.container(border=True):

        st.markdown("## 🗺")

        st.subheader("Interactive GIS Mapping")

        st.write(
            "Visualize road networks, industrial areas, land use, "
            "construction sites, and sensitive locations through "
            "interactive spatial analysis."
        )

# ---------------- CARD 2 ----------------

with col2:

    with st.container(border=True):

        st.markdown("## 🤖")

        st.subheader("AI Environmental Assessment")

        st.write(
            "Analyze integrated environmental datasets to identify "
            "potential pollution sources and understand urban pollution patterns."
        )

# ---------------- CARD 3 ----------------

with col3:

    with st.container(border=True):

        st.markdown("## 📊")

        st.subheader("Environmental Analytics")

        st.write(
            "Transform environmental information into meaningful insights "
            "through intelligent data exploration."
        )

st.markdown("<br>", unsafe_allow_html=True)

# -----------------------------------------------------
# SECOND ROW
# -----------------------------------------------------

col4, col5, col6 = st.columns(3, gap="large")

# ---------------- CARD 4 ----------------

with col4:

    with st.container(border=True):

        st.markdown("## 🏙")

        st.subheader("Urban Decision Support")

        st.write(
            "Support sustainable urban planning with data-driven "
            "environmental intelligence."
        )

# ---------------- CARD 5 ----------------

with col5:

    with st.container(border=True):

        st.markdown("## 🌍")

        st.subheader("Multi-Source Integration")

        st.write(
            "Combine GIS, AQI, weather, satellite observations, "
            "road network, and machine learning into one platform."
        )

# ---------------- CARD 6 ----------------

with col6:

    with st.container(border=True):

        st.markdown("## 📈")

        st.subheader("Pollution Forecasting")

        st.write(
            "Generate AI-powered pollution predictions using integrated "
            "environmental datasets."
        )

# =====================================================
# EXPLORE AIRSENSE AI
# =====================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<h2 style="text-align:center;">
Explore AirSense AI
</h2>
""", unsafe_allow_html=True)

st.markdown("""
<p style="
text-align:center;
color:#B8C5D6;
font-size:18px;
max-width:850px;
margin:auto;
">
Navigate through the different modules of AirSense AI to explore
environmental datasets, interactive GIS visualizations, AI-powered analysis,
and pollution forecasting.
</p>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ----------------------------------------------------
# FIRST ROW
# ----------------------------------------------------

c1, c2, c3 = st.columns(3, gap="large")

# Dashboard

with c1:

    with st.container(border=True):

        st.markdown("## 📊")

        st.subheader("Dashboard")

        st.write(
            "Explore interactive environmental analytics and dataset summaries."
        )

        st.page_link(
            "pages/Dashboard.py",
            label="Open Dashboard →"
        )

# GIS

with c2:

    with st.container(border=True):

        st.markdown("## 🗺")

        st.subheader("GIS Map")

        st.write(
            "Visualize environmental datasets using interactive geospatial mapping."
        )

        st.page_link(
            "pages/Map.py",
            label="Open GIS Map →"
        )

# AI

with c3:

    with st.container(border=True):

        st.markdown("## 🤖")

        st.subheader("AI Analysis")

        st.write(
            "Identify potential pollution sources using integrated environmental intelligence."
        )

        st.page_link(
            "pages/AI_Analysis.py",
            label="Open AI Analysis →"
        )

st.markdown("<br>", unsafe_allow_html=True)

# ----------------------------------------------------
# SECOND ROW
# ----------------------------------------------------

c4, c5 = st.columns(2, gap="large")

# Prediction

with c4:

    with st.container(border=True):

        st.markdown("## 📈")

        st.subheader("Prediction")

        st.write(
            "Generate AI-powered pollution forecasts using machine learning."
        )

        st.page_link(
            "pages/Prediction.py",
            label="Open Prediction →"
        )

# About

with c5:

    with st.container(border=True):

        st.markdown("## ℹ")

        st.subheader("About Project")

        st.write(
            "Learn about the project, technologies, datasets, and development process."
        )

        st.page_link(
            "pages/About.py",
            label="Learn More →"
        )

# =====================================================
# FOOTER
# =====================================================

st.markdown("<br><br><br>", unsafe_allow_html=True)

st.divider()

c1, c2 = st.columns([2, 1])

# -----------------------------------------------------
# LEFT
# -----------------------------------------------------

with c1:

    st.markdown("""
### 🌍 AirSense AI
""")

    st.caption("""
AI + GIS Powered Pollution Source Identification

Building smarter environmental intelligence through
Artificial Intelligence, Geographic Information Systems,
and multi-source environmental datasets.
""")

# -----------------------------------------------------
# RIGHT
# -----------------------------------------------------

with c2:

    st.markdown("#### Quick Access")

    st.page_link("pages/Dashboard.py", label="📊 Dashboard")

    st.page_link("pages/Map.py", label="🗺 GIS Map")

    st.page_link("pages/AI_Analysis.py", label="🤖 AI Analysis")

    st.page_link("pages/Prediction.py", label="📈 Prediction")

    st.page_link("pages/About.py", label="ℹ About Project")

st.markdown("<br>", unsafe_allow_html=True)

st.caption(
    "© 2026 AirSense AI • Built for the Economic Times Hackathon • "
    "AI • GIS • Environmental Intelligence"
)