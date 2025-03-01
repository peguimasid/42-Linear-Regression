import csv


def z_score(values):
    mean = sum(values) / len(values)
    std_dev = (sum((x - mean) ** 2 for x in values) / len(values)) ** 0.5
    return [(x - mean) / std_dev for x in values]


def read_data(file):
    """Reads the values from a CSV file and returns a list of data values.

    Args:
      file (str): The path to the CSV file.

    Returns:
      list: A list of data values.
    """
    try:
        with open(file, mode="r", newline="") as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)  # Skip the header
            return [[float(element) for element in row] for row in csvreader]
    except (FileNotFoundError, ValueError) as e:
        print(f"Error during data reading: {e}")
        raise
