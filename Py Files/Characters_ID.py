from textwrap import indent
import json


def main():
    filename = "All_Characters.json"

    # read data from json file
    with open(filename, "r") as f:
        data = json.load(f)

    # Initialize the list
    list = []

    # For each character in the All_Characters.json get the IDs and put them on the list
    for i in range(len(data)):
        list.append(data[i]["id"])

    # Writing data to a json file
    with open("Characters_ID.json", "w") as f:
        json.dump(list, f)
