import requests
from .errors import ApiError
from .helpers import base_url

def quote(ticker, access_token):
    headers = {'Authorization': f"Bearer {access_token}"}

    r = requests.get(base_url(f'/marketdata/{ticker}/quotes'), headers=headers)
    if r.status_code != 200:
        raise ApiError(f"GET /marketdata/{ticker}/quotes", r.status_code, r.json()['error'])

    return r.json()

def search(symbol, access_token):
    headers = {'Authorization': f"Bearer {access_token}"}
    params = {'symbol': symbol, 'projection': 'symbol-search'}

    r = requests.get(base_url('/instruments'), headers=headers, params=params)
    if r.status_code != 200:
        raise ApiError(f"GET /instruments", r.status_code, r.json()['error'])

    return r.json()

def fundamental(symbol, access_token):
    headers = {'Authorization': f"Bearer {access_token}"}
    params = {'symbol': symbol, 'projection': 'fundamental'}

    r = requests.get(base_url('/instruments'), headers=headers, params=params)
    if r.status_code != 200:
        raise ApiError(f"GET /instruments", r.status_code, r.json()['error'])

    return r.json()

# Start and end date are time since epoch. Use periods if not using start and end date.
def price_history(symbol, access_token, *, period_type='day', period=1, frequency_type='minute', frequency=1, start_date=None, end_date=None, need_extended_hours_data=False):
    headers = {'Authorization': f"Bearer {access_token}"}
    params = { 'periodType': period_type, 'frequencyType': frequency_type, 'frequency': frequency, 'needExtendendHoursData': need_extended_hours_data }
    if start_date and end_date:
        params.update({'startDate': start_date, 'endDate': end_date})
    else:
        params.update({'period': period})

    r = requests.get(base_url(f'/marketdata/{symbol}/pricehistory'), headers=headers, params=params)
    if r.status_code != 200:
        raise ApiError(f"GET /marketdata/{symbol}/pricehistory", r.status_code, r.json()['error'])

    return r.json()
