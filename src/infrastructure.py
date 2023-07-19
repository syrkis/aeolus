# infrastructure.py
#
# by: Noah Syrkis


# imports
import osmnx as ox


# functions
def get_energy_grid():
    """
    Returns the energy grid of Brazil
    """
    return ox.graph_from_place('Brazil', network_type='drive')