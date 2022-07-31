from genericpath import exists
import json
import os.path


def write_json(data, filename):

    # Creating the file if it doen't exist
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            json.dump(None, f)
        print(filename, "created")

    with open(filename, "r") as f:
        old_data = json.load(f)

        if old_data != None:
            data = data + old_data

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def keys():
    # Getting the Private and Public Keys from user and write them into a file (Tokens.json)

    # Public Key:
    PB_K = input(
        "Paste Public Key found in the Marvel Site (https://developer.marvel.com/account):")

    # Private Key
    PR_K = input(
        "Paste your Private Key found in the Marvel Site (https://developer.marvel.com/account):")

    l = {"PB_K": PB_K, "PR_K": PR_K}

    with open("Tokens.json", "w") as f:
        json.dump(l, f, indent=2)
