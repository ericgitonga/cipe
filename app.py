import streamlit as st
from streamlit_option_menu import option_menu
from apps import home, msmes_online, support, challenges, sector, digitech_adoption

st.set_page_config(page_title="MSME Digital Economy Survey Report", layout="wide")

apps = [
         {"func": home.app, "title": "Home", "icon": "house"},
         {"func": msmes_online.app, "title": "Number of MSMEs Online", "icon": "geo-alt-fill"},
         {"func": support.app, "title": "Support Needed by MSMEs", "icon": "tools"},
         {"func": challenges.app, "title": "Challenges Faced by MSMEs", "icon": "exclamation-circle-fill"},
         {"func": sector.app, "title": "MSMEs Online by Sector", "icon": "list-columns"},
         {"func": digitech_adoption.app, "title": "Digital Technology MSMEs Might Adopt in Future", "icon": "pc-display-horizontal"},
]

titles = [app["title"] for app in apps]
titles_lower = [title.lower() for title in titles]
icons = [app["icon"] for app in apps]

params = st.experimental_get_query_params()

if "page" in params:
    default_index = int(titles_lower.index(params["page"][0].lower()))
else:
    default_index = 0

with st.sidebar:
    selected = option_menu(
        "Main Menu",
        options=titles,
        icons=icons,
        menu_icon="cast",
        default_index=default_index,
    )
    
for app in apps:
    if app["title"] == selected:
        app["func"]()
        break

hide_st_style = """
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    header {visibility: hidden;}
                    </style>
                    """
