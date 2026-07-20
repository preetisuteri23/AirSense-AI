import streamlit as st


def navbar():

    # ==========================================
    # HIDE STREAMLIT DEFAULT NAVIGATION
    # ==========================================

    st.markdown("""
    <style>

    /* Hide default multipage navigation */
    [data-testid="stSidebarNav"]{
        display: none;
    }

    /* Hide collapsed sidebar button (>> icon) */
    [data-testid="stSidebarCollapsedControl"]{
        display: none;
    }

    /* Hide Streamlit header */
    header{
        visibility: hidden;
    }

    </style>
    """, unsafe_allow_html=True)

    # ==========================================
    # CUSTOM NAVBAR
    # ==========================================

    with st.container():

        left, right = st.columns([2, 6])

        with left:
            st.markdown("## 🌍 AirSense AI")

        with right:

            c1, c2, c3, c4, c5, c6 = st.columns(6)

            with c1:
                st.page_link(
                    "app.py",
                    label="🏠 Home"
                )

            with c2:
                st.page_link(
                    "pages/Dashboard.py",
                    label="📊 Dashboard"
                )

            with c3:
                st.page_link(
                    "pages/Map.py",
                    label="🗺 GIS Map"
                )

            with c4:
                st.page_link(
                    "pages/AI_Analysis.py",
                    label="🤖 AI Analysis"
                )

            with c5:
                st.page_link(
                    "pages/Prediction.py",
                    label="🎯 Prediction"
                )

            with c6:
                st.page_link(
                    "pages/About.py",
                    label="ℹ️ About"
                )

    st.divider()