import connexion
import six

from swagger_server.models.on_route import OnRoute  # noqa: E501
from swagger_server import util
from random import sample

def chargers_on_route(_from, to):  # noqa: E501
    """Get a list of the chargers on route

     # noqa: E501

    :param _from: Start or end point
    :type _from: str
    :param to: Start or end point
    :type to: str

    :rtype: OnRoute
    """
    return [
  {
    "lat": "52.618731",
    "long": "-1.205812",
    "network": "Ecotricity (Electric Highway)",
    "dist_miles": "50",
    "dist_km": "80",
    "extra_time": "5",
    "other": "extra_string"
  },
  {
    "lat": "53.713912",
    "long": "-1.743583",
    "network": "Ecotricity (Electric Highway)",
    "dist_miles": "25",
    "dist_km": "40",
    "extra_time": "5",
    "other": "extra_string"
  }
]


def getCoordinates(name):
  places = [[51.652135, -0.084229],[51.513806, -0.100695],[55.947426, -3.196410]]
  return sample(places,1)[0]

