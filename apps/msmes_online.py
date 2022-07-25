import pandas as pd
import numpy as np
import geopandas as gpd
import json
import leafmap.kepler as leafmap
import streamlit as st

def app():
    st.subheader("Number of MSMEs Online")

    kenya_gs = gpd.read_file("data/provinces/KenyaAdmn2.shp")
    kenya_gs = kenya_gs[["geometry"]]
    kenya_gs = kenya_gs[:8]
    
    kenya_df = pd.read_excel("data/msme.xlsx", sheet_name="msmes_online")
    kenya_df["MSMEs Not Online"] = kenya_df["Number of MSMEs"] - kenya_df["MSMEs Online"]
    kenya_df["Percentage of MSMEs Online"] = round((100 * kenya_df["MSMEs Online"] / kenya_df["Number of MSMEs"]), 2)
    
    kenya = pd.concat([kenya_df, kenya_gs], axis="columns")
    kenya = gpd.GeoDataFrame(kenya)
    
    if st.checkbox("Show data"):
        st.table(kenya.loc[:, kenya.columns != "geometry"])

    province = st.sidebar.selectbox("Select a province", kenya["Province"], index=0)

    m = leafmap.Map(center=[-0.02, 37.91], zoom=5, height=600, widescreen=False)

    if st.checkbox("Filter by province"):
        index = list(kenya["Province"]).index(province)
        prov = kenya.loc[index, "Province"]
        number_of_smes = kenya.loc[index, "Number of MSMEs"]
        smes_online = kenya.loc[index, "MSMEs Online"]
        percentage_online = kenya.loc[index, "Percentage of MSMEs Online"]

        st.write(f"In {prov} province, {number_of_smes} MSMEs were interviewed, out of which {smes_online} or {percentage_online}% are online.")
        m.add_gdf(kenya[kenya["Province"] == province], layer_name=province)
    else:
        m.add_gdf(kenya, layer_name="Provinces")
    m.to_streamlit(height=500)

    hide_st_style = """
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    header {visibility: hidden;}
                    </style>
                    """
    st.markdown(hide_st_style, unsafe_allow_html=True)

