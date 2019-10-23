"""
Module SLP
"""
import json
from slp_lib.api import API


class SLP(API):
    """
    Class SLP
    """

    def __init__(self, id=None):
        API.__init__(self)
        self.id = id
        self._name = None
        self._symbol = None
        self._version_type = None
        self._total_minted = None

        if self.id:
            self._load()

    def convert_adr(self, adr):
        """
        Convert address
        """
        self.api_url += '/slp/convert/{}'.format(adr)
        return json.loads(self.get())

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def _load(self):
        """
        Load info
        """
        self.api_url += '/slp/list/{}'.format(self.id)
        response = json.loads(self.get())

        self.name = response['name']
        self.symbol = response['symbol']
        self.total_minted = response['totalMinted']
        self.version_type = response['versionType']
