# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Charger(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, lat=None, long=None, network=None, dist_miles=None, dist_km=None, extra_time=None, other=None):  # noqa: E501
        """Charger - a model defined in Swagger

        :param lat: The lat of this Charger.  # noqa: E501
        :type lat: str
        :param long: The long of this Charger.  # noqa: E501
        :type long: str
        :param network: The network of this Charger.  # noqa: E501
        :type network: str
        :param dist_miles: The dist_miles of this Charger.  # noqa: E501
        :type dist_miles: str
        :param dist_km: The dist_km of this Charger.  # noqa: E501
        :type dist_km: str
        :param extra_time: The extra_time of this Charger.  # noqa: E501
        :type extra_time: str
        :param other: The other of this Charger.  # noqa: E501
        :type other: str
        """
        self.swagger_types = {
            'lat': str,
            'long': str,
            'network': str,
            'dist_miles': str,
            'dist_km': str,
            'extra_time': str,
            'other': str
        }

        self.attribute_map = {
            'lat': 'lat',
            'long': 'long',
            'network': 'network',
            'dist_miles': 'dist_miles',
            'dist_km': 'dist_km',
            'extra_time': 'extra_time',
            'other': 'other'
        }

        self._lat = lat
        self._long = long
        self._network = network
        self._dist_miles = dist_miles
        self._dist_km = dist_km
        self._extra_time = extra_time
        self._other = other

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The charger of this Charger.  # noqa: E501
        :rtype: Charger
        """
        return util.deserialize_model(dikt, cls)

    @property
    def lat(self):
        """Gets the lat of this Charger.

        latitude  # noqa: E501

        :return: The lat of this Charger.
        :rtype: str
        """
        return self._lat

    @lat.setter
    def lat(self, lat):
        """Sets the lat of this Charger.

        latitude  # noqa: E501

        :param lat: The lat of this Charger.
        :type lat: str
        """

        self._lat = lat

    @property
    def long(self):
        """Gets the long of this Charger.

        longitude  # noqa: E501

        :return: The long of this Charger.
        :rtype: str
        """
        return self._long

    @long.setter
    def long(self, long):
        """Sets the long of this Charger.

        longitude  # noqa: E501

        :param long: The long of this Charger.
        :type long: str
        """

        self._long = long

    @property
    def network(self):
        """Gets the network of this Charger.

        Network station is on.  # noqa: E501

        :return: The network of this Charger.
        :rtype: str
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this Charger.

        Network station is on.  # noqa: E501

        :param network: The network of this Charger.
        :type network: str
        """

        self._network = network

    @property
    def dist_miles(self):
        """Gets the dist_miles of this Charger.

        The distance in miles  # noqa: E501

        :return: The dist_miles of this Charger.
        :rtype: str
        """
        return self._dist_miles

    @dist_miles.setter
    def dist_miles(self, dist_miles):
        """Sets the dist_miles of this Charger.

        The distance in miles  # noqa: E501

        :param dist_miles: The dist_miles of this Charger.
        :type dist_miles: str
        """

        self._dist_miles = dist_miles

    @property
    def dist_km(self):
        """Gets the dist_km of this Charger.

        The distance in km  # noqa: E501

        :return: The dist_km of this Charger.
        :rtype: str
        """
        return self._dist_km

    @dist_km.setter
    def dist_km(self, dist_km):
        """Sets the dist_km of this Charger.

        The distance in km  # noqa: E501

        :param dist_km: The dist_km of this Charger.
        :type dist_km: str
        """

        self._dist_km = dist_km

    @property
    def extra_time(self):
        """Gets the extra_time of this Charger.

        Extra time needed  # noqa: E501

        :return: The extra_time of this Charger.
        :rtype: str
        """
        return self._extra_time

    @extra_time.setter
    def extra_time(self, extra_time):
        """Sets the extra_time of this Charger.

        Extra time needed  # noqa: E501

        :param extra_time: The extra_time of this Charger.
        :type extra_time: str
        """

        self._extra_time = extra_time

    @property
    def other(self):
        """Gets the other of this Charger.

        Other possible details.  # noqa: E501

        :return: The other of this Charger.
        :rtype: str
        """
        return self._other

    @other.setter
    def other(self, other):
        """Sets the other of this Charger.

        Other possible details.  # noqa: E501

        :param other: The other of this Charger.
        :type other: str
        """

        self._other = other
