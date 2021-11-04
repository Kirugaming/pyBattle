class Item:
    items = {
        "item": [
            {
                "itemName": "Starter Kit Voucher",
                "description": "A Voucher for a starter kit. You can redeem this at the store"
            },
            {
                "itemName": "Wooden Sword",
                "description": "A really terrible sword",
                "attack": 2,
                "strength": 2,
                "stamina": 1,
                "magic": 0
            },
            {
                "itemName": "Bow",
                "description": "The most basic bow",
                "attack": 2,
                "strength": 1,
                "stamina": 2,
                "magic": 0
            },
            {
                "itemName": "Weak Spell Book",
                "description": "A shabby spell book filled with only one spell",
                "attack": 2,
                "strength": 1,
                "stamina": 0,
                "magic": 2
            }
        ]
    }

    def __init__(self, item_id):
        self.name = self.items["item"][item_id]["itemName"]
        self.description = self.items["item"][item_id]["description"]

    def name(self):
        return self.name

    def description(self):
        return self.description


# DOES NOT WORK
class Weapon(Item):
    def __init__(self, item_id):
        super().__init__(item_id)
        self.attack_stat = self.items["item"][item_id]["attack"]
        self.strength_stat = self.items["item"][item_id]["strength"]
        self.stamina_stat = self.items["item"][item_id]["stamina"]
        self.magic_stat = self.items["item"][item_id]["magic"]

    def attack(self):
        return self.attack_stat

    def strength(self):
        return self.strength_stat

    def stamina(self):
        return self.stamina_stat

    def magic(self):
        return self.magic_stat
