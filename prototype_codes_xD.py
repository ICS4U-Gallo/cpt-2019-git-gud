import os
import json

#dw just some testing1

info = {"Player": 0}


if len(os.listdir("saves")) == 0:
    info = {"Player": 0}
    # with open(f"saves/save0.json", "w") as f:
    #     json.dump(info, f)
else:
    with open(".json", "r") as f:
        info = json.load(f)

def battle(player, opponent):
    pass