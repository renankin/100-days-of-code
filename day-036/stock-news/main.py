import requests
import os
from datetime import datetime, timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": os.environ.get("AV_API_KEY")
}

response = requests.get(url="https://www.alphavantage.co/query",
                        params=parameters)
response.raise_for_status()
stock_data = response.json()

today = datetime.now().strftime('%Y-%m-%d')
# last_refreshed = stock_data["Meta Data"]["3. Last Refreshed"]
# if last_refreshed != today:
#     yesterday_data = stock_data["Time Series (Daily)"].keys()[0]
#     day_before_yesterday_data =
#     print(yesterday_data, day_before_yesterday_data)

