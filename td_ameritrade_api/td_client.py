from .auth import access_token
from .errors import ApiError
from .data import quote, search, price_history, fundamental
from .accounts import account, transactions, positions, available_funds
from .helpers import api_call
from .trading import orders, place_conditional_order_data, place_conditional_order, buy_limit
from .watchlist import watchlists, watchlist

class client:

    def __init__(self, refresh_token, consumer_key, account_id=""):
        self.__refresh_token = refresh_token
        self.__consumer_key = consumer_key
        self.account_id = account_id

        self.__refresh_access_token()

    def __refresh_access_token(self):
        try:
            self.__access_token = access_token(self.__refresh_token, self.__consumer_key)
        except ApiError as error:
            raise Exception(f"Error authenticating", ApiError)

    @api_call
    def available_funds(self):
        return available_funds(self.account_id, self.__access_token)

    @api_call
    def quote(self, symbol):
        return quote(symbol, self.__access_token)

    @api_call
    def search(self, symbol):
        return search(symbol, self.__access_token)

    @api_call
    def account(self):
        return account(self.account_id, self.__access_token)

    @api_call
    def orders(self):
        return orders(self.account_id, self.__access_token)

    @api_call
    def transactions(self):
        return transactions(self.account_id, self.__access_token)

    @api_call
    def watchlists(self):
        return watchlists(self.account_id, self.__access_token)

    @api_call
    def watchlist(self, watchlist_id):
        return watchlist(watchlist_id, self.account_id, self.__access_token)

    @api_call
    def fundamental(self, symbol):
        return fundamental(symbol, self.__access_token)

    @api_call
    def price_history(self, symbol, *, period_type='day', period=1, frequency_type='minute', frequency=1, start_date=None, end_date=None, need_extended_hours_data=False):
        return price_history(symbol, self.__access_token, period_type=period_type, period=period, frequency_type=frequency_type, frequency=frequency, start_date=start_date, end_date=end_date, need_extended_hours_data=need_extended_hours_data)

    @api_call
    def place_conditional_order_data(self, symbol, price_to_sell, quantity, buy_price=None):
        return place_conditional_order_data(self.account_id, symbol, price_to_sell, quantity, self.__access_token, buy_price=buy_price)

    @api_call
    def positions(self):
        return positions(self.account_id, self.__access_token)

    @api_call
    def place_conditional_order(self, symbol, price_to_sell, quantity, buy_price=None):
        return place_conditional_order(self.account_id, symbol, price_to_sell, quantity, self.__access_token, buy_price=buy_price)

    @api_call
    def buy_limit(self, symbol, price, quantity):
        return buy_limit(self.account_id, symbol, price, quantity, self.__access_token)
