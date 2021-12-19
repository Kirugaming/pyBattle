import bag
from ask import ask, continu


def ask_camp(player_data):
    match ask("Do you want to set up camp here?", ("y", "n")):
        case "y":
            camp(player_data)


def rest(player_data):
    player_data.health = player_data.max_health
    continu("You sleep for the night.\nYou regained all your health.")


def camp(player_data):
    while True:
        match ask("What would you like to do at the camp?", ("rest", "bag", "leave")):
            case "rest":
                rest(player_data)
            case "bag":
                bag.access_bag(player_data)
            case "leave":
                return

