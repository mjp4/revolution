import connexion
import six
from swagger_server.controllers import status_controller
import json

from swagger_server.models.all_info import AllInfo  # noqa: E501
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
    car_status = status_controller.get_charge_perc(username, password)

    with open("swagger_server/controllers/charger-list/50over.json", "r") as charger_file:
        all_chargers = json.load(charger_file)

    return {"chargers": all_chargers,
            "car": car_status}
