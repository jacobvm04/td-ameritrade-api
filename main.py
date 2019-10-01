from dotenv import load_dotenv
import td_ameritrade_api as td
from os import getenv

load_dotenv()
client = td.client(getenv("REFRESH_TOKEN"), getenv("CONSUMER_KEY"), getenv("ACCOUNT_ID"))

print(client.quote("AAPL"))
