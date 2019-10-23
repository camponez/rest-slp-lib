"""Test Address"""
import os
from unittest.mock import patch
from slp_lib.address import Address

FIXTURE_DIR = os.path.dirname(os.path.realpath(__file__))


def test_address_details():
    """Test Address Details."""
    response = open(FIXTURE_DIR + '/fixtures/address.json').read()

    with patch('slp_lib.api.API.get') as mock_api_get:
        mock_api_get.return_value = response
        address = Address('ADRESS_TEST')

        assert address.balance == 0.01
        assert address.slp_address == 'simpleledger:qzs02v05l7qs5s24srqju498qu55dwuj0c20jv8m5x'
        assert address.legacy_address == '1Fg4r9iDrEkCcDmHTy2T79EusNfhyQpu7W'
        assert address.cash_address == 'bitcoincash:qzs02v05l7qs5s24srqju498qu55dwuj0cx5ehjm2c'
