# main.py
#   aeolus main script
# by: Noah Syrkis

# Imports
import tempfile
import rasterio
import geopandas as gpd
import elevation
from src.utils import get_args
from src.topography import calculate_slope, calculate_roughness


# Constants
DATA_DIR = 'data'


def main():

    args = get_args()

    brazil = gpd.read_file(f'{DATA_DIR}/brazil.geojson')
    offshore = gpd.read_file(f'{DATA_DIR}/offshore.geojson')
    brazil_and_offshore = brazil.union(offshore)

    if args.topography:

        with tempfile.TemporaryDirectory() as tmpdir:
            elevation.clip(bounds=brazil_and_offshore.total_bounds, output=f'{DATA_DIR}/topology/brazil_dem.tif', product='SRTM3', cache_dir=tmpdir, max_download_tiles=100)

        with rasterio.open(f'{DATA_DIR}/topography/brazil_dem.tif') as src:
            topography = src.read(1)

        with rasterio.open('data/topography/slope.tif', 'w', driver='GTiff', height=slope.shape[0], width=slope.shape[1], count=1, dtype=slope.dtype, crs=src.crs, transform=src.transform) as dst:
            dst.write(calculate_slope(topography), 1)

        with rasterio.open('data/topography/roughness.tif', 'w', driver='GTiff', height=roughness.shape[0], width=roughness.shape[1], count=1, dtype=roughness.dtype, crs=src.crs, transform=src.transform) as dst:
            dst.write(calculate_roughness(topography), 1)

    if args.vector:

        polygon = max(brazil.geometry[0].geoms, key=lambda x: x.area)
        offshore = gpd.GeoDataFrame({'geometry': [polygon]}, crs=brazil.crs) \
            .to_crs('EPSG:5880') \
            .buffer(100 * 1000) \
            .to_crs(brazil.crs) \
            .difference(brazil)
        brazil_and_offshore = offshore.union(brazil)

        offshore.to_file('data/offshore.geojson', driver='GeoJSON')
        brazil_and_offshore.to_file('data/offshore_brazil.geojson', driver='GeoJSON')