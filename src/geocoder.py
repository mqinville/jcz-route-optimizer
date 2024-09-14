import googlemaps

# Imports to load api key
from dotenv import load_dotenv
import os

load_dotenv() # Load the .env fie containing api key

api_key = os.getenv("GOOGLE_API_KEY")

if api_key:
    gmaps = googlemaps.Client(key=api_key)
    print("Google Maps Client Initialized")
else:
    print("API key not found")
    exit()

def geocoder(property_address):
    
    address_geocode= gmaps.geocode(property_address) # Call google api to geocode adress, returns a dictionary of locations 

    if address_geocode:
        latitude = address_geocode[0]['geometry']['location']['lat'] # Extract the latitude from the first result returned by geocoder
        longitude = address_geocode[0]['geometry']['location']['lng'] # Extract the longitude from the first result returned by geocoder

        geocoded_array = [latitude, longitude]
        return geocoded_array # Return a tuple containing the latitude and longitude
    
    else: # If no geocode equivalent found return None
        return None