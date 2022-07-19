import streamlit as st

def app():
    st.title("Home")

    st.markdown("### Visualizing MSME Digital Report Data")
    
    hide_st_style = """
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    header {visibility: hidden;}
                    </style>
                    """
    st.markdown(hide_st_style, unsafe_allow_html=True)

