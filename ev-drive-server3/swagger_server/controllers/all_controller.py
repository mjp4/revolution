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

    car_status = { "Watt ": "18160",
                   "location_lat": "52.375666666667",
                   "location_long": "-1.7978888888889"
                   }

    start_point = dict(lat=car_status['location_lat'], long=car_status['location_long'])
    end_point = filter_charger.get_coordinates(to)

    charger_raw_list = filter_charger.get_charger_list()
    all_chargers = filter_charger.filter_chargers_on_route_lat_long(start_point, end_point, charger_raw_list)


    for i in all_chargers:
        print(str(i))
        ast.literal_eval(str(i))
        charge_lat = i["lat"]
        charge_long = i["long"]
        i['dist_miles'] = float((dist_controller.get_dist_to_charger(start_point['lat'], start_point['long'], charge_lat, charge_long)))
        i['dist_km'] = i['dist_miles'] * 1.6

    all_chargers = sorted(all_chargers, key=itemgetter('dist_miles'))

    # Remove duplicates
    parsed_chargers = []
    ii = 1
    for i in all_chargers:
        ast.literal_eval(str(i))
        if parsed_chargers:
            if i["lat"] != parsed_chargers[:-1]["lat"] or i["long"] != parsed_chargers[:-1]["long"]:
                parsed_chargers.append(i)
        else:
            parsed_chargers.append(i)

    # all_chargers[:3]

    return {"chargers": parsed_chargers,
            "car": car_status}
