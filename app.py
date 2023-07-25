import streamlit as st
import numpy as np
import os

# set wide layout
# st.set_page_config(layout="wide")

@st.cache_data
def load_data():
    fps = ['power_density', 'powerlines', 'population_mask', 'wind_speed', 'protected_areas_mask', 'airport_mask', 'slope_mask', 'roughness', 'brazil_mask']
    names = ['Power Density', 'Power Lines', 'Population', 'Wind Speed', 'Protected Areas', 'Airports', 'Slope', 'Roughness', 'Brazil']
    data = {name: np.load(os.path.join("masks", fp + '.npy')).astype(float) for fp, name in zip(fps, names)}
    data['Power Density'] /= (data['Power Density'].max() / 100)
    data['Population'] /= (data['Population'].max() / 100)
    data['Roughness'] = data['Roughness'] * data['Brazil']
    data['Roughness'] /= (data['Roughness'].max() / 100)
    return data

def make_mask(data, thresholds):
    mask = np.ones_like(data['Power Density'])
    for key, threshold in thresholds.items():
        # if key in ['']
        mask *= data[key] > threshold
    return mask

def make_mask(frame, theshold=None, over=True):
    if theshold and over:
        frame = frame > theshold
    elif theshold and not over:
        frame = frame < theshold
    frame = frame.astype(float)
    frame /= frame.max()
    return frame



all_data = load_data()

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

data = all_data


st.sidebar.markdown("Select factor thresholds")
power_density = st.sidebar.slider("Power density (percentile)", 0, 100, 50) + 1
grid_distance = 31  - st.sidebar.slider("Grid distance (km)", 0, 30, 10)
# population = 101 - st.sidebar.slider("Population count", 0, 100, 50)
roughness = st.sidebar.slider("Rougness (percentile)", 0, 100, 50) + 1
wind_speed = st.sidebar.slider("Minimum wind speed (m/s)", 5, 10, 7) - 1

# Create three columns for the images
power_density_mask = make_mask(data['Power Density'], power_density)
grid_distance_mask = make_mask(data['Power Lines'], grid_distance)
# population_mask = make_mask(data['Population'], population)
roughness_mask = make_mask(data['Roughness'], roughness)
wind_speed_mask = make_mask(data['Wind Speed'], wind_speed)

final_mask = (data['Brazil'] * power_density_mask * grid_distance_mask * roughness_mask * wind_speed_mask).astype(float)


# Visualization
# mask = make_mask(data, {'Power Density': power_density, 'Wind Speed': wind_speed})
st.image(final_mask, caption='Final mask', use_column_width=True)

st.write(f"""The map above shows the areas that are suitable for wind power generation.
         It is a weighted sum of the maps below, where you can see the individual factors that were considered.""")


col1, col2, col4, col5 = st.columns(4)

# Display images in the three columns
col1.image(power_density_mask, caption='Power Density', use_column_width=True)
col2.image(grid_distance_mask, caption='Power Lines', use_column_width=True)
# col3.image(population_mask, caption='Population', use_column_width=True)
col4.image(roughness_mask, caption='Roughness', use_column_width=True)
col5.image(wind_speed_mask, caption='Wind Speed', use_column_width=True)


# about the project
st.title("More info on the map construction")
st.write(f"""In addition to the modalities that you control,
        the map also excludes areas that are not suitable for wind power generation,
        biodiversity conservation areas and areas with high roughness, and population.
         The constraints and the base topography can be seen below.""")

# new columns
col1, col2, col3 = st.columns(3)


col1.image(data['Airports'], caption='Airports', use_column_width=True)
col2.image(data['Protected Areas'], caption='Protected Areas', use_column_width=True)
col3.image(data['Slope'], caption='Slope', use_column_width=True)


# footer
st.write(f"""For more information on the potential of wind power generation in Brazil,
        contact the [Brazilian Climate Center.](https://doe.climatempo.com.br/cbc)""")
