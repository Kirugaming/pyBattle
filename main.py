import player
import item
from ask import ask, continu
from town import town


def player_start():
    print("\nIf you see this symbol: \"...\", press ENTER to "
          "continue.\n--------------------------------------------------------\n")

    # make player object using player creation function and give it to give it to the town
    # (make player, plop him in town) Gonna pass this object through the program
    player_data = player.player_creation()
    print(
        f"\nYour name is {player_data.name}.\nYour stats are {str(player_data.stats['strength'])} Strength, {str(player_data.stats['stamina'])} Stamina, and {str(player_data.stats['magic'])} Magic.")

    # give player a voucher
    player_data.bag[0] = item.get_item_by_id("K00001")
    continu("\nLooks like you're all set! Don't forget to pick up your adventurer starter set at the shop.\n[You "
            "obtained \"STARTER KIT VOUCHER\"!]")
    town(player_data)


if __name__ == '__main__':
    print("  ____       _______ _______ _      ______ _ ")
    print(" |  _ \\   /\\|__   __|__   __| |    |  ____| |")
    print(" | |_) | /  \\  | |     | |  | |    | |__  | |")
    print(" |  _ < / /\\ \\ | |     | |  | |    |  __| | |")
    print(" | |_) / ____ \\| |     | |  | |____| |____|_|")
    print(" |____/_/    \\_\\_|     |_|  |______|______(_)")
    match ask("Start Game?", ("y", "n")):
        case "n":
            print("closing...")
            quit()
        case _:
            player_start()
