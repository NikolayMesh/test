import requests
import json
from config import keys


class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(base: str, quote: str, amount: float):
        if quote == base:
            raise ConnectionError(f'Невозможно перевести одинаковые валюты {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConnectionError(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConnectionError(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConnectionError(f'Не удалось обработать количесво {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')
        total_base = json.loads(r.content)[keys[quote]]

        return total_base


