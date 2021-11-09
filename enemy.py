from __future__ import annotations


class Enemy:
    def __init__(self, name, description, max_health, attack, defense, enemy_id):
        self._name = name
        self._description = description
        self._max_health = max_health
        self._attack = attack
        self._defense = defense
        self._enemy_id = enemy_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return self._description

    @property
    def max_health(self) -> str:
        return self._max_health

    @property
    def attack(self) -> str:
        return self._attack

    @property
    def defense(self) -> str:
        return self._defense

    @property
    def enemy_id(self) -> str:
        return self._enemy_id

    @property
    def enemy_type(self) -> str:
        return self._enemy_id[0]


enemies = {
    "E00001": Enemy("Skeleton",
                    "A Weak Skeleton.",
                    5, 3, 5, "E00001"),
    "E00002": Enemy("Zombie",
                    "A Weak Zombie.",
                    7, 4, 6, "E00002"),
    "E00003": Enemy("Bandit",
                    "A Nasty Bandit! Watch your pockets.",
                    8, 4, 6, "E00003")
}


def get_enemy_by_id(enemy_id) -> Enemy:
    if enemy_id in enemies:
        return enemies[enemy_id]
