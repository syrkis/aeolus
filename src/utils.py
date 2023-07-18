# utils.py
#     utils and constants
# by: Noah Syrkis

# Imports
import argparse


# Constants
DATA_DIR = 'data'
KILOMETERS_OFFSHORE = 100



# Functions
def get_args():
    parser = argparse.ArgumentParser(description='aeolus main script')
    parser.add_argument('--topography', action='store_true', help='calculate topography')
    parser.add_argument('--vector', action='store_true', help='calculate vector')
    return parser.parse_args()