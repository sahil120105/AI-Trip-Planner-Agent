import requests
# You need the alpha_vantage package for this to work
from alpha_vantage.foreignexchange import ForeignExchange

class CurrencyConverter:
    """
    Converts currency using the Alpha Vantage 'Realtime Currency Exchange Rate' endpoint.
    
    This class is intended to be used by CurrencyConverterTool and expects an 
    ALPHA_VANTAGE_API_KEY.
    """
    def __init__(self, api_key: str):
        # Initialize the ForeignExchange wrapper from alpha_vantage
        # This wrapper handles the API endpoint, status codes, and data parsing.
        self.fe = ForeignExchange(key=api_key)
    
    def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
        """Convert the amount from one currency to another using the real-time rate."""
        
        # 1. Call the Alpha Vantage API for the exchange rate
        try:
            # Alpha Vantage's get_currency_exchange_rate returns a tuple: (data_dict, metadata)
            data, _ = self.fe.get_currency_exchange_rate(
                from_currency=from_currency,
                to_currency=to_currency
            )
        except Exception as e:
            # Catch errors from the alpha_vantage wrapper (e.g., connection issues, rate limits)
            raise Exception(f"Alpha Vantage API call failed: {e}")

        # 2. Extract the exchange rate from the Alpha Vantage response structure
        # The real-time rate is consistently found under the key '5. Exchange Rate'.
        try:
            exchange_rate = float(data['5. Exchange Rate'])
        except (KeyError, ValueError):
            # Handle cases where the API returns an error message instead of data (e.g., invalid currency codes)
            if 'Error Message' in data:
                 raise ValueError(f"Alpha Vantage Error: {data['Error Message']}")
            raise ValueError("Could not find the exchange rate in the Alpha Vantage API response.")

        # 3. Calculate and return the converted amount
        return amount * exchange_rate