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
intercept = 0
slope = 0

learning_rate = 0.01
iterations = 1000
