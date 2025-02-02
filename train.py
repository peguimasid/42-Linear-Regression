import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("data.csv")

x = data.iloc[:, 0]
y = data.iloc[:, 1]

# Normalize the data
x = (x - x.min()) / (x.max() - x.min())
y = (y - y.min()) / (y.max() - y.min())

intercept = 0
slope = 0


def compute_cost(x, y, theta0, theta1):
    m = len(y)
    predictions = theta0 + theta1 * x
    cost = (1 / (2 * m)) * sum((predictions - y) ** 2)
    return cost


print(compute_cost(x, y, intercept, slope))

line_x = np.linspace(x.min(), x.max(), 100)
line_y = intercept + slope * line_x

plt.plot(line_x, line_y, color="red", label="Regression Line")
plt.scatter(x, y, label="Data points")
plt.xlabel("mileage")
plt.ylabel("price")
plt.legend()
plt.show()
