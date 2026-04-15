from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor

def train_linear(X_train, y_train):
  model = LinearRegression()
  model.fit(X_train, y_train)
  return model

def train_rf(X_train, y_train):
  model = RandomForestRegressor(n_estimators = 100)
  model.fit(X_train, y_train)
  return model

def train_xgb(X_train, y_train):
  mdoel = XGBRegressor()
  model.fit(X_train, y_train)
  return model
  
