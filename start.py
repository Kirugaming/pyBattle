import json
from fightController import fight


def start():
    playerNameInput = input("Enter a name for your character: ")

    playerData = open("playerVariables.json", "w")
    playerData.write("{\"player\": [ {\"playerName\": \"" + playerNameInput + "\",\"playerMaxHealth\": 100}]}")
    playerData = open("playerVariables.json", "r")
    jsonPlayerData = json.load(playerData)

    print("Your name is " + jsonPlayerData["player"][0]["playerName"])

    print("Starting fight test...")
    fight()
# add story to start later
