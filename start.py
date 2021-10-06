import json
from town import town


def start():
    print("Welcome to the adventuring guild! Please register with the guild")

    playerNameInput = input("Enter a name for your character: ")

    # create and overwrite player variables
    playerData = open("playerVariables.json", "w")
    playerData.write("{\"player\": [ {\"playerName\": \"" + playerNameInput + "\",\"playerMaxHealth\": 100, "                                                                             "\"strength\": 5, \"stamina\": 5, "                                                                              "\"magic\": 5}]}")
    playerData = open("playerVariables.json", "r")
    jsonPlayerData = json.load(playerData)

    playerName = jsonPlayerData["player"][0]["playerName"]
    print("Your name is " + playerName)

    print("Looks like your all set! Dont forget to pick up your adventurer starter set at the shop.\nYou received a "
          "starter set voucher.")
    town()
# adventure hall where you register to be a adventure and go on your first quest
