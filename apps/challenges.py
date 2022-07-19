import pandas as pd
import plotly.express as px
import streamlit as st

def app():
    st.subheader("Challenges Faced by MSMEs")

    challenges_df = pd.read_csv("data/challenges.csv")

    if st.checkbox("Show data"):
        st.table(challenges_df)
    
    fig = px.bar(challenges_df, x="percentage", y="challenge", text_auto=True,
                 title="Challenges Faced by MSMEs",
                 labels = {"challenge": "Type of Challenge Faced", "percentage": "Percentage Listing That Challenge"})
    fig.update_layout(yaxis={"categoryorder":"total ascending"})
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("**NOTE: Bars with lables M1, M2 and M3 indicate missing labels in data**")
    
    hide_st_style = """
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    header {visibility: hidden;}
                    </style>
                    """
    st.markdown(hide_st_style, unsafe_allow_html=True)

