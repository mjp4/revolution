import connexion
import six
from math import cos, asin, sqrt

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


    lat_here = float(lat_here)
    long_here = float(long_here)
    lat_there = float(lat_there)
    long_there = float(long_there)

    p = 0.017453292519943295     #Pi/180
    a = 0.5 - cos((lat_there - lat_here) * p) \
        / 2 + cos(lat_here * p) \
        * cos(lat_there * p) \
        * (1 - cos((long_there - long_here) * p)) / 2
    return 12742 * asin(sqrt(a))



    # return 'do some magic!'

