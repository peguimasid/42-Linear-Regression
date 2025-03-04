import matplotlib.pyplot as plt
import json
import csv


def print_state(iteration, intercept, slope, cost):
    print(
        f"Iteration {iteration:03d}: Intercept = {intercept:.19f}, Slope = {slope:.19f}, Cost = {cost:5f}"
    )


def plot_cost_history(cost_history):
    plt.plot(cost_history)
    plt.xlabel("Iterations")
    plt.ylabel("Cost")
    plt.title("Cost Function Convergence")
    plt.show()


def plot_regression_line(x, y, intercept, slope):
    plt.scatter(x, y)
    plt.plot(x, intercept + slope * x, color="red")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f"Linear Regression (intercept: {intercept:.2f}, slope: {slope:.2f})")
    plt.show()


def plot_point_on_regression_line(x, y, intercept, slope, mileage, price):
    plt.scatter(x, y)
    plt.plot(x, intercept + slope * x, color="red")
    plt.scatter(mileage, price, color="lime", zorder=5)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(
        f"Linear Regression with Point (mileage: {mileage:.2f}, price: {price:.2f})"
    )
    plt.show()


def should_stop(cost_history):
    """
    Check if the cost has converged
    """
    if len(cost_history) < 2:
        return False
    return round(cost_history[-2], 7) == round(cost_history[-1], 7)


def store_thetas(intercept, slope):
    thetas = {"intercept": intercept, "slope": slope}

    with open("thetas.json", "w") as f:
        json.dump(thetas, f)


# Scratch
def z_score(values):
    mean = sum(values) / len(values)
    std_dev = (sum((x - mean) ** 2 for x in values) / len(values)) ** 0.5
    return [(x - mean) / std_dev for x in values]


def read_data(file):
    try:
        with open(file, mode="r", newline="") as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)  # Skip the header
            return [[float(element) for element in row] for row in csvreader]
    except (FileNotFoundError, ValueError) as e:
        print(f"Error during data reading: {e}")
        raise
