import item


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

    print("\nYour name is " + player_data.name + ".\nYour stats are " + str(player_data.stats["strength"]) +
          " Strength, " +
          str(player_data.stats["stamina"]) + " Stamina, and " + str(player_data.stats["magic"]) + " Magic.")
    cont = input("...")

    # give player a voucher
    player_data.set_bag(item.get_item_by_id("K00001"), 0)
    print("\nLooks like you're all set! Don't forget to pick up your adventurer starter set at the shop.\n[You obtained"
          " \"STARTER KIT VOUCHER\"!]")
    cont = input("...")
    return player_data
