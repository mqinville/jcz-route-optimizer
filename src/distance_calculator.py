import googlemaps
from datetime import time

# Imports to load api key
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if api_key:
    gmaps = googlemaps.Client(key=api_key) # Initialize googlemaps client
    print("Google Maps Client Initialized")
else:
    print("API key not found")
    exit()

def distance_calculator(geocoded_array):
    distance_matrix = [] # Matrix that will contain distances between all properties -  This is a hollow matrix (Diagonal is all zeroes)

    for i in range(0, len(geocoded_array)):
        meters_distance_at_i = [] # Array that will contain distances between one property and all the other - reset for every iteration
        for j in range (0, len(geocoded_array)):
            time_distance_at_i = gmaps.distance_matrix(tuple(geocoded_array[i]), tuple(geocoded_array[j]), mode="driving")# calculate the distance/time between location i and all other locations
            
            # If the distance was properly calculated then proceed
            if time_distance_at_i['rows'][0]['elements'][0]['status'] == 'OK':
                meters_distance_at_i.append(time_distance_at_i['rows'][0]['elements'][0]['distance']['value']) # Extract the distance in meters 
            else:
                print('Distance could not be calculated')

        distance_matrix.append(meters_distance_at_i) # Load the distance/times comparisons from location a to all other locations into distance matrix

    return distance_matrix # Return matrix containing time/distances between all properties

array = [[34.0770948, -118.39719],[42.4264444, -82.1957029],[42.4042706, -82.1766639],[42.411223, -73.525481],[37.595558, -77.583413]]

matrix = distance_calculator(array)
print(matrix)