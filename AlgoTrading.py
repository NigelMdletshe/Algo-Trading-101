#1 Data Scraping
#2 Backtesting
#3 Execution Code
#4 Deploy bot to cloud
#5 Trade Analysis

#Scrap data from Bitstamp

import json
import pandas as pd
import requests
import datetime

currency_pair = "btcusd"
url = f"https://www.bitstamp.net/api/v2/ohlc/{currency_pair}/"

start = "2020-01-01"
end   = "2023-05-08"

dates = pd.date_range(start,end, freq= "1H")
dates = [ int(x.value/10**9) for x in list (dates)]
#print(dates)

for first, last in zip(dates,dates[1:]):
    params = {
        "step":60,
        "limit":1000,
    }

    data = requests.get(url,params=params)
    data = data.json()["data"]["ohlc"]
    df = pd.DataFrame(data)
    print(df)