# TD Ameritrade API

## Setup instructions
Make sure you are using python 3.6 or greater, preferably python 3.7
I also highly recommend using `python-dotenv` to keep your api information safe.
To do this, create a .env file with the `REFRESH_TOKEN`, `CONSUMER_KEY`, and `ACCOUNT_ID` variables and install `python-dotenv`.

## How to use
```Python
from dotenv import load_dotenv
import td_ameritrade_api as td
from os import getenv

load_dotenv()
client = td.client(getenv("REFRESH_TOKEN"), getenv("CONSUMER_KEY"), getenv("ACCOUNT_ID"))

print(client.quote("AAPL"))
```
You can find all of the other functions in the `td_client.py` file.
There is no documentation yet, but it will be coming soon.
