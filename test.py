import json

i = {"Name": "???", "Gender": "Male"}

with open("saves\journey_1.json", "w") as f:
    json.dump(i, f, indent=4)