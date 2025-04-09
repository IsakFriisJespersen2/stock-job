from typing import List
from influxdb_client.domain.write_precision import  WritePrecision
from influxdb_client.client.write.point import Point
import pandas as pd
from pandas.core.api import DataFrame


def convert_to_df(ticker: str, _df: DataFrame) -> DataFrame:
    _df.reset_index(drop=False, inplace=True)
    if isinstance(_df.columns, pd.MultiIndex):
        _df.columns = _df.columns.droplevel(1)
    _df["ticker"] = ticker

    df = pd.DataFrame()
    if "Datetime" in _df:
        df["Date"] = pd.to_datetime(_df["Datetime"])
    if "Date" in _df:
        df["Date"] = pd.to_datetime(_df["Date"])

    df["open"] = _df["Open"]
    df["high"] = _df["High"]
    df["low"] = _df["Low"]
    df["close"] = _df["Close"]
    df["adjclose"] = _df["Close"]
    df["volume"] = _df["Volume"]
    df["ticker"] = _df["ticker"]

    return df

def convert_to_points(ticker, df: DataFrame) -> List[Point]:
    points = []
    for _, row in df.iterrows():
        point = (
            Point(f"{ticker}")
            .field("close", row["close"])
            .field("high", row["high"])
            .field("low", row["low"])
            .field("open", row["open"])
            .field("volume", row["volume"])
            .time(row["Date"], WritePrecision.S)
        )
        points.append(point)

    return points
