import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("data.csv")

x = data.iloc[:, 0]
y = data.iloc[:, 1]

# Normalize the data
x = (x - x.min()) / (x.max() - x.min())
y = (y - y.min()) / (y.max() - y.min())

plt.scatter(x, y, label="Data points")
plt.xlabel("mileage")
plt.ylabel("price")
plt.legend()

plt.show()
