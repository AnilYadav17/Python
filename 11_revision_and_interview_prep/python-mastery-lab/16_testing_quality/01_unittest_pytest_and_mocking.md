# Lesson 16.1: Professional Testing — `unittest`, `pytest`, & `unittest.mock`

## 1. What Is This in Simple Words?
Writing code is easy; knowing that your code **won't break tomorrow** when you make changes requires automated testing.  
- **Unit Testing**: Testing the smallest individual piece of code (a single function or method) in isolation.
- **Integration Testing**: Testing how multiple components (like your code and a database or filesystem) work together.
- **Mocking**: Creating fake "stunt doubles" for slow or dangerous dependencies (like payment gateways, third-party APIs, or sending real emails) during tests.

---

## 2. Testing with Python's Built-In `unittest`

Every Python installation comes with `unittest`:
```python
import unittest

def calculate_discount(price: float, discount_percent: float) -> float:
    if not (0 <= discount_percent <= 100):
        raise ValueError("Discount must be between 0 and 100")
    return price * (1 - discount_percent / 100)

class TestDiscountCalculator(unittest.TestCase):
    def setUp(self):
        # Runs BEFORE every test method
        self.standard_price = 100.0

    def test_valid_discount(self):
        result = calculate_discount(self.standard_price, 20)
        self.assertAlmostEqual(result, 80.0)

    def test_zero_discount(self):
        result = calculate_discount(self.standard_price, 0)
        self.assertEqual(result, 100.0)

    def test_invalid_negative_discount_raises_error(self):
        # Verify that ValueError is properly raised:
        with self.assertRaises(ValueError):
            calculate_discount(self.standard_price, -10)

if __name__ == "__main__":
    unittest.main()
```

---

## 3. Mocking External Services with `unittest.mock`

Never let your automated tests make real HTTP requests or charge real credit cards! Use `unittest.mock.patch`:

```python
from unittest.mock import patch
import unittest

def fetch_weather(city: str) -> str:
    # Imagine this makes an actual HTTP request to a weather API
    import urllib.request
    with urllib.request.urlopen(f"https://api.weather.com/{city}") as resp:
        return resp.read().decode("utf-8")

class TestWeatherAPI(unittest.TestCase):
    @patch("urllib.request.urlopen")
    def test_fetch_weather_mocked(self, mock_urlopen):
        # Configure fake mock response:
        mock_response = mock_urlopen.return_value.__enter__.return_value
        mock_response.read.return_value = b'{"temp": 24, "condition": "Sunny"}'

        result = fetch_weather("Berlin")
        self.assertIn("Sunny", result)
        # Verify the mock was called once:
        mock_urlopen.assert_called_once()
```

---

## 4. Mind-Blowing Facts! 💡

> **Fact 1: MagicMock Can Pretend to Be ANYTHING!**  
> `MagicMock` in Python automatically implements almost all dunder methods! You can iterate over it, call it like a function, access non-existent attributes, subscript it like a dictionary, and it will never crash:
> ```python
> from unittest.mock import MagicMock
> fake = MagicMock()
> fake.any_method().whatever_property[0].execute()  # Doesn't crash! Returns another MagicMock!
> ```
>
> **Fact 2: Flaky Tests are Silent Killers!**  
> Tests that rely on `time.sleep()`, current system clock (`datetime.now()`), or network availability are called "flaky tests" (they pass 95% of the time, and fail randomly). Professional engineers use frozen time (`freezegun`) and strict mocking to ensure tests run deterministically in milliseconds!

---

## 5. Self-Test
1. **Question**: Why is it dangerous to let unit tests hit live production APIs?
   - *Answer*: It makes tests slow, causes flaky failures when the network dips, can exhaust rate limits, and could accidentally modify live production data.
