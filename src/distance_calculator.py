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

def shortest_distance_from_shop(geocoded_array):

    shop_geocode = [42.341764, -82.002213] # Hardcode the shop geo location
    distances_from_shop =[] # array that will store distances from each property 

    for i in range(0, len(geocoded_array)):
        distance = gmaps.distance_matrix(tuple(shop_geocode), tuple(geocoded_array[i]), mode="driving") # calculate distance 

        if distance['rows'][0]['elements'][0]['status'] == 'OK':
            distances_from_shop.append(distance['rows'][0]['elements'][0]['distance']['value'])
        else:
            print("Distance from shop could not be found")
            distances_from_shop.append(-1)
        
    smallest_distance = distances_from_shop.index(min(distances_from_shop)) # Store the index of the property with smallest distance from shop

    return smallest_distance # Return the index of property with shortest distance

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
                meters_distance_at_i.append(-1) # Append negative distance to show faulty calculation

        distance_matrix.append(meters_distance_at_i) # Load the distance/times comparisons from location a to all other locations into distance matrix

    return distance_matrix # Return matrix containing time/distances between all properties

array = [[34.0770948, -118.39719],[42.4264444, -82.1957029],[42.4042706, -82.1766639],[42.411223, -73.525481],[37.595558, -77.583413]]

matrix = distance_calculator(array)
shortest = shortest_distance_from_shop(array)
print(matrix)
print(shortest)