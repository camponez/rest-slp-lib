import os
from slp_lib.slp import SLP
from unittest.mock import patch

FIXTURE_DIR = os.path.dirname(os.path.realpath(__file__))

# pylint: disable=line-too-long


def test_list():
    """
    Test List token
    """
    response = open(FIXTURE_DIR + '/fixtures/slp.json').read()
    with patch('slp_lib.api.API.get') as mock_api_get:
        mock_api_get.return_value = response
        slp = SLP('57d92951dd4e545d42535e12a70f20fab2139caf36c4700afcaf945c60a8c797')

        assert slp.name == 'Cruzeiro'
        assert slp.symbol == 'CRZ'
        assert slp.total_minted == 400
        assert slp.version_type == 1


def test_convert():
    """
    Test convert address
    """
    response = open(FIXTURE_DIR + '/fixtures/convert.json').read()
    with patch('slp_lib.api.API.get') as mock_api_get:
        mock_api_get.return_value = response
        slp_cls = SLP()
        slp = slp_cls.convert_adr(
            'simpleledger:qz9tzs6d5097ejpg279rg0rnlhz546q4fsnck9wh5m')
        assert slp['slpAddress'] == 'simpleledger:qz9tzs6d5097ejpg279rg0rnlhz546q4fsnck9wh5m'
        assert slp['cashAddress'] == 'bitcoincash:qz9tzs6d5097ejpg279rg0rnlhz546q4fslra7mh29'
        assert slp['legacyAddress'] == '1DeLbv5EMzLEFDvQ8wZiKeSuPGGtSSz5HP'
