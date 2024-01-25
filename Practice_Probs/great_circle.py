import numpy as np

def get_alpha(lon_2, lon_1):
    return (lon_2 - lon_1)

def lat_to_colat(lat):
    return (90. - lat) 

def great_circle(lat_1, lon_1, lat_2, lon_2):
    # Calculate the great circle distance between two points on a globe

    if lon_1 < -180 or lon_1 > 180:
        raise Exception('Longitude 1 is outside of the range -180:180')
    if lon_2 < -180 or lon_2 > 180:
        raise Exception('Longitude 2 is outside of the range -180:180')

    # First, convert the latitudes to colatitudes
    colat_1 = lat_to_colat(lat_1)
    colat_2 = lat_to_colat(lat_2)
    # and alpha is the difference between the two longitudes
    alpha = get_alpha(lon_2, lon_1)
    # Convert degrees to radians
    colat_1, colat_2, alpha = np.radians(colat_1), np.radians(colat_2), np.radians(alpha)
    # Spherical trig:
    cosa = np.cos(colat_1) * np.cos(colat_2) + np.sin(colat_1) * np.sin(colat_2) * np.cos(alpha)

    a = np.arccos(cosa)

    return np.degrees(a)