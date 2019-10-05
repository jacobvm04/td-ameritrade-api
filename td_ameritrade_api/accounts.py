import requests
from .errors import ApiError
from .helpers import base_url

def account(account_id, access_token):
    headers = {'Authorization': f"Bearer {access_token}"}

    r = requests.get(base_url(f'/accounts/{account_id}'), headers=headers)
    if r.status_code != 200:
        raise ApiError(f"GET /accounts/{account_id}", r.status_code, r.json()['error'])

    return r.json()

def transactions(account_id, access_token):
    headers = {'Authorization': f"Bearer {access_token}"}

    r = requests.get(base_url(f'/accounts/{account_id}/transactions'), headers=headers)
    if r.status_code != 200:
        raise ApiError(f"GET /accounts/{account_id}/transactions", r.status_code, r.json()['error'])

    return r.json()

def positions(account_id, access_token):
    headers = {'Authorization': f"Bearer {access_token}"}
    params = {'fields': 'positions,orders'}

    r = requests.get(base_url(f'/accounts/{account_id}'), headers=headers, params=params)
    if r.status_code != 200:
        raise ApiError(f"GET /accounts/{account_id}", r.status_code, r.json()['error'])

    return r.json()['securitiesAccount']['positions']

def available_funds(account_id, access_token):
    headers = {'Authorization': f"Bearer {access_token}"}

    r = requests.get(base_url(f'/accounts/{account_id}'), headers=headers)
    if r.status_code != 200:
        raise ApiError(f"GET /accounts/{account_id}", r.status_code, r.json()['error'])

    return r.json()['securitiesAccount']['currentBalances']['availableFunds']

