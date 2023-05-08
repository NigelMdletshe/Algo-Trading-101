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



# Set the currency pair and API endpoint
currency_pair = "btcusd"
url = f"https://www.bitstamp.net/api/v2/ohlc/{currency_pair}/"

# Define the date range
start = "2020-01-01"
end = "2023-05-08"

# Generate a list of hourly timestamps within the date range
dates = pd.date_range(start, end, freq="1H").tolist()
timestamps = [int(date.timestamp()) for date in dates]

# Fetch data for each timestamp interval
master_data = []

for i in range(len(timestamps) - 1):
    first = timestamps[i]
    last = timestamps[i + 1]

    params = {
        "step": 60,
        "limit": 1000,
        "start": first,
        "end": last,
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()["data"]["ohlc"]
        master_data += data

# Create a DataFrame from the collected data
df = pd.DataFrame(master_data)

# Clean and filter the DataFrame
df = df.drop_duplicates()
df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")
df = df.sort_values(by="timestamp")
df = df[(df["timestamp"] >= start) & (df["timestamp"] <= end)]

# Save the DataFrame to a CSV file
df.to_csv("bitcoinData.csv", index=False)

# Print the resulting DataFrame
print(df)
# This code takes a long time to print and ssave data, not sure what is the error, l am suspecting the network

