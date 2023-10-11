# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.array_todolist import ArrayTodolist  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAllController(BaseTestCase):
    """AllController integration test stubs"""

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


if __name__ == '__main__':
    import unittest
    unittest.main()
