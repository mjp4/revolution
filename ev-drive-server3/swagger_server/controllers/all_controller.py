import connexion
import six
from swagger_server.controllers import status_controller

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

    a = status_controller.get_charge_perc(username, password)
    return a