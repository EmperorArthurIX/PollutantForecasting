import streamlit as st

# Page Configuration
st.set_page_config(page_title="Results",
                   layout="wide")
with open("./static/css/styles.css") as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# Header Section
st.title("Results")

# Main Body
with open("./static/textContent/Results.md") as f:
    st.markdown(f.read(), unsafe_allow_html=True)

# User Input Section

st.subheader("Predicting PM10 Values")

import pickle
import pandas as pd
import joblib
with open("./Jupyter Files/et_model.pkl", "rb") as f:
    model = pickle.load(f)
data = pd.read_csv("./Jupyter Files/Dataset/test_data.csv")
data["From Date"] = pd.to_datetime(data["From Date"], format="%d-%m-%Y %H:%M")
data.set_index("From Date", inplace=True, drop=True)
with open("./Jupyter Files/scaler.bin", "rb") as f:
    scaler = joblib.load(f)
og_data = pd.read_csv("./Jupyter Files/Dataset/airport_air_csv.csv")
og_data["From Date"] = pd.to_datetime(og_data["From Date"], format="%d-%m-%Y %H:%M")
og_data.set_index("From Date", inplace=True, drop=True)
og_data.drop("PM2.5", axis=1, inplace=True)
scaler.fit(og_data[og_data.columns[:-1]])
scaled = pd.DataFrame(scaler.transform(data[data.columns[:-1]]))
preds = model.predict(scaled)
st.write(data[data.columns[-1]],preds)