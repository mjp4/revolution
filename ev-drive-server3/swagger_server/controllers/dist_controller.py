import connexion
import six
from math import cos, asin, sqrt
import requests
import json
import wget

from swagger_server.models.dist_to_charger import DistToCharger  # noqa: E501
from swagger_server import util

api_key = "AIzaSyDP0Rn3x3AP1nbSGZgdQ2HCyQXnme1UtJ8"

def get_dist_to_charger(lat_here, long_here, lat_there, long_there):  # noqa: E501
    """Get the distance to charger

     # noqa: E501

    :param lat_here: The latitude or longitude
    :type lat_here: str
    :param long_here: The latitude or longitude
    :type long_here: str
    :param lat_there: The latitude or longitude
    :type lat_there: str
    :param long_there: The latitude or longitude
    :type long_there: str

    :rtype: DistToCharger
    """

    url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins={},{}&destinations={},{}&key={}" \
        .format(lat_here, long_here, lat_there, long_there, api_key)

    website_text_result = requests.get(url).text
    data = json.loads(website_text_result)

    miles = data['rows'][0]['elements'][0]['distance']['text']

    return miles[:-3]

    # lat_here = float(lat_here)
    # long_here = float(long_here)
    # lat_there = float(lat_there)
    # long_there = float(long_there)

    # p = 0.017453292519943295     #Pi/180
    # a = 0.5 - cos((lat_there - lat_here) * p) \
    #     / 2 + cos(lat_here * p) \
    #     * cos(lat_there * p) \
    #     * (1 - cos((long_there - long_here) * p)) / 2
    # return 12742 * asin(sqrt(a))

def duration_to_time(duration_str):
    duration_list = duration_str.split(" ")
    if len(duration_list) > 2:
        time = int(duration_list[0]) * 60 + int(duration_list[2])
    elif len(duration_list) == 2:
        time = int(duration_list[0])

    return time

def extra_time_to_charger(lat_here, long_here, lat_charger, long_chager, lat_dest, lon_dest):

    url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins={},{}|{},{}&destinations={},{}|{},{}&key={}" \
        .format(lat_here, long_here, lat_charger, long_chager, lat_charger, long_chager, lat_dest, lon_dest, api_key)
    
    print(url)
    website_text_result = requests.get(url).text
    data = json.loads(website_text_result)
    
    origin_dest_time = data['rows'][0]['elements'][0]['duration']['text']
    origin_charger_time = data['rows'][0]['elements'][1]['duration']['text']
    charger_dest_time = data['rows'][1]['elements'][1]['duration']['text']
    
    extra_time = duration_to_time(origin_charger_time) + duration_to_time(charger_dest_time) - duration_to_time(origin_dest_time)
    
    return extra_time
