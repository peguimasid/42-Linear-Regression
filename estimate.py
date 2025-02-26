import json
from utils import plot_point_on_regression_line
import pandas as pd

data = pd.read_csv("data.csv")

x = data.iloc[:, 0]
y = data.iloc[:, 1]


def read_thetas():
    try:
        with open("thetas.json") as f:
            data = json.load(f)
            return data["intercept"], data["slope"]
    except (FileNotFoundError, KeyError, json.JSONDecodeError):
        return 0, 0


def main():
    try:
        mileage = float(input("Enter mileage: "))
        intercept, slope = read_thetas()
        price = intercept + (slope * mileage)
        print("Estimated price: ", price)
        plot_point_on_regression_line(x, y, intercept, slope, mileage, price)
    except ValueError:
        print("Invalid input. Please enter a numeric value for mileage.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
