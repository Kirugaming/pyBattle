from player import Player
from item import Item


def start():
    print("Welcome to the adventuring guild! Please register with the guild.")

    name_input = input("Enter a name for your character: ")

    player_data = Player(name_input, 5, 5, 5)

    print("\nYour name is " + player_data.name + "\nYour stats are " + str(player_data.stats["strength"]) +
          " Strength, " +
          str(player_data.stats["stamina"]) + " Stamina, and " + str(player_data.stats["magic"]) + " Magic.")

    # give player voucher
    player_data.set_bag(Item(0), 0)
    print("\nLooks like your all set! Dont forget to pick up your adventurer starter set at the shop.\nYou received a "
          "starter set voucher!")

