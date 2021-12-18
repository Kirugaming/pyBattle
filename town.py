import bag
import item
import player
import adventure
from ask import ask, continu
from fightController import controller


def new_player_gift(player_data):
    # starter kit choices
    # get first item in bag(which should be voucher) and get its name from item method

    player_data.bag[0] = None

    match ask("Ah, I see you have a starter kit voucher from the adventurer guild. \nWhat weapon "
              "would you like to exchange it for?", ("wooden sword", "bow", "spell book")):
        case "wooden sword":
            player_data.bag[0] = item.get_item_by_id("W00001")
        case "bow":
            player_data.bag[0] = item.get_item_by_id("W00002")
        case "spell book":
            player_data.bag[0] = item.get_item_by_id("W00003")


def shop(player_data):
    print("\nHey there adventurer! What can I get you?")

    if player_data.bag[0] is None:
        continu("Sorry man, I'm not selling anything at the moment. Be sure to come back when I am!")
        town(player_data)

    # if bag contains a voucher give player starter weapon
    elif any(search_bag_for_voucher.name() == "Starter Kit Voucher" for search_bag_for_voucher in player_data.bag):
        new_player_gift(player_data)
    town(player_data)


def town(player_data):
    print("\n\nWelcome to Town!\n")

    match ask("Where do you want to go?", ("shop", "bag", "leave")):
        case "shop":
            shop(player_data)
        case "bag":
            bag.access_bag(player_data)
            town(player_data)  # go back to start of town script
        case "leave":
            #     elif choice == "leave" and input("Are you sure you want to leave town? [Y/n]" == "n"):
            #         town(player_data)
            #     elif choice == "leave" and input("Are you sure you want to leave town? [Y/n]"):
            #         print("You Leave the town\nOff to adventure!")
            #         cont = input("...")
            adventure.adventure(player_data)
            #   controller("E00003", player_data)
