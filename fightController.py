import json
import random

# Enemy Data
enemyFile = open("enemies.json", "r")
enemy = json.loads(enemyFile.read())
enemyName = enemy["enemy"][0]["enemyName"]
enemyHealth = enemy["enemy"][0]["enemyMaxHealth"]


def fight():
    print("\nYou Encountered a " + enemyName)
    action = input("Type an Action\n"
                   # Pick a action if i can figure it out later
                   "Fight, Bag, Run\n")
    # actions!
    if action.lower() == "fight":
        print("You hit the " + enemyName + " for 2 damage.")
