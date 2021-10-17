import json
import time

def town():
    print("\n\nWelcome to Town!\n")

    playerFile = open('json/playerVariables.json', )
    player = json.loads(playerFile.read())
    itemFile = open('json/items.json', )
    items = json.loads(itemFile.read())
    playerFile.close()
    itemFile.close()

    def shop():
        playerFile = open('json/playerVariables.json', "w")
        itemFile = open('json/items.json', "w")

        print("\nHey there adventurer! What can i get you?")
        # starter kit choices
        if player["playerItems"][0]["itemName"] == "Starter Kit Voucher":
            choice = input(
                "\nAh. i see you have a starter kit voucher from the adventurer guild. \nWhat weapon "
                "would you like to exchange it for?\n[Wooden Sword][Bow][Spell Book]\n")
            if choice.lower() == "wooden sword":
                player["playerItems"][0] = items["items"][1]
                print("\nYou obtained a Wooden Sword")
            if choice.lower() == "bow":
                player["playerItems"][0] = items["items"][2]
                print("\nYou obtained a Bow")
            if choice.lower() == "spell book":
                player["playerItems"][0] = items["items"][3]
                print("\nYou obtained a Weak Spell Book")
        print("Sorry man, im not selling anything at the moment. Be sure to come back when i am!")
        cont = input("[ > ]")
        time.sleep(1)

        playerFile.write(json.dumps(player))
        itemFile.write(json.dumps(items))
        playerFile.close()
        itemFile.close()
        town()

    # TODO: Add adventure hall to check stats and receive and turn in quests

    choice = input("Where do you want to go?\n[Shop][Leave]\n")
    if choice.lower() == "shop":
        shop()
    elif choice.lower() == "leave":
        choice = input("Are you sure you want to leave town? [Y/n]")
        if choice == "n":
            town()
        # leave()
