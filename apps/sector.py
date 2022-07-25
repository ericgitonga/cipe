import pandas as pd
import plotly.express as px
import streamlit as st

def app():
    st.subheader("MSMEs Online by Sector")

    sector_df = pd.read_excel("data/msme.xlsx", sheet_name="sector")

    if st.checkbox("Show data"):
        st.table(sector_df)
    
    fig = px.bar(sector_df, x="percentage", y="sector", text_auto=True,
                 title="Percentage of MSMEs Online by Sector",
                 labels = {"sector": "Sector", "percentage": "Percentage Online"})
    fig.update_layout(yaxis={"categoryorder":"total ascending"})
    fig.update_xaxes(showticklabels=False, showgrid=False)
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("**NOTE: Bars with lables M1, M2, M3, M4, M5 and M6 indicate missing labels in data**")
    
    hide_st_style = """
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    header {visibility: hidden;}
                    </style>
                    """
    st.markdown(hide_st_style, unsafe_allow_html=True)

