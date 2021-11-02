import random


def adventure():
    paths = ["fork", "dungeon", "bandit", ]

    input("Pick a direction you would like to go\n[Left][Forward][Right]")
    while True:
        pathChoice = random.choice(paths)
        print(pathChoice)

        if pathChoice == "fork":
            choice = input("You encountered a fork in the road!\n[Left][Right]")
            # roll random num and see if bandit or some goodies
        if pathChoice == "dungeon":
            print("You found a dungeon!")
        if pathChoice == "bandit":
            print("Oh no! You Encountered a bandit")
        fightController()
