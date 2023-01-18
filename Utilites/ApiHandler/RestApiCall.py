import json

import requests

from Utilites.ApiHandler.ApiExceptionHandler import ThirdPartyApiException


class RestApiCall:

    def __init__(self):
        pass

    @staticmethod
    def get_headers(access_token):
        """
        """
        headers = {"app-client": "stnkManagement", "Content-Type": "application/json"}
        if access_token:
            headers["access-token"] = access_token
        return headers

    def request_get(self, url, access_token, query=None):
        """
        query = {'key1': 'value1', 'key2': 'value2'}
        https://httpbin.org/get?key2=value2&key1=value1
        """
        params = query or {}
        headers = self.get_headers(access_token)
        response = requests.get(url, params=params, headers=headers)
        if response.status_code == 200:
            return response.json()
        raise ThirdPartyApiException(response.status_code, str(response.content))

    def request_put(self, url, access_token, body=None):
        """
        """
        data = json.dump(body) if body else json.dumps({})
        headers = self.get_headers(access_token)
        response = requests.put(url, data=data, headers=headers)
        if response.status_code == 200:
            return True
        raise ThirdPartyApiException(response.status_code, str(response.content))

    def request_post(self, url, access_token, body=None):
        """
        """
        data = json.dump(body) if body else json.dumps({})
        headers = self.get_headers(access_token)
        response = requests.post(url, data=data, headers=headers)

        if response.status_code == 200:
            return response.json()
        raise ThirdPartyApiException(response.status_code, str(response.content))

    def request_delete(self, url, access_token, body=None):
        """
        """
        data = json.dump(body) if body else json.dumps({})
        headers = self.get_headers(access_token)
        response = requests.delete(url, data=data, headers=headers)

        if response.status_code == 200:
            return response.json()
        raise ThirdPartyApiException(response.status_code, str(response.content))
