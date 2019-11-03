"""Test Address"""
import os
from unittest.mock import MagicMock
from unittest.mock import patch
from slp_lib.address import Address

FIXTURE_DIR = os.path.dirname(os.path.realpath(__file__))


def test_address_details():
    """Test Address Details."""
    response = open(FIXTURE_DIR + '/fixtures/address.json').read()

    with patch('slp_lib.api.API.get') as mock_api_get:
        mock_api_get.return_value = response
        address = Address('ADRESS_TEST')

        assert address.balance['bch'] == 0.01
        assert address.slp_address == 'simpleledger:qzs02v05l7qs5s24srqju498qu55dwuj0c20jv8m5x'
        assert address.legacy_address == '1Fg4r9iDrEkCcDmHTy2T79EusNfhyQpu7W'
        assert address.cash_address == 'bitcoincash:qzs02v05l7qs5s24srqju498qu55dwuj0cx5ehjm2c'


def test_load_tokens():
    """
    Test balance on tokens
    """
    r_token_crz = open(FIXTURE_DIR + '/fixtures/token_57d9.json').read()
    r_token_crp = open(FIXTURE_DIR + '/fixtures/token_9da8.json').read()
    r_address = open(FIXTURE_DIR + '/fixtures/address.json').read()
    r_balance = open(FIXTURE_DIR + '/fixtures/balances_token.json').read()

    with patch('slp_lib.api.API.get') as mock_api_get:
        mock_api_get.side_effect = [r_address, r_balance, r_token_crz,
                                    r_token_crp]

        adr = Address('ADR_TEST')
        adr.load_tokens()
        assert adr.balance['bch'] == 0.01
        assert adr.balance['tokens'] == {'CRZ': 100, 'CRP': 9}


def test_balance():
    r_token_crz = open(FIXTURE_DIR + '/fixtures/token_57d9.json').read()
    r_token_crp = open(FIXTURE_DIR + '/fixtures/token_9da8.json').read()
    r_address = open(FIXTURE_DIR + '/fixtures/address.json').read()
    r_balance = open(FIXTURE_DIR + '/fixtures/balances_token.json').read()

    with patch('slp_lib.api.API.get') as mock_api_get:
        mock_api_get.side_effect = [r_address, r_balance, r_token_crz,
                                    r_token_crp]

        adr = Address('ADR_TEST')
        adr.load_tokens()
        assert adr.balance == {
            'bch': 0.01,
            'tokens': {'CRZ': 100, 'CRP': 9}
        }


def test_balance_no_tokens():
    r_address = open(FIXTURE_DIR + '/fixtures/address.json').read()

    with patch('slp_lib.api.API.get') as mock_api_get:
        mock_api_get.side_effect = [r_address, "{}"]
        adr = Address('ADR_TEST')
        adr.load_tokens()
        assert adr.balance == {
            'bch': 0.01,
            'tokens': {}
        }
