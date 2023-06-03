import streamlit as st

# Page Configuration
st.set_page_config(page_title="Literature Review",
                   layout="wide")
with open("./static/css/styles.css") as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# Header Section
st.title("Literature Review")

# Main Body
with open("./static/textContent/LiteratureReview.md") as f:
    st.markdown(f.read(), unsafe_allow_html=True)
