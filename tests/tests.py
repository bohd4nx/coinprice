import unittest
from unittest.mock import patch, MagicMock
from api_handling import get_crypto_price
from telegram_bot import send_message

class TestAPIHandling(unittest.TestCase):

    @patch('api_handling.requests.get')
    def test_get_crypto_price(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {'bitcoin': {'usd': 50000}}
        mock_get.return_value = mock_response

        price = get_crypto_price('bitcoin')
        self.assertEqual(price, 50000)

class TestTelegramBot(unittest.TestCase):

    @patch('telegram_bot.requests.post')
    def test_send_message(self, mock_post):
        send_message('Test message')
        mock_post.assert_called_once()

if __name__ == "__main__":
    unittest.main()
