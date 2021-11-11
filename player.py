import item


class Player:

    def __init__(self, name, strength, stamina, magic):
        self._name = name
        self._max_health = 10
        self._health = 10
        self._stats = {"strength": strength, "stamina": stamina, "magic": magic}
        self._bag = ["", "", "", "", ""]
        self._gold = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def max_health(self):
        return self._max_health

    @max_health.setter
    def max_health(self, new_max_health):
        self._max_health = new_max_health

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, new_health):
        self._health += new_health

    # lists with @property are janky as hell. you dont need a @(function).setter for lists i guess.
    # may have a method take parameters have a item and where to go and pass it through a setter.
    @property
    def stats(self):
        return self._stats

    @property
    def bag(self):
        return self._bag

    @property
    def gold(self):
        return self._gold

    @gold.setter
    def gold(self, new_gold):
        self._gold += new_gold


def player_creation():
    print("Welcome to the adventuring guild! Please register with the guild.")

    name_input = input("Enter a name for your character: ")

    player_data = Player(name_input, 5, 5, 5)

    print("\nYour name is " + player_data.name + "\nYour stats are " + str(player_data.stats["strength"]) +
          " Strength, " +
          str(player_data.stats["stamina"]) + " Stamina, and " + str(player_data.stats["magic"]) + " Magic.")

    # give player a voucher
    player_data.bag[0] = item.get_item_by_id("K00001")
    print("\nLooks like your all set! Dont forget to pick up your adventurer starter set at the shop.\nYou received a "
          "starter set voucher!")
    return player_data
