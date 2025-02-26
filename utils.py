import matplotlib.pyplot as plt
import json


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
