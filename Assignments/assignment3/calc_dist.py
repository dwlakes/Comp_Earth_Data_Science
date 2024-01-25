import numpy as np
import math

def great_circle(point1,point2):


    r = 6371 # Earth's radius in km
    lat1 = degrees_to_radians(point1[0])
    lon1 = degrees_to_radians(point1[1])


    lat2 = degrees_to_radians(point2[0])
    lon2 = degrees_to_radians(point2[1])

    step1 = np.cos(lat1)*np.cos(lat2)*np.cos((lon1-lon2))
    step2 = np.sin(lat1)*np.sin(lat2)
    step3 = (step2 + step1)
    step4 = np.arccos(step3)
    
    print(step4*r)
    
    d = r * np.arccos(np.cos(lat1)*np.cos(lat2)*np.cos(lon1-lon2)+np.sin(lat1)*np.sin(lat2))

    print(d)
    return d


def degrees_to_radians(degrees):  
  
    
    radians = degrees * np.pi / 180.0
  
    return radians


great_circle((-21.9201, -67.2530), (19.0323, -66.6045))