import bag
import item
import player
from fightController import controller


def new_player_gift(player_data):
    # starter kit choices
    # get first item in bag(which should be voucher) and get its name from item method

    player_data.bag[0] = ""
    choice = input(
        "\nAh, I see you have a starter kit voucher from the adventurer guild. \nWhat weapon "
        "would you like to exchange it for?\n[Wooden Sword]\n[Bow]\n[Spell Book]\n")
    if choice.lower() == "wooden sword":
        player_data.bag[0] = item.get_item_by_id("W00001")
        print("\n[You obtained \"WOODEN SWORD\"!]")
    if choice.lower() == "bow":
        player_data.bag[0] = item.get_item_by_id("W00002")
        print("\n[You obtained \"BOW\"!]")
    if choice.lower() == "spell book":
        player_data.bag[0] = item.get_item_by_id("W00003")
        print("\n[You obtained \"WEAK SPELL BOOK\"!]")
    shop(player_data)


def shop(player_data):
    print("\nHey there adventurer! What can I get you?")

    if player_data.bag[0] == "":
        cont = input("Sorry man, I'm not selling anything at the moment. Be sure to come back when I am!\n...")
        town(player_data)

    elif player_data.bag[0].name() == "Starter Kit Voucher":
        new_player_gift(player_data)
    else:
        cont = input("Sorry man, I'm not selling anything at the moment. Be sure to come back when I am!\n...")
        town(player_data)


def town(player_data):
    print("\n\nWelcome to Town!\n")

    choice = input("Where do you want to go?\n[Shop]\n[Bag]\n[Leave]\n")
    if choice.lower() == "shop":
        shop(player_data)
    elif choice.lower() == "bag":
        bag.access_bag(player_data)
        town(player_data)
    elif choice.lower() == "leave":
        choice = input("Are you sure you want to leave town? [Y/n]")
        if choice == "n":
            town(player_data)
        print("You Leave the town\nOff to adventure!")
        cont = input("...")
        controller("E00003", player_data)
