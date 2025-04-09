import os

import yfinance as yf
from influxdb_client.client.influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
from pytz.exceptions import Error
from utils.helpers import convert_to_df, convert_to_points

tickers = os.environ.get("TICKERS", "")
token = os.environ.get("INFLUX_DB_TOKEN", "")
org = os.environ.get("INFLUX_DB_ORG", "")
bucket = os.environ.get("INFLUX_DB_BUCKET", "")
url = os.environ.get("INFLUX_DB_URL", "")

if "" in [tickers, token, org, bucket, url]:
    raise Error("Missing environment variables")


client = InfluxDBClient(url=url, token=token, org=org, debug=False)
write_api = client.write_api(write_options=SYNCHRONOUS)


def main():
    for ticker in tickers.split(","):
        df = yf.download(
            tickers=ticker,
            interval="1m",
        )

        if df is None:
            continue

        df = convert_to_df(ticker=ticker, _df=df)
        print(df.head())

        points = convert_to_points(ticker=ticker, df=df)
        write_api.write(bucket=bucket, org=org, record=points)

    print("Done")
    exit(0)


main()
