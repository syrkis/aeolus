import streamlit as st
import numpy as np
import os

# set wide layout
st.set_page_config(layout="wide")

@st.cache_data
def load_data():
    fps = ['power_density', 'powerlines', 'population_mask', 'wind_speed', 'protected_areas_mask', 'airport_mask', 'slope_mask', 'roughness', 'brazil_mask', 'offshore_mask']
    names = ['Power Density', 'Power Lines', 'Population', 'Wind Speed', 'Protected Areas', 'Airports', 'Slope', 'Roughness', 'Brazil', 'Offshore']
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

def make_mask(frame, theshold=None):
    frame = frame > theshold
    frame = frame.astype(float)
    frame /= frame.max()
    return frame

def mask_ratio(mask):
    return mask.sum() / data['Brazil'].sum()
    

data = load_data()

# Header
st.title("Brazilian wind farm location scout")
st.write(f"""Tweak the modality thresholds below to find potential locations for wind farm projects.
         The explorer will show you the best locations based on how you've valued Power Density, Wind Speed, Biodiversity and Roughness.
         Five of Brazil's 26 states have meterological conditions that are suitable for wind power generation.
         You can focus on a paricular state, or get a country wide overview.""")


# columns
# col1, col2, col3, col4 = st.columns(4)
# slider1, slider2, slider3, slider4 = st.columns(4)

col1, col2, col3 = st.columns(3)
slider1, slider2, slider3 = st.columns(3)


# static masks
protected_areas_mask = ((data['Protected Areas'] + data['Airports'] + data['Offshore']) > 0).astype(float)

# thresholds
power_density_threshold = slider1.slider("Power dentiy percentile*", 50, 99, 50)
grid_distance_threshold = 26 - slider2.slider("Max km to 400V+ power line", 5, 25, 25)
wind_speed_threshold = slider3.slider("Minimum wind speed (m/s)", 5, 10, 5)
# roughness_threshold = slider4.slider("Rougness (percentile)", 0, 100, 50)

# masks
power_density_mask = make_mask(data['Power Density'], power_density_threshold)
grid_distance_mask = make_mask(data['Power Lines'], grid_distance_threshold)
wind_speed_mask = make_mask(data['Wind Speed'], wind_speed_threshold)
# roughness_mask = make_mask(data['Roughness'], roughness_threshold)

# images
col1.image(power_density_mask, use_column_width=True)
col2.image(grid_distance_mask, use_column_width=True)
col3.image(wind_speed_mask, use_column_width=True)
# col4.image(roughness_mask, use_column_width=True)




# final mask
final_mask = (power_density_mask *
              ((grid_distance_mask + data['Offshore']) > 0) *
              wind_speed_mask * protected_areas_mask)
                # data['Protected Areas'])



col1, col2 = st.columns(2)
col1.header(f"{mask_ratio(final_mask) * 100:.2f}% of Brazil is suitable for wind power generation")
col1.write(f"""Using your thresholds, {mask_ratio(final_mask) * 100:.2f}% of Brazil is suitable for wind power generation.""")
col1.write(f"""In addition to the thesholds you've set, the map also excludes areas that are not suitable due biodiversity considerations, airports, and other protected areas.""")
col1.write(f"""The map to the right shows the areas that are suitable for wind power generation, using your thresholds.""")
col1.write("""You can download the mask by clicking the bytton below, and use it to further explore the data in your own tools.""")
col1.download_button('Download mask', final_mask.tostring(), 'mask.npy', 'application/octet-stream')
col2.image(final_mask, caption='Final mask', use_column_width=True)



# about the project


# images
col1, col2, col3 = col1.columns(3)
col1.image(data['Protected Areas'], caption='Protected Areas', use_column_width=True)
col2.image(data['Airports'], caption='Airports', use_column_width=True)
col3.image(data['Slope'], caption='Slope', use_column_width=True)



# footer
# st.write('*Power density is an aggregate measure by the Global Winds Atlas, representing how much potential wind power is in an area.')