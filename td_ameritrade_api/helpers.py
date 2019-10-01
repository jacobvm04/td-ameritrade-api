from .errors import ApiError

def base_url(path):
    return 'https://api.tdameritrade.com/v1' + path

# Wraps the api call so that authentication is handled correctly
def api_call(func):
    def wrapped(*args, **kwargs):
        self = args[0]
        try:
            return func(*args, **kwargs)
        except ApiError as error:
            self.refresh_access_token()
            return func(*args, **kwargs)

    return wrapped
