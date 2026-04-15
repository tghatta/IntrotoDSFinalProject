import pandas as pd

def preprocess_data(df):
  df = df.copy()
  df = df.dropna()
  df.index = pd.to_datatime(df.index)
  df['Prev_Close'] = df['Close'].shift(1)
  df['MA_5'] = df['Close'].rolling(window=5).mean()
  df['MA_10'] = df['Close'].rolling(window=10).mean()
