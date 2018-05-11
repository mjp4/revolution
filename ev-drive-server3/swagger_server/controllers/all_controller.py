import connexion
import six
import logging
from swagger_server.models.all_info import AllInfo  # noqa: E501
from swagger_server import util
import status_controller
import dist_controller


logging.debug("login = %s , password = %s" % ( username , password)  )

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

    ###############CONVERT 'to' to long and lat ####################

    # Log in
    l = login(username, password)

    # return the car status, and the list of charge points
    a

    get chargers()



    return 'do some magic!'


def get_chargers(car_lat, car_lon ):
    # Filter chargers on route. (Nian)
    chargers = []

    # Calculate distances to charger. Order by nearest
    for charger in chargers:
        charg_lat = charger.get("lat")
        charg_lon = charger.get("lon")
        get_dist_to_charger(lat_here, long_here, lat_there, long_there):