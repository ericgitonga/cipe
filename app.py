import streamlit as st
from streamlit_option_menu import option_menu
from pages import msmes_online

st.set_page_config(page_title="MSME Digital Economy Survey Report", layout="wide")

pages = {
         "home": {"title": "Home", "icon": "house"},
         "01_msmes_online": {"title": "Number of MSMEs Online", "icon": "map"},
}

titles = [page["title"] for page in pages.values()]
icons = [page["icon"] for page in pages.values()]

st.markdown("## MSME Digital Economy Survey Report")
st.write("Visualizations for the report")

