# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InlineResponse200(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, success: bool=None):  # noqa: E501
        """InlineResponse200 - a model defined in Swagger

        :param success: The success of this InlineResponse200.  # noqa: E501
        :type success: bool
        """
        self.swagger_types = {
            'success': bool
        }

        self.attribute_map = {
            'success': 'success'
        }
        self._success = success

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse200':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200 of this InlineResponse200.  # noqa: E501
        :rtype: InlineResponse200
        """
        return util.deserialize_model(dikt, cls)

    @property
    def success(self) -> bool:
        """Gets the success of this InlineResponse200.


        :return: The success of this InlineResponse200.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success: bool):
        """Sets the success of this InlineResponse200.


        :param success: The success of this InlineResponse200.
        :type success: bool
        """

        self._success = success
