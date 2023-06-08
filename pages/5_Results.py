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

# User Input Section


already_scaled = None

# Collecting Data
with open("./Jupyter Files/grid_et_cv2_rmse.pkl", "rb") as f:
    model = pickle.load(f)
data = pd.read_csv("./Jupyter Files/Dataset/test_borivali.csv")
# data["From Date"] = pd.to_datetime(data["From Date"], format="%d-%m-%Y %H:%M")
# data.set_index("From Date", inplace=True, drop=True)
try:
    data.drop("From Date", axis=1, inplace=True)
except:
    pass

with open("./Jupyter Files/scaler.bin", "rb") as f:
    scaler = joblib.load(f)
    already_scaled = False
og_data = pd.read_csv("./Jupyter Files/Dataset/airport_air_csv.csv")
# og_data["From Date"] = pd.to_datetime(og_data["From Date"], format="%d-%m-%Y %H:%M")
# og_data.set_index("From Date", inplace=True, drop=True)
try:
    og_data.drop("From Date", axis=1, inplace=True)
except:
    pass
# og_data.drop("PM2.5", axis=1, inplace=True)
data.interpolate(method='linear', inplace=True)

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
             caption="Parameters of Grid Search with 2-Fold Cross Validation for Hyperparameter Tuning in ET Regressor")

# USER INTERACTION SECTION
with st.container():
    st.subheader("Live Testing")
    st.write("#### Input your own data!")
    edit_data = st.experimental_data_editor(
        data.reset_index(), num_rows='dynamic')

    st.write("#### Data after user input")
    st.dataframe(edit_data)

    if already_scaled == False:
        # scaler.fit(og_data[og_data.columns[:-1]])
        scaled = pd.DataFrame(scaler.fit_transform(
            edit_data[edit_data.columns[1:-1]]))

    cols = st.columns(2)
    preds = model.predict(scaled)
    final_df = pd.DataFrame(
        {"Original PM10": edit_data[edit_data.columns[-1]].values, "Predictions": preds})
    cols[0].write("Side-by-side comparison")
    cols[0].dataframe(final_df,width=400)
    cols[1].write("Differences in Predictions and Original")
    cols[1].write(edit_data[edit_data.columns[-1]]-preds)

    st.write("Graph Visualization")
    st.line_chart(final_df, width=100, height=400)

#################
