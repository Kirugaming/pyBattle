from item import Item


class Player:
    max_health = 100

    def __init__(self, name, strength, stamina, magic):
        self.name = name
        self.health = 100
        self.stats = {"strength": strength, "stamina": stamina, "magic": magic}
        self.bag = ["", "", "", "", ""]
        self.gold = 0

    def get_name(self):
        return self.name

    def get_bag(self, index):
        return self.bag[index]

    def set_bag(self, item, position):
        self.bag[position] = item

    def remove_bag(self, index):
        self.bag[index] = ""


def player_creation():
    print("Welcome to the adventuring guild! Please register with the guild.")

    name_input = input("Enter a name for your character: ")

    player_data = Player(name_input, 5, 5, 5)

    print("\nYour name is " + player_data.name + "\nYour stats are " + str(player_data.stats["strength"]) +
          " Strength, " +
          str(player_data.stats["stamina"]) + " Stamina, and " + str(player_data.stats["magic"]) + " Magic.")

    # give player a voucher
    player_data.set_bag(Item(0), 0)
    print("\nLooks like your all set! Dont forget to pick up your adventurer starter set at the shop.\nYou received a "
          "starter set voucher!")

    return player_data
