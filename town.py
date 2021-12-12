import bag
import item
import player
from fightController import controller


def new_player_gift(player_data):
    # starter kit choices
    # get first item in bag(which should be voucher) and get its name from item method

    player_data.bag[0] = None
    choice = input(
        "\nAh, I see you have a starter kit voucher from the adventurer guild. \nWhat weapon "
        "would you like to exchange it for?\n[Wooden Sword]\n[Bow]\n[Spell Book]\n").lower()  # lowercase choice

    player_data.bag[0] = item.get_item_by_id("W00001")

    if choice in ["wooden sword", "bow", "spell book"]:
        player_data.bag[0] = item.get_item_by_name(choice)
        print(
            f"\n[You Obtained a \"{player_data.bag[0].name().upper()}\"!]")  # Display weapon choice and capitalize it for coolness
    else:
        print("You did not type the right weapon to exchange the voucher for.")
        new_player_gift(player_data)


def shop(player_data):
    print("\nHey there adventurer! What can I get you?")

    if player_data.bag[0] is None:
        cont = input("Sorry man, I'm not selling anything at the moment. Be sure to come back when I am!\n...")
        town(player_data)

    # if bag contains a voucher give player starter weapon
    elif any(search_bag_for_voucher.name() == "Starter Kit Voucher" for search_bag_for_voucher in player_data.bag):
        new_player_gift(player_data)
    town(player_data)


def town(player_data):
    print("\n\nWelcome to Town!\n")

    choice = input("Where do you want to go?\n[Shop]\n[Bag]\n[Leave]\n").lower()
    if choice == "shop":
        shop(player_data)
    elif choice == "bag":
        bag.access_bag(player_data)
        town(player_data)  # go back to start of town script
    elif choice == "leave" and input("Are you sure you want to leave town? [Y/n]" == "n"):
        town(player_data)
    elif choice == "leave" and input("Are you sure you want to leave town? [Y/n]"):
        print("You Leave the town\nOff to adventure!")
        cont = input("...")
        controller("E00003", player_data)
    else:
        print("Please select correct choice.")
        town(player_data)

