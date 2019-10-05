# API Reference

## Client

_`class`_ `td_ameritrade_api.`**`client`**`(`_`refresh_token, consumer_key, account_id`_`)`

### Parameters

* **refresh\_token** \(Required\[str\]\) The oauth2 refresh token from the TD Ameritrade API used to obtain the access token to use the API.
* **consumer\_key** \(Required\[str\]\) The API consumer key from when you create an app on TD's developer website.
* **account\_id** \(Optional\[str\]\) Your account id which is needed to view account stats or place any orders. Trying to call any methods that require this to work will result in an error.

### Methods

_`dict`_ `client.`**`quote`**`(`_`symbol`_`)`

Returns a quote on the supplied symbol.
**Parameters**

* **symbol** \(Required\[str\]\) The symbol to get the quote of.

**Raises**

* **ApiError** - Raised when there is an error calling the API.

_`dict`_ `client.`**`search`**`(`_`symbol`_`)`

Search or retrieve instrument data.
**Parameters**

* **symbol** \(Required\[str\]\) An asset symbol.

**Raises**

* **ApiError** - Raised when there is an error calling the API.

_`dict`_ `client.`**`fundemental`**`(`_`symbol`_`)`

Returns fundamental data for the supplied symbol.
**Parameters**

* **symbol** \(Required\[str\]\) An asset symbol.

**Raises**

* **ApiError** - Raised when there is an error calling the API.

_`dict`_ `client.`**`account`**`()`

Returns Account balances.

**Raises**

* **ApiError** - Raised when there is an error calling the API.

## Exceptions

### ApiError

_`exception`_ `td_ameritrade_api.`**`ApiError`**`(`_`APIPath, status, error`_`)`

* **APIPath**  The path to the address where the error occurred.
* **status** The HTTP request response code.
* **error** The error message, may be nil.

