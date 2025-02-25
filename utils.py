import matplotlib.pyplot as plt


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
