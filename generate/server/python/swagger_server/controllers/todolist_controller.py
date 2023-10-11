import connexion
import six

from swagger_server.models.array_todolist import ArrayTodolist  # noqa: E501
from swagger_server.models.create_or_update_todolist import CreateOrUpdateTodolist  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.todolist import Todolist  # noqa: E501
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


def todolist_post(body):  # noqa: E501
    """Create new Todolist

    Create new active todolist # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Todolist
    """
    if connexion.request.is_json:
        body = CreateOrUpdateTodolist.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def todolist_todolist_id_delete(todolist_id):  # noqa: E501
    """Delete existing todolist

    Delete existing todolist in database # noqa: E501

    :param todolist_id: TodoList id for updated
    :type todolist_id: str

    :rtype: InlineResponse200
    """
    return 'do some magic!'


def todolist_todolist_id_put(body, todolist_id):  # noqa: E501
    """Update existing todolist

    Update existing todolist in database # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param todolist_id: TodoList id for updated
    :type todolist_id: str

    :rtype: Todolist
    """
    if connexion.request.is_json:
        body = CreateOrUpdateTodolist.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
