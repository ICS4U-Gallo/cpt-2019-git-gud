import os
import json

#dw just some testing

info = {"Player": 0}


if len(os.listdir("saves")) == 0:
    with open(f"saves/save0.json", "w") as f:
        json.dump(info, f)


def battle(player, opponent):
    pass