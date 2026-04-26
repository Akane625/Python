import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
from datetime import datetime, timedelta


def make_csv():
  start = datetime(2000, 1, 1)
  data = {"Date": [start + timedelta(days=i) for i in range(100)], "Temperature (°C)": [random.randint(20, 40) for i in range(100)]}
  df = pd.DataFrame(data)
  df.to_csv('temperature.csv', index=False)


make_csv()
df = pd.read_csv('temperature.csv')
df['7-Day Rolling Average'] = df['Temperature (°C)'].rolling(window=7).mean()

plt.figure(figsize=(20, 10))
plt.plot(df['Date'], df['Temperature (°C)'], label='Daily Temperature', color='blue', linewidth=2)
plt.plot(df['Date'], df['7-Day Rolling Average'], label = '7-Day Moving Average', color='red', linewidth=2)

plt.title("Temperature vs. 7-Day Rolling Average")
plt.xlabel("Date")
plt.xticks(df['Date'][::20])
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
