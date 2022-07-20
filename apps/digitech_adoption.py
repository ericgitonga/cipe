import pandas as pd
import plotly.express as px
import streamlit as st

def app():
    st.subheader("Digital Technology Adopted by MSMEs")

    digitech_df = pd.read_csv("data/digitech_adoption.csv")

    if st.checkbox("Show data"):
        st.table(digitech_df)
    
    fig = px.bar(digitech_df, x="percentage", y="digital_technology", text_auto=True,
                 title="Digital Technology Adopted by MSMEs",
                 labels = {"digital_technology": "Type of Digital Technology", "percentage": "Percentage Using That Digital Technology"})
    fig.update_layout(yaxis={"categoryorder":"total ascending"})
    fig.update_xaxes(showticklabels=False, showgrid=False)
    st.plotly_chart(fig, use_container_width=True)

    hide_st_style = """
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    header {visibility: hidden;}
                    </style>
                    """
    st.markdown(hide_st_style, unsafe_allow_html=True)

