import requests
from .errors import ApiError
from .helpers import base_url

"""Returns an access token when given a refresh token and consumer key"""
def access_token(refresh_token, consumer_key):
    data = {'grant_type': 'refresh_token', 'refresh_token': refresh_token, 'client_id': consumer_key}

    r = requests.post(base_url('/oauth2/token'), data=data)
    if r.status_code != 200:
        raise ApiError(f"POST /oauth2/token/", r.status_code, r.json()['error'])
    return r.json()['access_token']

