import requests
from .errors import ApiError
from .helpers import base_url
from .data import quote

def orders(account_id, access_token):
    headers = {'Authorization': f"Bearer {access_token}"}
    # params = {'accountId': account_id}
    params = {}

    # r = requests.get(base_url(f'/orders'), headers=headers, params=params)
    r = requests.get(base_url(f'/accounts/{account_id}/orders'), headers=headers, params=params)
    if r.status_code != 200:
        # raise ApiError(f"GET /orders", r.status_code, r.json()['error'])
        raise ApiError(f"GET /accounts/{account_id}/orders", r.status_code, r.json()['error'])

    return r.json()

def place_conditional_order(account_id, symbol, price_to_sell, quantity, access_token, buy_price=None):
    price = 0

    if not buy_price:
        stock_quote = quote(symbol, access_token)
        price = stock_quote[symbol]['askPrice']
    else:
        price = buy_price


    headers = {'Authorization': f"Bearer {access_token}"}

    data = {
        "orderType": "LIMIT",
        "session": "NORMAL",
        "price": price,
        "duration": "DAY",
        "orderStrategyType": "TRIGGER",
        "orderLegCollection": [
            {
                "instruction": "BUY",
                "quantity": quantity,
                "instrument": {
                    "symbol": symbol,
                    "assetType": "EQUITY"
                }
            }
        ],
        "childOrderStrategies": [
            {
                "orderType": "LIMIT",
                "session": "NORMAL",
                "price": price_to_sell,
                "duration": "DAY",
                "orderStrategyType": "SINGLE",
                    "orderLegCollection": [
                        {
                            "instruction": "SELL",
                            "quantity": quantity,
                            "instrument": {
                                "symbol": symbol,
                                "assetType": "EQUITY"
                            }
                        }
                    ]
            }
        ]
    }

    r = requests.post(base_url(f'/accounts/{account_id}/orders'), headers=headers, json=data)
    if r.status_code != 200:
        raise ApiError(f"POST /accounts/{account_id}/orders", r.status_code, r.json()['error'])

    return r.json()

def buy_limit(account_id, symbol, price, quantity, access_token):

    headers = {'Authorization': f"Bearer {access_token}"}

    data = {
        "orderType": "LIMIT",
        "session": "NORMAL",
        "price": price,
        "duration": "DAY",
        "orderStrategyType": "SINGLE",
        "orderLegCollection": [
            {
                "instruction": "BUY",
                "quantity": quantity,
                "instrument": {
                    "symbol": symbol,
                    "assetType": "EQUITY"
                }
            }
        ]
    }

    r = requests.post(base_url(f'/accounts/{account_id}/orders'), headers=headers, json=data)
    if r.status_code != 200:
        raise ApiError(f"POST /accounts/{account_id}/orders", r.status_code, r.json()['error'])

    return r.json()

def place_conditional_order_data(account_id, symbol, price_to_sell, quantity, access_token, buy_price=None):
    price = 0

    if not buy_price:
        stock_quote = quote(symbol, access_token)
        price = stock_quote[symbol]['askPrice']
    else:
        price = buy_price

    data = {
        "orderType": "LIMIT",
        "session": "NORMAL",
        "price": price,
        "duration": "DAY",
        "orderStrategyType": "TRIGGER",
        "orderLegCollection": [
            {
                "instruction": "BUY",
                "quantity": quantity,
                "instrument": {
                    "symbol": symbol,
                    "assetType": "EQUITY"
                }
            }
        ],
        "childOrderStrategies": [
            {
                "orderType": "LIMIT",
                "session": "NORMAL",
                "price": price_to_sell,
                "duration": "DAY",
                "orderStrategyType": "SINGLE",
                    "orderLegCollection": [
                        {
                            "instruction": "SELL",
                            "quantity": quantity,
                            "instrument": {
                                "symbol": symbol,
                                "assetType": "EQUITY"
                            }
                        }
                    ]
            }
        ]
    }

    return data
