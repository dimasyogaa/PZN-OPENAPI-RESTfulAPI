import connexion
import six

from swagger_server.models.array_todolist import ArrayTodolist  # noqa: E501
from swagger_server import util


def todolist_get(include_done=None, name=None):  # noqa: E501
    """Get All Todolist

    Get all active todolist by default # noqa: E501

    :param include_done: Is include_done todolist
    :type include_done: bool
    :param name: Filter todolist by name
    :type name: str

    :rtype: ArrayTodolist
    """
    return 'do some magic!'
