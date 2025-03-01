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
