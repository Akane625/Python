import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random


def create_csv():
  products = ["Chicken", "Sandwich", "Salad", "Coffee", "Beef", "Pork", "Rice", "Soda"]
  data = {"Products": [random.choice(products) for i in range(1000)], "Sales": [random.randint(1, 100) for i in range(1000)]}
  df = pd.DataFrame(data)
  df.to_csv("sales.csv", index=False)


def pandas_bar():
  top5.plot(kind='bar')
  plt.title("Top 5 Product Sales")
  plt.xlabel("Products")
  plt.ylabel("Sales")
  plt.xticks(rotation=0)
  plt.tight_layout()
  plt.show()


def matplot_bar():
  plt.bar(top5.index, top5.values)
  plt.title("Top 5 Product Sales")
  plt.xlabel("Products")
  plt.ylabel("Sales")
  plt.xticks(rotation=0)
  plt.tight_layout()
  plt.show()


create_csv()

df = pd.read_csv('sales.csv')
filter = df.groupby('Products')["Sales"].sum().sort_values(ascending=False)
top5 = filter.head(5)
print(top5)

pandas_bar()
matplot_bar()
