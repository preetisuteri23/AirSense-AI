import streamlit as st
import geopandas as gpd
import folium
from streamlit_folium import st_folium
from pathlib import Path
import numpy as np
from utils.navbar import navbar

st.set_page_config(
    page_title="Pollution Source Map",
    page_icon="🗺️",
    layout="wide"
)

navbar()

BASE_DIR = Path(__file__).resolve().parent.parent

css_path = BASE_DIR / "styles" / "style.css"

with open(css_path) as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)
DATA_DIR = BASE_DIR / "DATA" / "CLEANED"

industrial = gpd.read_file(DATA_DIR / "cleaned_industrial.geojson")

sensitive = gpd.read_file(DATA_DIR / "cleaned_sensitive_locations.geojson")

construction = gpd.read_file(DATA_DIR / "cleaned_construction_waste.geojson")

road = gpd.read_file(DATA_DIR / "Delhi_Road_Network_cleaned.geojson")

landuse = gpd.read_file(DATA_DIR / "Delhi_Land_Use_cleaned.geojson")

ward = gpd.read_file(DATA_DIR / "Delhi_Wards.geojson")

st.title("🗺 Pollution Source Identification Map")

st.write(
    """
    Explore pollution-related datasets using GIS to identify
    potential pollution sources and environmental hotspots.
    """
)

st.divider()

m = folium.Map(
    location=[28.61, 77.23],
    zoom_start=11,
    tiles="CartoDB Positron"
)

industrial_layer = folium.FeatureGroup(name="🏭 Industrial Areas")

folium.GeoJson(
    industrial,
    style_function=lambda x: {
        "color": "#1f77b4",
        "weight": 2,
        "fillColor": "#1f77b4",
        "fillOpacity": 0.5
    },
    tooltip="Industrial Area"
).add_to(industrial_layer)

industrial_layer.add_to(m)

# =====================================================
# SENSITIVE LOCATIONS
# =====================================================

# Remove empty geometries
sensitive = sensitive[~sensitive.geometry.is_empty].copy()

sensitive_layer = folium.FeatureGroup(
    name="🏥 Sensitive Locations"
)

folium.GeoJson(
    sensitive,
    style_function=lambda feature: {
        "color": "#FF6B6B",
        "weight": 1,
        "fillColor": "#FF6B6B",
        "fillOpacity": 0.35
    },
    highlight_function=lambda feature: {
        "weight": 3,
        "color": "#B71C1C",
        "fillOpacity": 0.9,
    },
    tooltip=folium.GeoJsonTooltip(
        fields=["name", "amenity"],
        aliases=["Name", "Category"],
        sticky=True
    ),
    popup=folium.GeoJsonPopup(
        fields=["name", "amenity"],
        aliases=["Name", "Category"],
        labels=True,
        localize=True
    )
).add_to(sensitive_layer)

sensitive_layer.add_to(m)

# =====================================================
# CONSTRUCTION SITES
# =====================================================

construction = construction[~construction.geometry.is_empty].copy()

construction_layer = folium.FeatureGroup(
    name="🚧 Construction Sites"
)

folium.GeoJson(
    construction,
    style_function=lambda feature: {
        "color": "#FF8C00",
        "weight": 2,
        "fillColor": "#FFA500",
        "fillOpacity": 0.75,
    },
    highlight_function=lambda feature: {
        "weight": 3,
        "color": "#E65100",
        "fillOpacity": 0.80,
    },
    tooltip=folium.GeoJsonTooltip(
        fields=["name", "category"],
        aliases=["Name", "Category"],
        sticky=True
    ),
    popup=folium.GeoJsonPopup(
        fields=["name", "construction", "waste", "category"],
        aliases=[
            "Name",
            "Construction",
            "Waste",
            "Category"
        ],
        labels=True
    )
).add_to(construction_layer)

construction_layer.add_to(m)

# =====================================================
# ROAD NETWORK
# =====================================================



# Remove empty geometries
road = road[~road.geometry.is_empty].copy()

# Keep only major roads
road = road[
    road["highway"].astype(str).str.contains(
        "primary|secondary|trunk|motorway",
        case=False,
        na=False
    )
].copy()

# Keep only required columns
road = road[
    ["name", "highway", "lanes", "maxspeed", "geometry"]
].copy()

# Convert numpy arrays/lists into strings
def clean_value(x):
    if isinstance(x, np.ndarray):
        return ", ".join(map(str, x))
    elif isinstance(x, list):
        return ", ".join(map(str, x))
    elif x is None:
        return "Unknown"
    else:
        return str(x)

road["name"] = road["name"].apply(clean_value)
road["highway"] = road["highway"].apply(clean_value)
road["lanes"] = road["lanes"].apply(clean_value)
road["maxspeed"] = road["maxspeed"].apply(clean_value)

road_layer = folium.FeatureGroup(name="🛣 Road Network", show=False)

folium.GeoJson(
    road,
    style_function=lambda feature: {
        "color": "#808080",
        "weight":1.2,
        "opacity": 0.45,
    },
    highlight_function=lambda feature: {
        "color": "#000000",
        "weight": 2.5,
    },
    tooltip=folium.GeoJsonTooltip(
        fields=["name", "highway"],
        aliases=["Road", "Type"],
        sticky=True
    ),
    popup=folium.GeoJsonPopup(
        fields=["name", "highway", "lanes", "maxspeed"],
        aliases=[
            "Road Name",
            "Road Type",
            "Lanes",
            "Max Speed"
        ],
        labels=True
    )
).add_to(road_layer)

road_layer.add_to(m)

# =====================================================
# LAND USE
# =====================================================

# Remove empty geometries
landuse = landuse[~landuse.geometry.is_empty].copy()

# Keep only required columns
landuse = landuse[["Land_Type", "name", "geometry"]].copy()

# Fill missing names
landuse["name"] = landuse["name"].fillna("Unknown")
landuse["Land_Type"] = landuse["Land_Type"].fillna("Unknown")

# Color palette
land_colors = {
    "residential": "#2ECC71",
    "commercial": "#3498DB",
    "industrial": "#8E44AD",
    "retail": "#F39C12",
    "construction": "#FF8C00",
    "forest": "#145A32",
    "grass": "#58D68D",
    "grassland": "#7DCEA0",
    "meadow": "#82E0AA",
    "wood": "#1E8449",
    "farmland": "#D4AC0D",
    "farmyard": "#CA6F1E",
    "farmplots": "#F7DC6F",
    "greenfield": "#27AE60",
    "plant_nursery": "#52BE80",
    "greenhouse_horticulture": "#73C6B6",
    "wetland": "#5DADE2",
    "water": "#3498DB",
    "reservoir": "#5DADE2",
    "basin": "#85C1E9",
    "railway": "#566573",
    "government": "#5B2C6F",
    "institutional": "#7D3C98",
    "education": "#AF7AC5",
    "religious": "#E74C3C",
    "place_of_worship": "#EC7063",
    "cemetery": "#616A6B",
    "military": "#34495E",
    "recreation_ground": "#82E0AA",
    "brownfield": "#A04000",
    "scrub": "#7FB069",
    "depot": "#7B7D7D",
    "allotments": "#A9DFBF",
    "civic": "#7F8C8D",
    "cultural_centre": "#BB8FCE",
    "Event Venue": "#F5B041",
    "Mela Ground": "#F8C471"
}

landuse_layer = folium.FeatureGroup(
    name="🌳 Land Use",
    show=False
)

folium.GeoJson(
    landuse,
    style_function=lambda feature: {
        "fillColor": land_colors.get(
            feature["properties"]["Land_Type"],
            "#BDC3C7"
        ),
        "color": land_colors.get(
            feature["properties"]["Land_Type"],
            "#BDC3C7"
        ),
        "weight": 1,
        "fillOpacity": 0.35,
    },
    highlight_function=lambda feature: {
        "weight": 2,
        "fillOpacity": 0.7,
        "color": "#000000",
    },
    tooltip=folium.GeoJsonTooltip(
        fields=["Land_Type", "name"],
        aliases=["Land Type", "Name"],
        sticky=True
    ),
    popup=folium.GeoJsonPopup(
        fields=["Land_Type", "name"],
        aliases=["Land Type", "Name"],
        labels=True
    )
).add_to(landuse_layer)

landuse_layer.add_to(m)

# =====================================================
# WARD BOUNDARIES
# =====================================================

ward = ward[~ward.geometry.is_empty].copy()

# Fill missing values safely
if "Ward_Name" in ward.columns:
    ward["Ward_Name"] = ward["Ward_Name"].fillna("Unknown Ward")

if "Ward_No" in ward.columns:
    ward["Ward_No"] = ward["Ward_No"].fillna("-")

ward_layer = folium.FeatureGroup(
    name="🗺 Ward Boundaries",
    show=False
)

folium.GeoJson(
    ward,
    style_function=lambda feature: {
        "fillColor": "#FFFFFF",
        "color": "#FFFFFF",
        "weight": 1,
        "fillOpacity": 0
    },
    highlight_function=lambda feature: {
        "color": "#00FFFF",
        "weight": 3,
        "fillOpacity": 0.15
    },
    tooltip=folium.GeoJsonTooltip(
        fields=["Ward_Name"],
        aliases=["Ward"],
        sticky=True
    ),
    popup=folium.GeoJsonPopup(
        fields=["Ward_Name", "Ward_No"],
        aliases=[
            "Ward Name",
            "Ward Number"
        ],
        labels=True
    )
).add_to(ward_layer)

ward_layer.add_to(m)

folium.LayerControl(collapsed=False).add_to(m)

st_folium(
    m,
    width=1200,
    height=650
)

