class Item:

    def __init__(self, name, description, item_id):
        self._name = name
        self._description = description
        self._item_id = item_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return self._description

    @property
    def item_id(self) -> str:
        return f"Item Id: {self._item_id}"


class KeyItem(Item):
    def __init__(self, name, description, item_id):
        Item.__init__(self, name, description, item_id)


class Weapon(Item):
    def __init__(self, name, description, attack, strength, stamina, magic, item_id):
        Item.__init__(self, name, description, item_id)
        self._attack = attack
        self._strength = strength
        self._stamina = stamina
        self._magic = magic

    def attack(self):
        return self._attack

    def strength(self):
        return self._strength

    def stamina(self):
        return self._stamina

    def magic(self):
        return self._magic


items = {
    "K00001": KeyItem("Starter Kit Voucher",
                      "A Voucher for a starter kit. You can redeem this at the store",
                      "K00001"),
    "W00001": Weapon("Wooden Sword",
                     "A really terrible sword",
                     2, 2, 1, 0, "W00001"),
    "W00002": Weapon("Bow",
                     "The most basic bow",
                     2, 1, 2, 0, "W00002"),
    "W0003": Weapon("Weak Spell Book",
                    "A shabby spell book filled with only one spell",
                    2, 1, 0, 2, "W00003")
}


def get_item_by_id(item_id) -> Item:
    if item_id in items:
        return items.get(item_id)


def get_item_by_name(item_name) -> Item:
    items_list = items.items()
    for item in items_list:
        if item[1].name == item_name:
            return item[1]
