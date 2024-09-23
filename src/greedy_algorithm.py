import math

def greedy(distance_matrix, start_index):
    
    num_properties = len(distance_matrix)
    route = [] # Array that will hold the route
    visited_properties = [False] * num_properties # Boolean array set to false, tracks locations visited
    total_distance = 0 # Integer variable to track total distance of the route\
    current_property = start_index # Set the current property index to our starting index
    visited_count = 0 # COunter varuabke to track how many properties have been visited

    # Set our visit to current property to true and add this property to the route
    visited_properties[start_index] = True 
    route.append(start_index) 

    # While loop that will loop until all properties are visited
    while (len(route) < num_properties):
        minimum_dist = math.inf # Set the minimum distance of current iteration to infinity
        nearest_property = None # Set the current nearest property to None 
        
        
        for i in range(num_properties):
            #Check if the current property is already in our route/ current property
            if not visited_properties[i]:  
                    # If the current distance is less then the minimum distance set new min distance and new nearest property
                if distance_matrix[current_property][i] < minimum_dist:
                    minimum_dist = distance_matrix[current_property][i]
                    nearest_property = i 

        visited_properties[nearest_property] = True # Mark the nearest property as visited
        route.append(nearest_property) # Add the new nearest property to our route
        total_distance += minimum_dist # Add the minimum distance to total dstabce sum
        current_property = nearest_property # Set current property to the property just added to route
        visited_count += 1 # Increment the amount of properties visited

    return route, total_distance # Return the optimised route and total distance of this route


dist_matrix = [[0, 3781577, 3778237, 4593348, 4219316], [3781327, 0, 3832, 830264, 1092809], [3777937, 3832, 0, 827043, 1089418], [4593368, 829487, 827398, 0, 762082], [4222891, 1093318, 1089978, 780420, 0]]
start = 2

route, dist = greedy(dist_matrix, start)
print(route, dist)

