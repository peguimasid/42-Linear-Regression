from utils import z_score, read_data

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
    return intercept, slope, cost_history


intercept, slope, cost_history = gradient_descent(x, y, intercept, slope)

print(intercept, slope)
