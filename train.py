import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("data.csv")
m = len(data)

x = data.iloc[:, 0]
y = data.iloc[:, 1]

# Normalize the data
x = (x - x.mean()) / x.std()
y = (y - y.mean()) / y.std()

# Start params
intercept = 2
slope = 10
learning_rate = 0.01
iterations = 1000


def compute_cost(x, y, intercept, slope):
    m = len(y)
    predictions = intercept + slope * x
    cost = (1 / (2 * m)) * sum((predictions - y) ** 2)
    return cost


def gradient_descent(x, y, intercept, slope):
    cost_history = []  # Store cost at each iteration

    for i in range(iterations):
        # Compute predictions
        predictions = intercept + slope * x

        # Compute gradients (derivatives)
        d_intercept = (1 / m) * sum(predictions - y)
        d_slope = (1 / m) * sum((predictions - y) * x)

        if i % 20 == 0:
            show_regression_line(x, y, intercept, slope)

        # Update parameters
        intercept -= learning_rate * d_intercept
        slope -= learning_rate * d_slope

        # Store the cost (optional, for monitoring)
        cost = compute_cost(x, y, intercept, slope)
        cost_history.append(cost)

    return intercept, slope, cost_history


def show_cost_history(cost_history):
    plt.plot(cost_history)
    plt.xlabel("Iterations")
    plt.ylabel("Cost")
    plt.title("Cost Function Convergence")
    plt.show()


def show_regression_line(x, y, intercept, slope):
    plt.scatter(x, y)
    plt.plot(x, intercept + slope * x, color="red")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f"Linear Regression (intercept: {intercept:.2f}, slope: {slope:.2f})")
    plt.show()


intercept, slope, cost_history = gradient_descent(x, y, intercept, slope)

print(intercept, slope)

# show_regression_line(x, y, intercept, slope)
