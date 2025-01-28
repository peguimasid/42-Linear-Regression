import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('data.csv')

x = data.iloc[:, 0]
y = data.iloc[:, 1]

# Perform linear regression using numpy.polyfit
coefficients = np.polyfit(x, y, 1)
slope, intercept = coefficients

# Generate the regression line
regression_line = slope * x + intercept

plt.scatter(x, y, label='Data points')
plt.plot(x, regression_line, color='red', label='Regression line')
plt.xlabel('mileage')
plt.ylabel('price')
plt.legend()

plt.show()
