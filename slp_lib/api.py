"""API"""
import requests


class API:
    """
    Class API
    """

    def __init__(self):
        self.base_url = 'https://rest.bitcoin.com/v2'
        self.api_url = None

    def get(self):
        """
        Get
        """
        response = requests.get(self.api_url)
        if not response.ok:
            raise requests.ConnectionError
        return requests.get(self.api_url).content
