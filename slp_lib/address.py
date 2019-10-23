"""Module Address"""
import json

from slp_lib.api import API


class Address(API):
    """
    Class Address
    """

    def __init__(self, address):
        API.__init__(self)
        self._balance = None
        self._slp_address = None
        self._legacy_address = None
        self._cash_address = None

        self._load(address)

    @property
    def balance(self):
        """
        Balance Property
        """
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value

    @property
    def slp_address(self):
        """
        Property slp_address
        """
        return self._slp_address

    @slp_address.setter
    def slp_address(self, value):
        self._slp_address = value

    @property
    def legacy_address(self):
        """
        Property Legacy address
        """
        return self._legacy_address

    @legacy_address.setter
    def legacy_address(self, value):
        self._legacy_address = value

    @property
    def cash_address(self):
        """
        Property Cash Address
        """
        return self._cash_address

    @cash_address.setter
    def cash_address(self, value):
        self._cash_address = value

    def _load(self, address):
        self.api_url += "/address/details/{}".format(address)
        response = json.loads(self.get())
        self.balance = response['balance']
        self.slp_address = response['slpAddress']
        self.legacy_address = response['legacyAddress']
        self.cash_address = response['cashAddress']
