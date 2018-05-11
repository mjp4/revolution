# import connexion
import six
import requests
import json
import wget


def duration_to_time(duration_str):
    duration_list = duration_str.split(" ")
    if len(duration_list) > 2:
        time = int(duration_list[0]) * 60 + int(duration_list[2])
    elif len(duration_list) == 2:
        time = int(duration_list[0])

    return time

def extra_time_to_charger(lat_here, long_here, lat_charger, long_chager, lat_dest, lon_dest):

    api_key = "AIzaSyCsYddGN_7QHkR-JnCS4PA-giJV79ZqW7c"


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
