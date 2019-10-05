# API Reference

## Client

_`class`_ `td_ameritrade_api.`**`client`**`(`_`refresh_token, consumer_key, account_id`_`)`

### Parameters

* **refresh\_token** \(Required\[str\]\)  The oauth2 refresh token from the TD Ameritrade API used to obtain the access token to use the API.
* **consumer\_key** \(Required\[str\]\)  The API consumer key from when you create an app on TD's developer website.
* **account\_id** \(Optional\[str\]\)  Your account id which is needed to view account stats or place any orders. Trying to call any methods that require this to work will result in an error.

### Methods

_`dict`_ `client.`**`quote`**`(`_`symbol`_`)`

Returns a quote on the supplied symbol. 

**Parameters**

* **symbol** \(Required\[str\]\)  The symbol to get the quote of.

**Raises**

* **ApiError** - Raised when there is an error calling the API.



_`dict`_ `client.`**`search`**`(`_`symbol`_`)`

Search or retrieve instrument data. 

**Parameters**

* **symbol** \(Required\[str\]\)  An asset symbol.

**Raises**

* **ApiError** - Raised when there is an error calling the API.



_`dict`_ `client.`**`fundemental`**`(`_`symbol`_`)`

Returns fundamental data for the supplied symbol. 

**Parameters**

* **symbol** \(Required\[str\]\)  An asset symbol.

**Raises**

* **ApiError** - Raised when there is an error calling the API.



_`dict`_ `client.`**`account`**`()`

Returns Account balances.

**Raises**

* **ApiError** - Raised when there is an error calling the API.





_`dict`_ `client.`**`orders`**`()`

Returns all orders for your account.

**Raises**

* **ApiError** - Raised when there is an error calling the API.





_`dict`_ `client.`**`transactions`**`()`

Returns all transactions for your account.

**Raises**

* **ApiError** - Raised when there is an error calling the API.





_`dict`_ `client.`**`watchlists`**`()`

Returns all watch lists for your account.

**Raises**

* **ApiError** - Raised when there is an error calling the API.





_`dict`_ `client.`**`watchlist`**`(`_`watchlist_id`_`)`

Returns a specific watch list. 

**Parameters**

* **watchlist\_id** \(Required\[str\]\) The id of the watchlist you want to get.

**Raises**

* **ApiError** - Raised when there is an error calling the API.





_`dict`_ `client.`**`positions`**`()`

Returns all positions for your account.

**Raises**

* **ApiError** - Raised when there is an error calling the API.





_`dict`_ `client.`**`available_funds`**`()`

Returns the amount of available funds in your account.

**Raises**

* **ApiError** - Raised when there is an error calling the API.





_`dict`_ `client.`**`price_history`**`(`_`symbol, *, period_type='day', period=1, frequency_type='minute', frequency=1, start_date=None, end_date=None, need_extended_hours_data=False`_`)`

Returns price history for the specified symbol.

**Parameters**

* **symbol** \(Required\[str\]\)  An asset symbol.
* **period\_type** \(Optional\[str\]\)  The type of period to show. Valid values are `day`, `month`, `year`, or `ytd` \(year to date\).
* **period** \(Optional\[int\]\) The number of periods to show.
* **frequency\_type** \(Optional\[str\]\)  The type of frequency with which a new candle is formed. Valid frequency\_types by period\_type: `day`: minute `month`: daily, weekly `year`: daily, weekly, monthly `ytd`: daily, weekly
* **frequency** \(Optional\[int\]\)  The number of the frequency\_type to be included in each candle. Valid frequencies by frequency\_type: `minute`: 1, 5, 10, 15, 30 `daily`: 1 `weekly`: 1 `monthly`: 1
* **start\_date** \(Optional\[int\]\) Start date as milliseconds since epoch. If start\_date and end\_date are provided, period should not be provided.
* **end\_date** \(Optional\[int\]\) End date as milliseconds since epoch. If start\_date and end\_date are provided, period should not be provided. 
* **need\_extended\_hours\_data** \(Optional\[bool\]\) If true, extended hours data will be included.

**Raises**

* **ApiError** - Raised when there is an error calling the API.





_`void`_ `client.`**`buy_limit_equity`**`(`_`symbol, price, quanity`_`)`

Places a limit order to buy for the specified equity at the specified price for the specified quantity.

**Parameters**

* **symbol** \(Required\[str\]\) An asset symbol.
* **price** \(Required\[float\]\) The price that you want the limit order to be at.
* **quantity** \(Required\[int\]\) The amount of the asset that you want to buy.

**Raises**

* **ApiError** - Raised when there is an error calling the API.





_`void`_ `client.`**`sell_limit_equity`**`(`_`symbol, price, quanity`_`)`

Places a limit order to sell for the specified equity at the specified price for the specified quantity.

**Parameters**

* **symbol** \(Required\[str\]\) An asset symbol.
* **price** \(Required\[float\]\) The price that you want the limit order to be at.
* **quantity** \(Required\[int\]\) The amount of the asset that you want to sell.

**Raises**

* **ApiError** - Raised when there is an error calling the API.





_`void`_ `client.`**`place_custom_order`**`(`_`symbol, price, quanity`_`)`

Places a custom order. Check [here ](https://developer.tdameritrade.com/content/place-order-samples)for documentation on how to make custom orders.

**Parameters**

* **order**\(Required\[dict\]\) The order to place.

**Raises**

* **ApiError** - Raised when there is an error calling the API.

## Exceptions

### ApiError

_`exception`_ `td_ameritrade_api.`**`ApiError`**`(`_`APIPath, status, error`_`)`

* **APIPath**  The path to the address where the error occurred.
* **status** The HTTP request response code.
* **error** The error message, may be nil.

