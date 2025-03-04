import pandas as pd
from utils import (
    plot_cost_history,
    plot_regression_line,
    print_state,
    should_stop,
    store_thetas,
)

data = pd.read_csv("data.csv")

x = data.iloc[:, 0]
y = data.iloc[:, 1]

# Z-score standardization
x = (x - x.mean()) / x.std()
y = (y - y.mean()) / y.std()

# Start params
m = len(data)
intercept = 0
slope = 0
learning_rate = 0.01
iterations = 1000


def compute_cost(x, y, intercept, slope):
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

        # Update parameters
        intercept -= learning_rate * d_intercept
        slope -= learning_rate * d_slope

        # Store the cost (optional, for monitoring)
        cost = compute_cost(x, y, intercept, slope)
        cost_history.append(cost)

        if should_stop(cost_history):
            break

        # Print the current state
        print_state(i, intercept, slope, cost)

    return intercept, slope, cost_history


intercept, slope, cost_history = gradient_descent(x, y, intercept, slope)

# Revert x and y to original scale
x = data.iloc[:, 0]
y = data.iloc[:, 1]

# Adjust intercept and slope to original scale
slope = slope * y.std() / x.std()
intercept = y.mean() - slope * x.mean()

plot_regression_line(x, y, intercept, slope)
plot_cost_history(cost_history)

store_thetas(intercept, slope)
