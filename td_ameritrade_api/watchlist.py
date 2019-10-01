import requests
from .errors import ApiError
from .helpers import base_url

def watchlists(account_id, access_token):
    headers = {'Authorization': f"Bearer {access_token}"}

    r = requests.get(base_url(f'/accounts/{account_id}/watchlists'), headers=headers)
    if r.status_code != 200:
        raise ApiError(f"GET /accounts/{account_id}/watchlists", r.status_code, r.json()['error'])

    return r.json()

def watchlist(watchlist_id, account_id, access_token):
    headers = {'Authorization': f"Bearer {access_token}"}

    r = requests.get(base_url(f'/accounts/{account_id}/watchlists/{watchlist_id}'), headers=headers)
    if r.status_code != 200:
        raise ApiError(f"GET /accounts/{account_id}/watchlists/{watchlist_id}", r.status_code, r.json()['error'])

    return r.json()
