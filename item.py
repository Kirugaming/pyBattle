class Item:
    items = {
        "item": [
            {
                "itemName": "Starter Kit Voucher",
                "description": "A Voucher for a starter kit. You can redeem this at the store"
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
