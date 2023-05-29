import streamlit as st

#### Page Configuration
st.set_page_config(page_title="Home",
                   layout="wide")
with open("./static/css/styles.css") as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)

#### Header Section
st.title("Pollutant Forecasting")

#### Main Body
st.header("Abstract")

with open("./static/textContent/Abstract.md") as f:
    st.write(*f.readlines())