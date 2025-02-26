import json


def read_thetas():
    try:
        with open("thetas.json") as f:
            data = json.load(f)
            return data["intercept"], data["slope"]
    except (FileNotFoundError, KeyError, json.JSONDecodeError):
        return 0, 0


intercept, slope = read_thetas()

print(intercept, slope)
