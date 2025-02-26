import json


def read_thetas():
    with open("thetas.json") as f:
        data = json.load(f)
        return data["intercept"], data["slope"]


intercept, slope = read_thetas()

print(intercept, slope)
