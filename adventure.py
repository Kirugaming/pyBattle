import random

from ask import ask
from fightController import controller
import town


def fork(player_data):
    ask("You Encountered a fork in the road! Pick a path to go through.", ("left", "right"))


def dungeon(player_data):
    print("You found a Dungeon!")


def randomEncounter(player_data):
    return controller("E00003", player_data)


def go_to_known_location(player_data):
    pass
    match ask("Pick a location to go to", player_data.known_locations):
        case "town":
            town.town(player_data)


def randomPath(player_data):
    return random.choice([randomEncounter(player_data), fork(player_data), dungeon(player_data)])


def adventure(player_data):
    match ask("Would you like to go to a known location or adventure?", ("known location", "adventure")):
        case "known location":
            go_to_known_location(player_data)
    while True:
        ask("Pick a direction you would like to go.", ("left", "forward", "right"))
        randomPath(player_data)