import item


def town(player_data):
    print("\n\nWelcome to Town!\n")

    def shop():

        print("\nHey there adventurer! What can I get you?")

        # starter kit choices
        # get first item in bag(which should be voucher) and get its name from item method
        if player_data.get_bag(0).name() == "Starter Kit Voucher":
            player_data.remove_bag(0)
            choice = input(
                "\nAh, I see you have a starter kit voucher from the adventurer guild. \nWhat weapon "
                "would you like to exchange it for?\n[Wooden Sword]\n[Bow]\n[Spell Book]\n")
            if choice.lower() == "wooden sword":
                player_data.set_bag(item.get_item_by_id("W00001"), 0)
                print("\n[You obtained \"WOODEN SWORD\"!]")
            if choice.lower() == "bow":
                player_data.set_bag(item.get_item_by_id("W00002"), 0)
                print("\n[You obtained \"BOW\"!]")
            if choice.lower() == "spell book":
                player_data.set_bag(item.get_item_by_id("W00003"), 0)
                print("\n[You obtained \"WEAK SPELL BOOK\"!]")
        print("Sorry man, I'm not selling anything at the moment. Be sure to come back when I am!")
        cont = input("...")
        town(player_data)

    choice = input("Where do you want to go?\n[Shop]\n[Leave]\n")
    if choice.lower() == "shop":
        shop()
    elif choice.lower() == "leave":
        choice = input("Are you sure you want to leave town? [Y/n]")
        if choice == "n":
            town(player_data)
        print("You Leave the town\nOff to adventure!")
        cont = input("...")