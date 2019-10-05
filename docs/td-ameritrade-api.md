# Getting Started

## Getting your API information

{% embed url="https://developer.tdameritrade.com/content/getting-started" caption="This is a good guide on how to get your API information" %}

## Storing your API information

Make sure you are using python 3.6 or greater. We also highly recommend using `python-dotenv` to keep your to store your API information. To do this, create a .env file with the `REFRESH_TOKEN`, `CONSUMER_KEY`, and `ACCOUNT_ID` variables and.

```text
REFRESH_TOEKN=""
CONSUMER_KEY=""
ACCOUNT_ID=""
```

Then you can install python-dotenv with 

```text
$ python3.7 -m install python-dotenv
```

## Basic setup

First install the python package

```text
$ python3.7 -m install td-ameritrade-api
```

Then you have to initialize a client object with your refresh token, API consumer key, and your account id. Then you can access all of the APIs functions.

```python
from dotenv import load_dotenv
import td_ameritrade_api as td
from os import getenv

load_dotenv()
client = td.client(getenv("REFRESH_TOKEN"), getenv("CONSUMER_KEY"), getenv("ACCOUNT_ID"))

print(client.quote("AAPL"))
```



