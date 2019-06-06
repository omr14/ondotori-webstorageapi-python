"""
Pyhton Client for ONDOTORI WebStorage API
TR-7wf/nw series
API reference
https://ondotori.webstorage.jp/docs/api/index.html
"""
import requests
import json

from .exception import detect_exception

class WebStorageAPIClient:

    def __init__(self, auth):

        self.url_prefix = 'https://api.webstorage.jp/v1/'
        self.base_body = auth
        self.headers = {
            'Host': 'api.webstorage.jp:443',
            'Content-Type': 'application/json',
            'X-HTTP-Method-Override': 'GET'
        }

    def post(self, path, params, headers=None):
        """ post to api
        Args:
            path (str): path to API request endpoint.    
            params (dict): parameters for request.
            headers (dict): headers for request.
        Returns:
            requets Response object
        """
        url = self.url_prefix + path
        response = requests.post(url, json=params, headers=headers)

        if response.ok:
            return response
        else:
            detect_exception(response) 
            # error = response.json()['error']
            # raise RuntimeError('code:{}, message:{}'.format(error['code'], error['message']))

    def get_current(self, device_serials=None):
        """ Get Current
        Args:
            device_serials (list, optional): serial ids of ONDOTORI devices
                all current device data was taken if parameter is null
        Returns:
            requests Response object
        """
        body = self.base_body.copy()
        if device_serials is not None:
            body['remote-serial'] = device_serials
        return self.post('devices/current', body, self.headers)

    def get_latest(self, device_serial):
        """ Get latest-data of one device max samples is limited 300
        Args:
            device_serial (str): serial id of ONDOTORI device
        Returns:
            requests Response object
        """
        body = self.base_body.copy()
        body['remote-serial'] = device_serial
        return self.post('devices/latest-data', body, self.headers)

    def get_data(self, device_serial):
        """ Get
        Args:
            device_serial (str): serial id of ONDOTORI device
        Returns:
            requests Response object
        """
        body = self.base_body.copy()
        body['remote-serial'] = device_serial
        return self.post('devices/data', body, self.headers)
