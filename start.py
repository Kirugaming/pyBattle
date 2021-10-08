import json
import time
from town import town


def start():
    print("Welcome to the adventuring guild! Please register with the guild.")

    playerNameInput = input("Enter a name for your character: ")

    templatePlayerData = '{"playerData": [ { "playerName": "' + playerNameInput + '", "playerMaxHealth": 100, ' \
                                                                                  '"strength": 5, "stamina": 5, ' \
                                                                                  '"magic": 5 } ], "playerItems": [ { ' \
                                                                                  '"itemName": "" }, { "itemName": "" ' \
                                                                                  '}, { "itemName": "" }, ' \
                                                                                  '{ "itemName": "" }, { "itemName": ' \
                                                                                  '"" }, { "itemName": "" }, ' \
                                                                                  '{ "itemName": "" }, { "itemName": ' \
                                                                                  '"" }, { "itemName": "" } ] } '

    player = json.loads(templatePlayerData)

    player["playerItems"][0]["itemName"] = "Starter Kit Voucher"

    playerFile = open("playerVariables.json", "w")
    playerFile.write(json.dumps(player))
    # playerData = open("playerVariables.json", "r")
    # jsonPlayerData = json.load(playerData)

    time.sleep(1)

    print("\nYour name is " + playerNameInput + "\nYour stats are " + str(
        player["playerData"][0]["strength"]) + " strength, " + str(
        player["playerData"][0]["stamina"]) + " stamina, and " + str(player["playerData"][0]["magic"]) + " magic.")

    time.sleep(2)

    print("\nLooks like your all set! Dont forget to pick up your adventurer starter set at the shop.\nYou received a "
          "starter set voucher!")
    # town()
# adventure hall where you register to be a adventure and go on your first quest
