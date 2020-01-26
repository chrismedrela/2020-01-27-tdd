import datetime

import requests


class NoData(Exception):
    pass


API_ENDPOINT = 'http://api.nbp.pl/api/exchangerates/tables/a/{}/?format=json'
DATE_FORMAT = '%Y-%m-%d'

def get_exchange_rate(currency, date):
    currency = currency.upper()
    date_as_str = date.strftime(DATE_FORMAT)
    url = API_ENDPOINT.format(date_as_str)
    response = requests.get(url)
    if response.status_code == 404:
        raise NoData
    json = response.json()
    rates = [rate['mid'] for rate in json[0]['rates']
             if rate['code'] == currency]
    try:
        rate = rates[0]
    except IndexError:
        raise ValueError("Invalid currency")
    else:
        return rate