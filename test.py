import json

i = {"Name": "???", "Gender": "???", "Money": 0, "Pokemons": {}, "Inventory": {}, "Location": "view"}

with open("saves\journey_1.json", "w") as f:
    json.dump(i, f, indent=4)