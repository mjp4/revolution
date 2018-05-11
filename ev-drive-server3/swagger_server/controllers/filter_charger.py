import six
from swagger_server.controllers import status_controller

import matplotlib.pyplot as plt
from matplotlib import interactive
import requests
import json


def get_route(start, end):
    """
    This function gets the route information from a mysterious website.
    
    Inputs the start and end coordinates.
    Returns a list of Point instances represents the route found by the website.  
    """

    # Get the route data from website.
    base_url = "http://www.yournavigation.org/api/1.0/gosmore.php?format=kml&flat={0}&flon={1}&tlat={2}&tlon={3}&v=motorcar&fast=1&layer=mapnik"
    get_url = base_url.format(start["lat"], start["long"], end["lat"], end["long"])
    website_text_result = requests.get(get_url).text
    
    # Filter the output to get the coordinates.
    website_text_result = website_text_result.split("<coordinates> ")[1]
    website_text_result = website_text_result.split("</coordinates>")[0]
    coordinate_list = website_text_result.split("\n")[:-1]
    
    # Form a list of Point instances.
    new_coordinate_list = []
    for coordinate in coordinate_list:
        point = {"lat": float(coordinate.split(",")[0]), "long": float(coordinate.split(",")[1])}
        new_coordinate_list.append(point)
    
    return new_coordinate_list


def get_coordinates(postcode):
    """
    This function returns the lat and long for a given postcode.
    
    Input the postcode as a string. You can have space between. 
    Returns a Point instance with lat and long.
    """

    # Remove the space between postcode.
    postcode = postcode.replace(" ", "")
    base_url = "http://api.postcodes.io/postcodes/{0}"
    get_url = base_url.format(postcode)
    website_text_result = requests.get(get_url).text
    website_result = json.loads(website_text_result)

    if website_result['status'] != 200:
        return []
    lat = website_result['result']['latitude']
    long = website_result['result']['longitude']
   
    return {"lat": lat, "long": long}



def get_charger_list():
    """
    Funciton that returns the charger list stored in a json file

    Returns a list of dictionaries with the charger content on them
    """

    charger_file = open('charger-list/50over.json','r')
    content = charger_file.read()
    charger_list = json.loads(content)

    return charger_list


def filter_charger(input_route, charger_list):
    """
    input_route is a list of points, every one of them contains two numbers, long and lat.
    charger_list is a list of random points on the map, also contain long and lat.
    
    The aim is to get a list of chargers along the path within 0.03 miles.
    """

    long_list = []
    lat_list = []
    
    # Loop through the route, group all long and lat into two lists. 
    for route_point in input_route:
        long_list.append(route_point["long"])
        lat_list.append(route_point["lat"])
    
    long_min = min(long_list) - 0.03
    long_max = max(long_list) + 0.03
    lat_min = min(lat_list) - 0.03
    lat_max = max(lat_list) + 0.03

    # Filter the charger.
    # The route forms a block within the long and lat range, filter out the charger outside of it.
    charger_in_range = []
    for charger in charger_list:
        if float(charger["long"]) <= long_max and float(charger["long"]) >= long_min:
            if float(charger["lat"]) <= lat_max and float(charger["lat"]) >= lat_min:
                charger_in_range.append(charger)

    # Do calculations to filter more.
    # Keep chargers within 2 miles distance from the route, which is 0.03 degree either long or lat. 
    final_charger = []
    for charger in charger_in_range:
        for route_point in input_route:
            if abs(route_point["long"] - charger["long"]) < 0.03 and abs(route_point["lat"] - charger["lat"]) < 0.03:
                final_charger.append(charger)
                break

    return final_charger


def plot_maps(route, charger_raw_list, charger_filtered_list):
    route_long = []
    route_lat = []
    for i in route:
        route_long.append(i["long"])
        route_lat.append(i["lat"])

    charger_raw_long = []
    charger_raw_lat = []
    for i in charger_raw_list:
        charger_raw_long.append(i["long"])
        charger_raw_lat.append(i["lat"])

    # Build the figure with route and original charger.
    plt.figure(1)
    plt.xlabel("lat")
    plt.ylabel("long")
    plt.title("The Map")
    plt.scatter(charger_raw_long, charger_raw_lat, label="Charger", color="red", marker="*", s=5)
    plt.plot(route_long, route_lat, label="Car Route", color="blue")
    plt.legend()
    interactive(True)
    plt.show()

    charger_filtered_long = []
    charger_filtered_lat = []
    for i in charger_filtered_list:
        charger_filtered_long.append(i["long"])
        charger_filtered_lat.append(i["lat"])

    # Build the figure with route and filtered charger.
    plt.figure(2)
    plt.xlabel("long")
    plt.ylabel("lat")
    plt.title("Filtered Map")
    plt.scatter(charger_filtered_long, charger_filtered_lat, label="Charger", color="red", marker="*", s=5)
    plt.plot(route_long, route_lat, label="Car Route", color="blue")
    plt.legend()
    interactive(False)
    plt.show()


def get_chargers_on_route(start_postcode, end_postcode, plot=False):
    """
    Define the start_point and the end_point, randomly generate charging points.
    Plot the raw map and filter map.
    """
    start_point = get_coordinates(start_postcode)
    end_point = get_coordinates(end_postcode)
    route = get_route(start_point, end_point)
    charger_raw_list = get_charger_list()
    charger_filtered_list = filter_charger(route, charger_raw_list)

    if plot:
        plot_maps(route, charger_raw_list, charger_filtered_list)

    return charger_filtered_list


if __name__ == "__main__":
    get_chargers_on_route("EN2 6SB", "SW7 2AZ", plot=True)
