import connexion
import six

from swagger_server.models.on_route import OnRoute  # noqa: E501
from swagger_server import util


def chargers_on_route(_from, to):  # noqa: E501
    """Get a list of the chargers on route

     # noqa: E501

    :param _from: Start or end point
    :type _from: str
    :param to: Start or end point
    :type to: str

    :rtype: OnRoute
    """
    return 'do some magic!'
