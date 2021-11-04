import player
from town import town

if __name__ == '__main__':
    print("Battle!")
    answer = input("Start Game? [Y/n]")
    if answer == "n":
        print("closing...")
    else:
        print("\nIf you see this symbol: [ > ], press ENTER to "
              "continue.\n------------------------------------------------------\n")

        # make player object using player creation function and give it to give it to the town
        # (make player, plop him in town) Gonna pass this object through the program
        town(player.player_creation())

