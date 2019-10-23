import requests
import pytest
from unittest.mock import patch
from slp_lib.api import API


@patch('requests.get')
def test_connection_error(mock_get):
    """
    Test connection error
    """
    mock_get.return_value.ok = False

    with pytest.raises(requests.ConnectionError):
        api = API()
        api.get()


@patch('requests.get')
def test_get(mock_get):
    """
    Test get
    """
    mock_get.return_value.ok = True
    api = API()
    api.get()

    assert api.api_url == 'https://rest.bitcoin.com/v2'
    mock_get.call_once()
