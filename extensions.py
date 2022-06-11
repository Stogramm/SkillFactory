import requests
import json
from config import *

class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f'Нельзя конвертировать {quote} в {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не получилось обработать валюту {quote}.')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не получилось обработать валюту {base}.')

        try:
            amount = int(amount)
        except ValueError:
            raise ConvertionException(f'Ошибка в количестве валюты {amount}.')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total = json.loads(r.content)[keys[base]]
        total_base = total * amount

        return total_base
