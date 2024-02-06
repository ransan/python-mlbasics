import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Date": pd.date_range(start="2021-10-01", periods=10),
    "Measurement": [16, 13, 14, 12, np.nan, np.nan, np.nan, 8, 7, 5]
})

df["Measurement"].fillna(method="ffill", limit=2, inplace=True)
df["Measurement"].fillna(value=df["Measurement"].mean(), inplace=True)
print(list(df["Measurement"]))