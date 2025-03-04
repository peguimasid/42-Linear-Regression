from utils import (
    read_data,
    z_score,
    should_stop,
    plot_cost_history,
    plot_regression_line,
    print_state,
    store_thetas,
)

data = read_data("data.csv")

x = [row[0] for row in data]
y = [row[1] for row in data]

# Z-score standardization
x = z_score(x)
y = z_score(y)

# Start params
m = len(data)
intercept = 0
slope = 0
learning_rate = 0.01
iterations = 1000


def compute_cost(x, y, intercept, slope):
    predictions = [intercept + slope * val for val in x]
    errors = [(predicted - actual) ** 2 for predicted, actual in zip(predictions, y)]
    cost = (1 / (2 * m)) * sum(errors)
    return cost


def gradient_descent(x, y, intercept, slope):
    cost_history = []

    for i in range(iterations):
        # Compute predictions
        predictions = [intercept + slope * x_val for x_val in x]

        # Compute gradients
        intercept_errors = [
            predicted - actual for predicted, actual in zip(predictions, y)
        ]
        d_intercept = (1 / m) * sum(intercept_errors)

        slope_errors = [
            (predicted - actual) * x_val
            for predicted, actual, x_val in zip(predictions, y, x)
        ]
        d_slope = (1 / m) * sum(slope_errors)

        # Update parameters
        intercept -= learning_rate * d_intercept
        slope -= learning_rate * d_slope

        # Store the cost (optional, for monitoring)
        cost = compute_cost(x, y, intercept, slope)
        cost_history.append(cost)

        if should_stop(cost_history):
            break

        print_state(i, intercept, slope, cost)

    return intercept, slope, cost_history


intercept, slope, cost_history = gradient_descent(x, y, intercept, slope)

# Revert x and y to original scale
x = [row[0] for row in data]
y = [row[1] for row in data]

# Adjust intercept and slope to original scale
x_mean = sum(x) / len(x)
y_mean = sum(y) / len(y)
x_std = (sum([(xi - x_mean) ** 2 for xi in x]) / len(x)) ** 0.5
y_std = (sum([(yi - y_mean) ** 2 for yi in y]) / len(y)) ** 0.5

slope = slope * y_std / x_std
intercept = y_mean - slope * x_mean

plot_regression_line(x, y, intercept, slope)
plot_cost_history(cost_history)

store_thetas(intercept, slope)
