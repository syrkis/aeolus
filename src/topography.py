# topography.py
#  topography functions
# by: Noah Syrkis


# Imports
import numpy as np
from scipy.ndimage.filters import uniform_filter


# Functions
def calculate_slope(topography):
    x, y = np.gradient(topography)
    slope = np.pi/2. - np.arctan(np.sqrt(x*x + y*y))
    return slope

def calculate_roughness(topography):
    window_size = 3
    square = topography**2
    mean_square = uniform_filter(square, window_size)
    mean_ = uniform_filter(topography, window_size)
    return np.sqrt(mean_square - mean_**2)