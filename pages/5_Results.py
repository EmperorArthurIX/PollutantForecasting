import joblib
import pandas as pd
import pickle
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

# Collecting Data
with open("./Jupyter Files/et_pm25_gscv_ccp_md_mss_msl_ne.pkl", "rb") as f:
    model = pickle.load(f)
data = pd.read_csv("./Jupyter Files/Dataset/test_borivali.csv")

try:
    data.drop("From Date", axis=1, inplace=True)
    data.drop("BP", axis=1, inplace=True)
    data.dropna(inplace=True)
except:
    pass

og_data = pd.read_csv("./Jupyter Files/Dataset/airport_air_csv.csv")

try:
    og_data.drop("From Date", axis=1, inplace=True)
    og_data.drop("BP", axis=1, inplace=True)
    og_data.dropna(inplace=True)
except:
    pass


##################
with st.container():
    st.subheader(
        "Comparing regressors trained With and Without PM2.5 values known")
    from PIL import Image
    cols = st.columns(2)
    cols[0].image(Image.open("./static/media/prediction_error_2.5.png"),
                  caption="Predictions by regressor trained with PM2.5")
    cols[1].image(Image.open("./static/media/prediction_error.png"),
                  caption="Predictions by regressor trained without PM2.5")
    cols[0].image(Image.open("./static/media/residual 2.5.jpg"),
                  caption="Residuals and Residual Distribution for regressor trained with PM2.5")
    cols[1].image(Image.open("./static/media/residuals.png"),
                  caption="Residuals and Residual Distribution for regressor trained without PM2.5")

with st.container():
    st.subheader("Comparing Pruned and Un-Pruned Extra Trees Regressor")
    from PIL import Image
    cols = st.columns(2)
    cols[0].image(Image.open("./static/media/learning 2.5.jpg"),
                  caption="Validation Curve of Un-Pruned ET Regressor")
    cols[1].image(Image.open("./static/media/validation.jpg"),
                  caption="Validation Curve of Pruned ET Regressor")

with st.container():
    st.subheader("Grid Search Overview")
    from PIL import Image
    st.image(Image.open("./static/media/grid ET.jpg"),
             caption="Parameters of Grid Search with 2-Fold Cross Validation for Hyperparameter Tuning in Preliminary ET Regressor")
    st.image(Image.open("./static/media/newgridet.jpg"),
                  caption="Parameters of Grid Search with 10-Fold Repeated Cross Validation for Hyperparameter Tuning in the Final ET Regressor")

# USER INTERACTION SECTION
with st.container():
    st.subheader("Live Testing")
    st.write("#### Input your own data!")
    edit_data = st.experimental_data_editor(
        data.reset_index(), num_rows='dynamic')

    st.write("#### Data after user input")
    st.dataframe(edit_data)

    scaled = edit_data[edit_data.columns[1:-1]]
    cols = st.columns(2)
    preds = model.predict(scaled)

    with st.container():
        final_df = pd.DataFrame()
        final_df["Original PM10"] = edit_data[edit_data.columns[-1]].values
        final_df["Predictions"] = preds
        final_df["Error"] =  edit_data[edit_data.columns[-1]]-preds
        final_df["Absolute Error"] = abs(final_df["Error"])
        final_df["% Error (over range 0 to 400)"] = final_df["Absolute Error"]/4
        st.dataframe(final_df)

    st.write("Graph Visualization")
    st.line_chart(final_df, y=["Original PM10", "Predictions"], width=100, height=400)
    st.bar_chart(edit_data[edit_data.columns[-1]]-preds)

#################
