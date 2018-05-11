import requests
import json
from random_points import Point


def get_route(start, end):
    """
    This function gets the route information from a mysterious website.
    
    Inputs the start and end Point instance.
    Returns a list of Point instances represents the route found by the website.  
    """

    # Get the route data from website.
    base_url = "http://www.yournavigation.org/api/1.0/gosmore.php?format=kml&flat={0}&flon={1}&tlat={2}&tlon={3}&v=motorcar&fast=1&layer=mapnik"
    get_url = base_url.format(start.latitude, start.longitude, end.latitude, end.longitude)
    website_text_result = requests.get(get_url).text
    
    # Filter the output to get the coordinates.
    website_text_result = website_text_result.split("<coordinates> ")[1]
    website_text_result = website_text_result.split("</coordinates>")[0]
    coordinate_list = website_text_result.split("\n")[:-1]
    
    # Form a list of Point instances.
    new_coordinate_list = []
    for coordinate in coordinate_list:
        point = Point(float(coordinate.split(",")[0]), float(coordinate.split(",")[1]))
        new_coordinate_list.append(point)
    
    return new_coordinate_list


def get_coordinates(postcode):
    """
    This function returns the latitude and longitude for a given postcode.
    
    Input the postcode as a string. You can have space between. 
    Returns a Point instance with latitude and longitude.
    """

    # Remove the space between postcode.
    postcode = postcode.replace(" ", "")
    base_url = "http://api.postcodes.io/postcodes/{0}"
    get_url = base_url.format(postcode)
    website_text_result = requests.get(get_url).text
    website_result = json.loads(website_text_result)

    if website_result['status'] != 200:
        return []
    latitude = website_result['result']['latitude']
    longitude = website_result['result']['longitude']
   
    return Point(latitude,longitude)


if __name__ == "__main__":
    coordinate = get_coordinates("EN2 6SB")
    print(coordinate)