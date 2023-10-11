# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.array_todolist import ArrayTodolist  # noqa: E501
from swagger_server.models.create_or_update_todolist import CreateOrUpdateTodolist  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.todolist import Todolist  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTodolistController(BaseTestCase):
    """TodolistController integration test stubs"""

    def test_todolist_get(self):
        """Test case for todolist_get

        Get All Todolist
        """
        query_string = [('include_done', false),
                        ('name', 'name_example')]
        response = self.client.open(
            '/api/v1/todolist',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_todolist_post(self):
        """Test case for todolist_post

        Create new Todolist
        """
        body = CreateOrUpdateTodolist()
        response = self.client.open(
            '/api/v1/todolist',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_todolist_todolist_id_delete(self):
        """Test case for todolist_todolist_id_delete

        Delete existing todolist
        """
        response = self.client.open(
            '/api/v1/todolist/{todolistId}'.format(todolist_id='todolist_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_todolist_todolist_id_put(self):
        """Test case for todolist_todolist_id_put

        Update existing todolist
        """
        body = CreateOrUpdateTodolist()
        response = self.client.open(
            '/api/v1/todolist/{todolistId}'.format(todolist_id='todolist_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
