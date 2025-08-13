import unittest

import requests
from requests import Response

from py3_http_utils.response import RequestsResponseHandler

from py3_http_utils.response import HttpxResponseHandler


class MyTestCase(unittest.TestCase):
    def test_requests_response_handler(self):
        response = requests.get(url="https://www.baidu.com")

        def pretreatment(response: Response = None):
            response.encoding = response.apparent_encoding
            return response

        text = RequestsResponseHandler.text(response=response, pretreatment=None, condition=lambda x: response.ok)
        self.assertEqual(True, isinstance(text, str))  # add assertion here


if __name__ == '__main__':
    unittest.main()
