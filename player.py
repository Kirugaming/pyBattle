PLAYER_START_STRENGTH: int = 5
PLAYER_START_STAMINA: int = 5
PLAYER_START_MAGIC: int = 5
PLAYER_START_MAX_HEALTH: int = 20


class Player:

    def __init__(self, name, strength, stamina, magic, max_health):
        self._name = name
        self._max_health = max_health
        self._health = self._max_health
        self._stats = {"strength": strength, "stamina": stamina, "magic": magic}
        self._bag = [None, None, None, None, None]
        self._equips = {"weapon": None, "armor": None}
        self._known_locations = ["town"]
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
        self._health = new_health

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
    def known_locations(self) -> list:
        return self._known_locations

    @property
    def gold(self) -> int:
        return self._gold

    @gold.setter
    def gold(self, new_gold):
        self._gold = new_gold


def player_creation():
    return Player(
        input(
            "Welcome to the adventuring guild! Please register with the guild.\nEnter a name for your character: "
        ),
        PLAYER_START_STRENGTH,
        PLAYER_START_STAMINA,
        PLAYER_START_MAGIC,
        PLAYER_START_MAX_HEALTH,
    )
