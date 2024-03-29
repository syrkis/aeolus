import streamlit as st
import numpy as np
import os
from esda.moran import Moran
from libpysal.weights import lat2W
# import rasterio

# set wide layout
st.set_page_config(layout="wide")

def pad_matrix_to_square(M):
    """Pad a matrix with zeros to make it square."""
    if M.shape[0] == M.shape[1]:
        return M
    elif M.shape[0] > M.shape[1]:
        pad_width = ((0, 0), (0, M.shape[0] - M.shape[1]))
    else:
        pad_width = ((0, M.shape[1] - M.shape[0]), (0, 0))
    return np.pad(M, pad_width, mode='constant', constant_values=0)

@st.cache_data
def load_data(state=None):
    fps = ['power_density', 'powerlines', 'population_mask', 'wind_speed', 'protected_areas_mask', 'airport_mask', 'slope_mask', 'roughness', 'brazil_mask', 'offshore_mask']
    if state is not None:
        fps = [fp + '_' + state for fp in fps]
    names = ['Power Density', 'Power Lines', 'Population', 'Wind Speed', 'Protected Areas', 'Airports', 'Slope', 'Roughness', 'Brazil', 'Offshore']
    if state is not None:
        data = {name: pad_matrix_to_square(np.load(os.path.join("masks", fp + '.npy'))).astype(float) for fp, name in zip(fps, names)}
    else:
        data = {name: pad_matrix_to_square(np.load(os.path.join("masks", fp + '.npy'))).astype(float)[::3, ::3] for fp, name in zip(fps, names)}
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

def calculate_percentile(data, percentile):
    return np.percentile(data, percentile)

def moran_i(mask, _):
    # compute standardized moran's I (use vectorized operations)
    # exclude values outside of the brazil offshore mask
    moran = Moran(mask.flatten(), w)
    return moran.I * moran_brazil_ratio

area_sizes = {'Brazil': 8514215, 'Rio Grande do Norte': 52796, 'Bahia': 565733, 'Rio Grande do Sul': 281707, 'Piaui': 251529, 'Nordeste': 1558196}

all_data = {state: load_data(state) for state in  ['Rio Grande do Norte', 'Bahia', 'Rio Grande do Sul', 'Piaui', 'Nordeste']}
all_data['Brazil'] = load_data()

w = lat2W(*all_data['Brazil']['Brazil'].shape)
moran_brazil_ratio = all_data['Brazil']['Brazil'].sum() / all_data['Brazil']['Brazil'].size

# Header
st.title("Brazilian wind farm location scout")
st.write(f"""Tweak the modality thresholds below to find potential locations for wind farm projects.
         The explorer will show you the best locations based on how you've valued Power Density, Wind Speed, Biodiversity and Terrain Roughness.
         Five of Brazil's 26 states have meterological conditions that are suitable for wind power generation.
         You can focus on a paricular state, or get a country wide overview.""")


# columns
# col1, col2, col3, col4 = st.columns(4)
# slider1, slider2, slider3, slider4 = st.columns(4)
selected_region = st.selectbox('Selected region:', ['Brazil', 'Rio Grande do Norte', 'Bahia', 'Rio Grande do Sul', 'Piaui', 'Nordeste'])
data = all_data[selected_region]

moran_brazil_ratio = data['Brazil'].sum() / data['Brazil'].size
col1, col2, col3, col4 = st.columns(4)

slider1, slider2, slider3, slider4 = st.columns(4)


# static masks
protected_areas_mask = ((data['Protected Areas'] + data['Airports'] + data['Offshore']) > 0).astype(float)

# thresholds
power_density_threshold = slider1.slider("Power dentiy* (percentile)", 50, 99, 50)
grid_distance_threshold = 26 - slider2.slider("Max distance (km) to 400V+ power line", 5, 25, 25)
wind_speed_threshold = slider3.slider("Minimum wind speed (m/s)", 5, 10, 5)
roughness_threshold = int(slider4.slider("Terrain Roughness (percentile)", 1, 99, 0) / 2) + 49

# masks
power_density_mask = make_mask(data['Power Density'], power_density_threshold)
grid_distance_mask = make_mask(data['Power Lines'], grid_distance_threshold)
wind_speed_mask = make_mask(data['Wind Speed'], wind_speed_threshold)
roughness_mask = make_mask(data['Roughness'], calculate_percentile(data['Roughness'], roughness_threshold))

# images
col1.image(power_density_mask, use_column_width=True)
col2.image(grid_distance_mask, use_column_width=True)
col3.image(wind_speed_mask, use_column_width=True)
col4.image(roughness_mask, use_column_width=True)



# final mask
final_mask = (power_density_mask *
              ((grid_distance_mask + data['Offshore']) > 0) *
              wind_speed_mask * protected_areas_mask *
              (roughness_mask + data['Offshore']) > 0).astype(float)
                # data['Protected Areas'])



col1, col2 = st.columns(2)
col1.header(f"{mask_ratio(final_mask) * 100:.2f}% of {selected_region} is suitable for wind power generation. Thats {area_sizes[selected_region] * mask_ratio(final_mask):,.0f} km²!")
col1.write(f"""Using your thresholds, {mask_ratio(final_mask) * 100:.2f}% of {selected_region} is suitable for wind power generation.""")
col1.write(f"""The map to the right shows the areas that are suitable for wind power generation, using your thresholds.""")
col1.write("Moran's I is a measure of spatial autocorrelation that quantifies the degree to which the potential wind farm areas are clustered together. The measure ranges from -1 (perfect dispersion) to 1 (perfect clustering). Click below to compute—this may take a few seconds. NOTE: Currently this only works when Brazil is selected.")
if selected_region == 'Brazil':
    if col1.button('Compute Moran\'s I'):
        col1.header(f"""Moran's I is {moran_i(final_mask, data):.2f}.""")
col1.write("""You can download the mask by clicking the button below, and use it to further explore the data in your own tools. Current mask is a numpy array, with 1 representing suitable areas, and 0 representing unsuitable areas. More formats are comming soon.""")
col1.download_button('Download mask', final_mask.tobytes(), 'mask.npy', 'application/octet-stream')
col2.image(final_mask, caption='Final mask', use_column_width=True)



# about the project


# images
st.header('Additional exclusion criteria')
st.write(f"""In addition to the thresholds you've set, the map also excludes areas unsuitable due to biodiversity considerations and other protected areas, airports, and slopes above 20 % inclination.""")
col1, col2, col3 = st.columns(3)
col1.image(data['Protected Areas'], caption='Protected Areas', use_column_width=True)
col2.image(data['Airports'], caption='Airports', use_column_width=True)
col3.image(data['Slope'], caption='Slope', use_column_width=True)

# footer
st.write('*Power density is an aggregate measure by the Global Winds Atlas, representing how much potential wind power is in an area.')