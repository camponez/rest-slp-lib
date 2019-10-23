"""API"""
import requests


class API:
    """
    Class API
    """

    def __init__(self):
        self.api_url = 'https://rest.bitcoin.com/v2'

    def get(self):
        response = requests.get(self.api_url)
        if not response.ok:
            raise requests.ConnectionError
        return requests.get(self.api_url).content
