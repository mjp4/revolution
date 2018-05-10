import connexion
import six

from swagger_server.models.dist_to_charger import DistToCharger  # noqa: E501
from swagger_server import util


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
    return 'do some magic!'
