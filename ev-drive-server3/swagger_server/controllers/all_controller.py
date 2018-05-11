import connexion
import six
import logging
from swagger_server.models.all_info import AllInfo  # noqa: E501
from swagger_server import util
import status_controller


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

    # Get charge info from car
    leaf_info = l.get_latest_battery_status()
    perc_charge = leaf_info.state_of_charge



    # Get current location from car
    lon_from, lat_from = get_location(l)
    lon_lat_from = lon_from + " " + lat_from)

    # Filter chargers on route (Nian)

    # Calculate distances to charger, and from charger to end point. Order by nearest


    # return the car status, and the list of charge points






    return 'do some magic!'
