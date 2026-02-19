from unittest.mock import MagicMock
from unittest.mock import patch

from src.external_api import convert_to_rub


def test_convert_to_rub_ruble() -> None:
    transaction = {
        "operationAmount": {
            "amount": "100.0",
            "currency": {"code": "RUB"}
        }
    }
    assert convert_to_rub(transaction) == 100.0


@patch("src.external_api.requests.get")
@patch("src.external_api.os.getenv")
def test_convert_to_rub_usd(mock_getenv: MagicMock, mock_get: MagicMock) -> None:
    mock_getenv.return_value = "dummy_key"
    mock_response = MagicMock()
    mock_response.json.return_value = {"result": 7500.0}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    transaction = {
        "operationAmount": {
            "amount": "100.0",
            "currency": {"code": "USD"}
        }
    }
    assert convert_to_rub(transaction) == 7500.0
    mock_get.assert_called_once()


@patch("src.external_api.requests.get")
@patch("src.external_api.os.getenv")
def test_convert_to_rub_api_error(mock_getenv: MagicMock, mock_get: MagicMock) -> None:
    mock_getenv.return_value = "dummy_key"
    mock_get.side_effect = Exception("API error")

    transaction = {
        "operationAmount": {
            "amount": "100.0",
            "currency": {"code": "EUR"}
        }
    }
    assert convert_to_rub(transaction) == 0.0


def test_convert_to_rub_no_api_key() -> None:
    with patch("src.external_api.os.getenv", return_value=None):
        transaction = {
            "operationAmount": {
                "amount": "100.0",
                "currency": {"code": "USD"}
            }
        }
        assert convert_to_rub(transaction) == 0.0
