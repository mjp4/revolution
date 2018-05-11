# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class AllInfoCar(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, lat=None, long=None, charge=None):  # noqa: E501
        """AllInfoCar - a model defined in Swagger

        :param lat: The lat of this AllInfoCar.  # noqa: E501
        :type lat: str
        :param long: The long of this AllInfoCar.  # noqa: E501
        :type long: str
        :param charge: The charge of this AllInfoCar.  # noqa: E501
        :type charge: str
        """
        self.swagger_types = {
            'lat': str,
            'long': str,
            'charge': str
        }

        self.attribute_map = {
            'lat': 'lat',
            'long': 'long',
            'charge': 'charge'
        }

        self._lat = lat
        self._long = long
        self._charge = charge

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The allInfo_car of this AllInfoCar.  # noqa: E501
        :rtype: AllInfoCar
        """
        return util.deserialize_model(dikt, cls)

    @property
    def lat(self):
        """Gets the lat of this AllInfoCar.


        :return: The lat of this AllInfoCar.
        :rtype: str
        """
        return self._lat

    @lat.setter
    def lat(self, lat):
        """Sets the lat of this AllInfoCar.


        :param lat: The lat of this AllInfoCar.
        :type lat: str
        """

        self._lat = lat

    @property
    def long(self):
        """Gets the long of this AllInfoCar.


        :return: The long of this AllInfoCar.
        :rtype: str
        """
        return self._long

    @long.setter
    def long(self, long):
        """Sets the long of this AllInfoCar.


        :param long: The long of this AllInfoCar.
        :type long: str
        """

        self._long = long

    @property
    def charge(self):
        """Gets the charge of this AllInfoCar.

        The charge in watt hour  # noqa: E501

        :return: The charge of this AllInfoCar.
        :rtype: str
        """
        return self._charge

    @charge.setter
    def charge(self, charge):
        """Sets the charge of this AllInfoCar.

        The charge in watt hour  # noqa: E501

        :param charge: The charge of this AllInfoCar.
        :type charge: str
        """

        self._charge = charge