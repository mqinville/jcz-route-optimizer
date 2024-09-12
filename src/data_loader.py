import csv

# Function for loading grass properties into a multidimensional array
def load_properties_csv(file_path) :

    property_array = []
   

    with open(file_path, 'r') as file: # Open the designated property csv file in read mode - Auto closes at end of block
        properties_csv = csv.reader(file) # Intitalize DictReader object, each row from csv is turned into a dictionary       
    
        for rows in properties_csv:
            property_array.append(rows)
    
    property_array.pop(0) # Remove the "column/title" row from the array

    return property_array # Return list containing csv info

