import requests
import os
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
TWILIO_SID = "ACc92ab8dfc63f45ef93a25ab718b0e213"
TWILIO_TOKEN = os.environ.get("AUTH_TOKEN")


stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": os.environ.get("AV_API_KEY")
}
response = requests.get(url=STOCK_ENDPOINT,
                        params=stock_params)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]

data_list = [value for (key, value) in stock_data.items()]
yesterday_price = float(data_list[0]["4. close"])
previous_day_price = float(data_list[1]["4. close"])
diff_percent = (round(100 * (yesterday_price - previous_day_price) /
                yesterday_price))

if abs(diff_percent) > 2:
    news_params = {
        "apiKey": os.environ.get("NEWS_API_KEY"),
        "qInTitle": COMPANY_NAME,
        "pagesize": 3,
        "language": "en",
    }
    response = requests.get(url=NEWS_ENDPOINT,
                            params=news_params)
    response.raise_for_status()
    articles = response.json()["articles"]

    if diff_percent > 0:
        up_down = "🔺"
    else:
        up_down = "🔻"

    formatted_articles = [
        f"{STOCK}: {up_down}{diff_percent}%\n"
        f"Headline: {article['title']}\nBrief: {article['description']}"
        for article in articles
    ]

    client = Client(TWILIO_SID, TWILIO_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+12622057162",
            to="+447985503160",
        )
        print(message.status)
