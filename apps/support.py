import pandas as pd
import plotly.express as px
import streamlit as st

def app():
    st.subheader("Support Needed by MSMEs")

    support_df = pd.read_excel("data/msme.xlsx", sheet_name="support")

    if st.checkbox("Show data"):
        st.table(support_df)
    
    fig = px.bar(support_df, x="percentage", y="support", text_auto=True,
                 title="Support for MSMEs to Go Online",
                 labels = {"support": "Type of Support", "percentage": "Percentage Listing That Support"})
    fig.update_layout(yaxis={"categoryorder":"total ascending"})
    fig.update_xaxes(showticklabels=False, showgrid=False)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("**NOTE: Label with asterisk not accurate due to being cut off in the PDF report**")
        
    hide_st_style = """
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    header {visibility: hidden;}
                    </style>
                    """
    st.markdown(hide_st_style, unsafe_allow_html=True)

