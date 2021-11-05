import item


def town(player_data):
    print("\n\nWelcome to Town!\n")

    def shop():

        print("\nHey there adventurer! What can i get you?")

        # starter kit choices
        # get first item in bag(which should be voucher) and get its name from item method
        if player_data.get_bag(0).name() == "Starter Kit Voucher":
            player_data.remove_bag(0)
            choice = input(
                "\nAh. i see you have a starter kit voucher from the adventurer guild. \nWhat weapon "
                "would you like to exchange it for?\n[Wooden Sword][Bow][Spell Book]\n")
            if choice.lower() == "wooden sword":
                player_data.set_bag(item.get_item_by_id("W00001"), 0)
                print("\nYou obtained a Wooden Sword")
            if choice.lower() == "bow":
                player_data.set_bag(item.get_item_by_id("W00002"), 0)
                print("\nYou obtained a Bow")
            if choice.lower() == "spell book":
                player_data.set_bag(item.get_item_by_id("W00003"), 0)
                print("\nYou obtained a Weak Spell Book")
        print("Sorry man, im not selling anything at the moment. Be sure to come back when i am!")
        cont = input("[ > ]")
        town(player_data)

    choice = input("Where do you want to go?\n[Shop][Leave]\n")
    if choice.lower() == "shop":
        shop()
    elif choice.lower() == "leave":
        choice = input("Are you sure you want to leave town? [Y/n]")
        if choice == "n":
            town(player_data)
        print("You Leave the town\nOff to adventure!")
