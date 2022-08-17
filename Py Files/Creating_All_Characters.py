from textwrap import indent
from marvel import Marvel
import Methods
import json


def main():

    # Getting the Private and Public Keys from user and write them into a file
    Methods.keys()

    # Getting the Private and Public  Keys from Tokens.json
    with open("Tokens.json", "r") as f:
        data = json.load(f)

        PB_K = data["PB_K"]
        PR_K = data["PR_K"]

    # Setting the API object
    marvel = Marvel(PUBLIC_KEY=PB_K, PRIVATE_KEY=PR_K)
    characters = marvel.characters

    # Scan all characters using offset until the "results" within "data" is empty
    count = 0
    char = characters.all(offset=count)
    file_name = "All_Characters.json"

    while char["data"]["results"] != []:

        Methods.write_json(char["data"]["results"], file_name)

        # adjust for quick check-ups (default=20)
        count += 20
        char = characters.all(offset=count)
