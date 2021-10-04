import json
from fightController import fight


def start():
    playerNameInput = input("Enter a name for your character: ")

    playerData = open("playerVariables.json", "w")
    playerData.write("{\n"
                     "\"player\": ["
                     " {\n"
                     "\"playerName\": \"" + playerNameInput + "\",\n"
                                                              "\"playerMaxHealth\": 100\n"
                                                              "}\n"
                                                              "]\n"
                                                              "}")
    playerData = open("playerVariables.json", "r")
    jsonPlayerData = json.load(playerData)

    print("Your name is " + jsonPlayerData["player"][0]["playerName"])

    print("Starting fight test...")
    fight()
