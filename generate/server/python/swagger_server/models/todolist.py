# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Todolist(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, name: str=None, priority: float=None, tags: List[str]=None):  # noqa: E501
        """Todolist - a model defined in Swagger

        :param id: The id of this Todolist.  # noqa: E501
        :type id: str
        :param name: The name of this Todolist.  # noqa: E501
        :type name: str
        :param priority: The priority of this Todolist.  # noqa: E501
        :type priority: float
        :param tags: The tags of this Todolist.  # noqa: E501
        :type tags: List[str]
        """
        self.swagger_types = {
            'id': str,
            'name': str,
            'priority': float,
            'tags': List[str]
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'priority': 'priority',
            'tags': 'tags'
        }
        self._id = id
        self._name = name
        self._priority = priority
        self._tags = tags

    @classmethod
    def from_dict(cls, dikt) -> 'Todolist':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Todolist of this Todolist.  # noqa: E501
        :rtype: Todolist
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Todolist.


        :return: The id of this Todolist.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Todolist.


        :param id: The id of this Todolist.
        :type id: str
        """

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this Todolist.


        :return: The name of this Todolist.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Todolist.


        :param name: The name of this Todolist.
        :type name: str
        """

        self._name = name

    @property
    def priority(self) -> float:
        """Gets the priority of this Todolist.


        :return: The priority of this Todolist.
        :rtype: float
        """
        return self._priority

    @priority.setter
    def priority(self, priority: float):
        """Sets the priority of this Todolist.


        :param priority: The priority of this Todolist.
        :type priority: float
        """

        self._priority = priority

    @property
    def tags(self) -> List[str]:
        """Gets the tags of this Todolist.


        :return: The tags of this Todolist.
        :rtype: List[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags: List[str]):
        """Sets the tags of this Todolist.


        :param tags: The tags of this Todolist.
        :type tags: List[str]
        """

        self._tags = tags