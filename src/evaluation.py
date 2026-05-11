from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def evaluate(y_true, y_pred):
  mse = mean_squared_error(y_true, y_pred)
  rmse = np.sqrt(mse)
  mae = mean_absolute_error(y_true, y_pred)
  return {
    "MSE": mse,
    "RMSE": rmse,
    "MAE": mae
  }

def plot_actual_vs_predicted(y_true, y_pred, model_name, output_path=None, show=False):
  dates = y_true.index
  actual = np.asarray(y_true).ravel()
  predicted = np.asarray(y_pred).ravel()

  plt.figure(figsize=(12, 6))
  plt.plot(dates, actual, label="Actual Close Price", linewidth=2)
  plt.plot(dates, predicted, label=f"{model_name} Predicted Close Price", linewidth=2)
  plt.title(f"Actual vs Predicted Stock Prices - {model_name}")
  plt.xlabel("Date")
  plt.ylabel("Close Price")
  plt.legend()
  plt.grid(True, alpha=0.3)
  plt.tight_layout()

  if output_path:
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=300)

  if show:
    plt.show()
  else:
    plt.close()
