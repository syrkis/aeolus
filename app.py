import streamlit as st
import numpy as np
import os

# set wide layout
# st.set_page_config(layout="wide")

@st.cache_data
def load_data():
    fps = ['power_density_mask', 'wind_speed_mask', 'M']
    names = ['Power Density', 'Wind Speed', 'All']
    data = {name: np.load(os.path.join("masks", fp + '.npy')) for fp, name in zip(fps, names)}
    return data

def weighted_sum(data, weights):
    mask = sum([data[name] * weight for name, weight in weights.items()])
    mask = np.where(mask > 0.5, 1, 0)
    return mask


data = load_data()

# Header
st.title("Brazilian wind farm location scout")
st.write(f"""Use the explorer on the left to find potential locations for your wind farm project.
         The explorer will show you the best locations based on how you've valued Power Density, Wind Speed, Biodiversity and Roughness.
         Five of Brazil's 26 states have meterological conditions that are suitable for wind power generation.
         You can focus on a paricular state, or get a country wide overview.""")


# Sidebar
st.sidebar.title("Explorer")

# st.sidebar.markdown("Select the region")
region = st.sidebar.selectbox("Region", ['All', 'Northeast', 'South', 'Southeast', 'North', 'Center-West'])


power_density = st.sidebar.slider("Power Density", 0, 10, 5) / 10
wind_speed = st.sidebar.slider("Wind Speed", 0, 10, 5) / 10
biodiversity = st.sidebar.slider("Biodiversity", 0, 10, 5) / 10
roughness = st.sidebar.slider("Roughness", 0, 10, 5) / 10


# Create three columns for the images


# Visualization
mask = weighted_sum(data, {'Power Density': power_density, 'Wind Speed': wind_speed})
st.image(mask, caption='Final mask', use_column_width=True)

st.write(f"""The map above shows the areas that are suitable for wind power generation.
         It is a weighted sum of the maps below, where you can see the individual factors that were considered.""")


col1, col2, col3, col4 = st.columns(4)
# Display images in the three columns
col1.image(data['All'], caption='Power Density', use_column_width=True)
col2.image(data['All'], caption='Wind Speed', use_column_width=True)
col3.image(data['All'], caption='All', use_column_width=True)
col4.image(data['All'], caption='All', use_column_width=True)


# about the project
st.title("Behind the scenes")