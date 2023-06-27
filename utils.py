import json


def get_data(file):
    with open("file", "r") as file:
        data = json.load(file)

    return data

print (get_data("operations.json")
