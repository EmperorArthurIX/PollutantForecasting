import streamlit as st

#### Page Configuration
st.set_page_config(page_title="Model Selection",
                   layout="wide")
with open("./static/css/styles.css") as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)

#### Header Section
st.title("Model Selection")

#### Main Body
with open("./static/textContent/ModelSelection.md") as f:
    st.markdown(f.read(), unsafe_allow_html=True)