import item


def access_bag(player_data):
    print("Inside of your bag is...")
    for bag_index, item_in_bag in enumerate(player_data.bag, start=0):
        if player_data.bag[bag_index]:
            print("[" + str(bag_index + 1) + " : " + (player_data.bag[bag_index].name()) + "]")

    bag_action = input("Pick a item number to access\n[bag number][leave]")
    if bag_action.lower() == "leave":
        return
    item_action = input(
        "What would you like to do with " + player_data.bag[int(bag_action) - 1].name() + "\n[Equip][Use]["
                                                                                          "Trash]")
    if item_action.lower() == "equip":
        equip_item(player_data, bag_action)

    if item_action.lower() == "use":
        pass
    if item_action.lower() == "trash":
        pass


def equip_item(player_data, bag_action):
    if player_data.bag[int(bag_action) - 1].item_id()[0] == "W":
        for bag_index, item_in_bag in enumerate(player_data.bag, start=0):
            if player_data.bag[bag_index] == "":
                swap_equips(player_data, "weapon", bag_index, bag_action)
        print("You don't have enough room in your bag")

    elif player_data.bag[int(bag_action) - 1].item_id()[0] == "A":
        for bag_index, item_in_bag in enumerate(player_data.bag, start=0):
            if player_data.bag[bag_index] == "":
                swap_equips(player_data, "armor", bag_index, bag_action)
        print("You don't have enough room in your bag")
    else:
        print("You can not equip this")

    access_bag(player_data)


def swap_equips(player_data, item_type, bag_index, bag_action):
    item_withholding = player_data.equips[item_type]
    player_data.equips[item_type] = player_data.bag[int(bag_action) - 1]
    player_data.bag[int(bag_action) - 1] = item_withholding
    print(player_data.equips[item_type].name() + " was equipped\n")
    access_bag(player_data)


def use_item():
    print("ITEM was used\n")
    # TODO: show item is used and trigger behavior item uses


def trash_item():
    print("ITEM was tossed\n")
    # TODO: show item was tossed and remove item from bag


class Player:

    def __init__(self, name, strength, stamina, magic):
        self._name = name
        self._max_health = 10
        self._health = 10
        self._stats = {"strength": strength, "stamina": stamina, "magic": magic}
        self._bag = ["", "", "", "", ""]
        self._equips = {"weapon": "", "armor": ""}
        self._gold = 0

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def max_health(self) -> int:
        return self._max_health

    @max_health.setter
    def max_health(self, new_max_health):
        self._max_health += new_max_health

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self, new_health):
        self._health += new_health

    @property
    def stats(self) -> dict:
        return self._stats

    @property
    def bag(self) -> list:
        return self._bag

    @property
    def equips(self) -> dict:
        return self._equips

    @property
    def gold(self) -> int:
        return self._gold

    @gold.setter
    def gold(self, new_gold):
        self._gold += new_gold


def player_creation():
    print("Welcome to the adventuring guild! Please register with the guild.")

    name_input = input("Enter a name for your character: ")

    player_data = Player(name_input, 5, 5, 5)

    print("\nYour name is " + player_data.name + ".\nYour stats are " + str(player_data.stats["strength"]) +
          " Strength, " +
          str(player_data.stats["stamina"]) + " Stamina, and " + str(player_data.stats["magic"]) + " Magic.")

    # give player a voucher
    player_data.bag[0] = item.get_item_by_id("K00001")
    print("\nLooks like you're all set! Don't forget to pick up your adventurer starter set at the shop.\n[You obtained"
          " \"STARTER KIT VOUCHER\"!]")
    cont = input("...")
    return player_data
