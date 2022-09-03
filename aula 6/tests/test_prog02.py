import unittest
from unittest.mock import MagicMock, patch
from prog02 import retorna_info_criptomoeda


class TestProg02(unittest.TestCase):

    @patch("prog02.requests")
    def test_criptomoeda_deve_retornar_info_sobre_criptomoeda(self, mock_requests):

        mock_response = MagicMock()
        mock_response.json.return_value = {
            "data": {
                "id": "bitcoin",
                "rank": "1",
                "symbol": "BTC",
                "name": "Bitcoin",
                "supply": "19140231.0000000000000000",
                "maxSupply": "21000000.0000000000000000",
                "marketCapUsd": "377498029396.0075500634399263",
                "volumeUsd24Hr": "7029527231.1855548412979494",
                "priceUsd": "19722.7520083747970473",
                "changePercent24Hr": "-0.9114117567179711",
                "vwap24Hr": "19867.7572029255987171",
                "explorer": "https://blockchain.info/"
            }
        }

        mock_requests.get.return_value = mock_response

        resultado = retorna_info_criptomoeda('bitcoin')

        self.assertEqual("Bitcoin", resultado[0])
        self.assertEqual("BTC", resultado[1])

        mock_requests.get.assert_called_once_with('https://api.coincap.io/v2/assets/bitcoin')
        mock_response.json.assert_called_once()