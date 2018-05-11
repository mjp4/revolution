import connexion
import six
import requests
import json
import wget

def get_time_to_charger(lat_here, long_here, lat_charger, long_chager, lat_dest, lon_dest):

    api_key = "AIzaSyCsYddGN_7QHkR-JnCS4PA-giJV79ZqW7c"


    url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins={},{}|{},{}&destinations={},{}|{},{}&key={}" \
        .format(lat_here, long_here, lat_charger, long_chager, lat_charger, long_chager, lat_dest, lon_dest, api_key)
    print(url)
    fs = wget.download(url=url, out='dist.json')
    with open(fs, 'r') as f:
        content = f.read()

    data = json.loads(content)
    
    original_time = data['rows'][0]['elements'][0]['duration']['text']

    print(original_time)


    #miles = data['rows'][0]['elements'][0]['distance']['text']

    #return miles[:-3]

get_time_to_charger(55.838968, -4.263472, 55.504997, -4.368097,55.631621, -3.872165)
