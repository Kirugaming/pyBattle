class Player:
    def __init__(self, name, strength, stamina, magic):
        self.name = name
        self.stats = {"strength": strength, "stamina": stamina, "magic": magic}
        self.bag = ["", "", "", "", ""]

    def get_name(self):
        return self.name

    def set_bag(self, item, position):
        self.bag[position] = item
