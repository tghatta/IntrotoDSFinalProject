import yfinance as yf
import pandas as pd

def download_stock_data(ticker = "AAPL", start = "2015-01-01", end = "2014-01-01"):
  data = yf.download(ticker, start= start, end = end)
  return data

if _name_ == "__main__":
  df = download_stock_data()
  df.to_csv("data/raw/aaple.csv")
