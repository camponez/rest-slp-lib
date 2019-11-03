"""Module Address"""
import json

from slp_lib.api import API
from slp_lib.slp import SLP


class Address(API):
    """
    Class Address
    """

    def __init__(self, address):
        API.__init__(self)
        self.address = address
        self._balance = None
        self._bch_balance = None
        self._slp_address = None
        self._legacy_address = None
        self._cash_address = None
        self.tokens = {}

        self._load()

    @property
    def balance(self):
        """
        Balance Property
        """
        balance = {}
        balance['bch'] = self._bch_balance
        balance['tokens'] = self.tokens
        return balance

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

    def _load(self):
        self.api_url = "{}/address/details/{}".format(self.base_url,
                                                      self.address)
        response = json.loads(self.get())
        self._bch_balance = response['balance']
        self.slp_address = response['slpAddress']
        self.legacy_address = response['legacyAddress']
        self.cash_address = response['cashAddress']

    def load_tokens(self):
        """
        Load Balance of tokens
        """
        self.tokens = {}
        self.api_url = '{}/slp/balancesForAddress/{}'.format(self.base_url,
                                                             self.slp_address)

        l_tokens = json.loads(self.get())

        for token in l_tokens:
            slp = SLP(token['tokenId'])
            self.tokens[slp.symbol] = token['balance']
