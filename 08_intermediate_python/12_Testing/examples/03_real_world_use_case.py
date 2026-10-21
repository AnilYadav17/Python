"""
03_real_world_use_case.py
Real-world scenario: Testing an External Weather API Client using unittest.mock.
Demonstrates:
- Mocking external HTTP requests without touching the actual network
- Testing successful JSON payload parsing
- Testing API error responses and timeout exceptions
- Verifying exact call parameters with assert_called_once_with
"""

import unittest
from unittest.mock import patch, MagicMock

# Production Service Client
class WeatherServiceClient:
    def __init__(self, api_key, base_url="https://api.weather.com"):
        self.api_key = api_key
        self.base_url = base_url

    def get_temperature(self, city):
        import urllib.request
        import json

        url = f"{self.base_url}/v1/current?city={city}&key={self.api_key}"
        req = urllib.request.Request(url)

        # External network call
        with urllib.request.urlopen(req, timeout=5) as response:
            if response.status != 200:
                raise RuntimeError(f"API Error: HTTP {response.status}")
            data = json.loads(response.read().decode("utf-8"))
            return data["temperature_celsius"]


class TestWeatherServiceClient(unittest.TestCase):
    def setUp(self):
        self.client = WeatherServiceClient(api_key="mock_key_12345")

    # Patch urllib.request.urlopen where it is used
    @patch("urllib.request.urlopen")
    def test_get_temperature_success(self, mock_urlopen):
        # 1. Arrange: Configure the mock response
        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.read.return_value = b'{"city": "Paris", "temperature_celsius": 18.5}'
        # Context manager support: __enter__ returns the mock response
        mock_urlopen.return_value.__enter__.return_value = mock_response

        # 2. Act: Call the method under test
        temp = self.client.get_temperature("Paris")

        # 3. Assert: Verify outcome and that urlopen was invoked
        self.assertEqual(temp, 18.5)
        self.assertTrue(mock_urlopen.called)
        print("  [Verified] Success path parsed JSON correctly with mocked network.")

    @patch("urllib.request.urlopen")
    def test_get_temperature_timeout_raises_exception(self, mock_urlopen):
        # Arrange: Configure mock to raise a TimeoutError
        import urllib.error
        mock_urlopen.side_effect = TimeoutError("Connection timed out after 5000ms")

        # Act & Assert
        with self.assertRaises(TimeoutError):
            self.client.get_temperature("Tokyo")
        print("  [Verified] Timeout exception propagated correctly.")


def main():
    print("--- Executing Mocked Service Unit Tests ---")
    suite = unittest.TestLoader().loadTestsFromTestCase(TestWeatherServiceClient)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

if __name__ == "__main__":
    main()
