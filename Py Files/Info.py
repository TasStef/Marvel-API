import os
from marvel import Marvel
import json
import Methods


def main():

    # Getting the Private and Public  Keys from Tokens.json
    with open("Tokens.json", "r") as f:
        data = json.load(f)

        PB_K = data["PB_K"]
        PR_K = data["PR_K"]

    filename = "Characters_Info.json"
    marvel = Marvel(PUBLIC_KEY=PB_K, PRIVATE_KEY=PR_K)

    charactersId = marvel.characters

    # Getting the ids from file
    with open("Characters_ID.json", "r") as f:
        ids = json.load(f)

    # For all the ids on file, get the data for characters from API, using characters/characterId
    # and write them in a json file Characters_Info.json
    for id in ids:
        data = charactersId.get(id)

        dict = data["data"]["results"][0]

        # Delete all unneccesary data
        del dict["resourceURI"]
        del dict["comics"]
        del dict["series"]
        del dict["stories"]
        del dict["events"]
        del dict["urls"]

        l = [dict]
        Methods.write_json(l, filename)

    # Deleting Tokens.json
    os.remove("Tokens.json")
