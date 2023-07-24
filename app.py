import streamlit as st
import numpy as np
import os

@st.cache_data
def load_data():
    fps = ['power_density_mask', 'wind_speed_mask']
    names = ['Power Density', 'Wind Speed']
    data = {name: np.load(os.path.join("masks", fp + '.npy')) for fp, name in zip(fps, names)}
    return data


data = load_data()

# Header
st.title("Brazilian Wind Farm Location Scout")
# st.write("This app allows you to explore good locations for wind farms in Brazil.")


# Sidebar
st.sidebar.title("Parameters")

st.sidebar.markdown("Select the region")
region = st.sidebar.selectbox("Region", ['All', 'Northeast', 'South', 'Southeast', 'North', 'Center-West'])

# add spacing
st.sidebar.markdown("")
st.sidebar.markdown("")
st.sidebar.markdown("")

st.sidebar.markdown("Select the modality")
modality = st.sidebar.selectbox("Modality", ['Power Density', 'Wind Speed'])


# Visualization
st.image(data[modality], use_column_width=True)