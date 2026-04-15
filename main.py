import pandas as pd
from src.data_loader import download_stock_data
from src.preprocessing import preprocess_data
from src.models import train_linear, train_rf, train_xgb
from src.evaluation import evaluate

df = download_stock_data("AAPL")
df = preprocess_data(df)

X = df[['Prev_Close', 'MA_5', 'MA_10']]
Y = df['Close']

split = int(len(df)* 0.8)
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

models = {
  "Linear" : train_linear(X_train, y_train),
  "RandomForest" : train_rf(X_train, y_train),
  "XGBoost" : train_xgb(X_train, y_train)
}

for name, model in models.items():
  preds = model.predict(X_test)
  metrics = evaluate(y_test, preds)
  print(f"{name}: {metrics}")
