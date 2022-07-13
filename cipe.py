import pandas as pd
import numpy as np
import geopandas as gpd
import json
import leafmap.kepler as leafmap
import streamlit as st

st.markdown("#### Micro, Small & Medium Enterprises Digital Economy Survey Report")

kenya = gpd.read_file("data/provinces/KenyaAdmn2.shp")

kenya = kenya[["ADMIN2", "geometry"]]
kenya.rename(columns={"ADMIN2": "Province"}, inplace=True)
kenya = kenya[:8]

kenya["Province"] = ["Rift Valley", "Eastern", "North Eastern", "Western",
                     "Nyanza", "Central", "Coast", "Nairobi"]
kenya["Number of MSMEs"] = [156, 264, 152, 148, 121, 145, 149, 145]
kenya["MSMEs Online"] = [55, 183, 10, 74, 62, 51, 81, 134]
kenya["Percentage of MSMEs Online"] = round((100 * kenya["MSMEs Online"] / kenya["Number of MSMEs"]), 2)

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

