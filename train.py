import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("data.csv")

x = data.iloc[:, 0]
y = data.iloc[:, 1]

# Normalize the data
# x = (x - x.mean()) / x.std()
# y = (y - y.mean()) / x.std()
x = (x - x.min()) / (x.max() - x.min())
y = (y - y.min()) / (y.max() - y.min())

intercept = 0  # 1
slope = 0  # -1.2

learning_rate = 0.01
iterations = 5000


def compute_cost(x, y, intercept, slope):
    m = len(y)
    predictions = intercept + slope * x
    cost = (1 / (2 * m)) * sum((predictions - y) ** 2)
    return cost


def gradient_descent(x, y, intercept, slope):
    m = len(y)
    for _ in range(iterations):
        predictions = intercept + slope * x
        d_intercept = (1 / m) * sum(predictions - y)
        d_slope = (1 / m) * sum((predictions - y) * x)
        intercept = intercept - learning_rate * d_intercept
        slope = slope - learning_rate * d_slope
    return intercept, slope


intercept, slope = gradient_descent(x, y, intercept, slope)

line_x = np.linspace(x.min(), x.max(), 100)
line_y = intercept + slope * line_x

plt.plot(line_x, line_y, color="red", label="Regression Line")
plt.scatter(x, y, label="Data points")
plt.xlabel("mileage")
plt.ylabel("price")
plt.legend()
plt.show()
