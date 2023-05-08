import streamlit as st
import predict_page as pp
#pp.show_predict_page()
import time
from explore_page import show_explore_page

with st.sidebar:
    page = st.radio(
        "Choose the option to go",
        ("Predict", "📈 Explore")
    )
    with st.spinner("Loading..."):
        time.sleep(0.5)
    st.success("Done!")
#page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

if page == "Predict":
    pp.show_predict_page()
else:
    show_explore_page()