import connexion
import six
from swagger_server.controllers import status_controller
import json

from swagger_server.models.all_info import AllInfo  # noqa: E501
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
    car_status = { "Watt Hours": "18160",
                   "location_lat": "52.375666666667",
                   "location_long": "-1.7978888888889"
                   }

    start_point = dict(lat=car_status['location_lat'], long=car_status['location_long'])
    end_point = filter_charger.get_coordinates(to)

    charger_raw_list = filter_charger.get_charger_list()
    all_chargers = filter_charger.filter_chargers_on_route_lat_long(start_point, end_point, charger_raw_list)

    return {"chargers": all_chargers,
            "car": car_status}
