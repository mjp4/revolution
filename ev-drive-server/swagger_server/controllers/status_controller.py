import connexion
import six

from swagger_server.models.charge_perc import ChargePerc  # noqa: E501
from swagger_server import util


def get_charge_perc(username, password):  # noqa: E501
    """Get the charge percentage

     # noqa: E501

    :param username: Username for logging in 
    :type username: str
    :param password: Users password
    :type password: str

    :rtype: ChargePerc
    """
    return 'do some magic!'
