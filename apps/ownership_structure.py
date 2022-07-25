import pandas as pd
import plotly.express as px
import streamlit as st

def app():
    st.subheader("Online by Ownership Structure")

    support_df = pd.read_excel("data/msme.xlsx", sheet_name="ownership_structure")

    if st.checkbox("Show data"):
        st.table(support_df)
    
    fig = px.bar(support_df, x="percentage", y="ownership_structure", text_auto=True,
                 title="Percentage of MSMEs Online by Ownership Structure",
                 labels = {"ownership_structure": "Ownership Structure", "percentage": "Percentage Online"})
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

