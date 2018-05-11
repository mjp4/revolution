import connexion
import six
from swagger_server.controllers import status_controller
import json
import ast
from operator import itemgetter


from swagger_server.models.all_info import AllInfo  # noqa: E501
from swagger_server.controllers import dist_controller
from swagger_server.controllers import filter_charger
from swagger_server import util


def all_info(username, password, to):  # noqa: E501
    """Get all the info
     # noqa: E501
    :param username: Username for logging in
    :type username: str
    :param password: Users password
    :type password: str
    :param to: Start or end point
    :type to: str
    :rtype: AllInfo
    """
    # car_status = status_controller.get_charge_perc(username, password)

    username = "mark@perryman.org.uk"

    car_status = { "WattHour": "18160",
                   "location_lat": "52.375666666667",
                   "location_long": "-1.7978888888889"
                   }

    start_point = dict(lat=car_status['location_lat'], long=car_status['location_long'])
    end_point = filter_charger.get_coordinates(to)

    charger_raw_list = filter_charger.get_charger_list()

    route_chargers = filter_charger.filter_chargers_on_route_lat_long(start_point, end_point, charger_raw_list)

    chargers_with_dist = chargers_with_distance(start_point, route_chargers)

    sorted_chargers = sorted(chargers_with_dist, key=itemgetter('dist_miles'))

    # Remove duplicates
    parsed_chargers = []
    print(sorted_chargers)
    for i in sorted_chargers:
        if parsed_chargers:
            if i["lat"] != parsed_chargers[-1]["lat"] or i["long"] != parsed_chargers[-1]["long"]:
                parsed_chargers.append(i)
        else:
            parsed_chargers.append(i)

    limited_chargers = parsed_chargers[:3]

    return {"chargers": limited_chargers,
            "car": car_status}

def chargers_with_distance(start_point, chargers):
    for charger in chargers:
        ast.literal_eval(str(charger))
        charge_lat = charger["lat"]
        charge_long = charger["long"]
        charger['dist_miles'] = float((dist_controller.get_dist_to_charger(start_point['lat'], start_point['long'], charge_lat, charge_long)))
        charger['dist_km'] = charger['dist_miles'] * 1.6
    return chargers

