from random import randint
import bag
import enemy


# be able to pass different monsters into the function

def fight(encountered_enemy, player_data):
    player_damage = 0
    if (encountered_enemy.defense - player_data.equips['weapon'].attack()) > player_data.equips['weapon'].attack():
        print("The Enemy's defense is higher than your attack!\nYour attack did nothing.")
    else:
        player_damage = randint((encountered_enemy.defense - player_data.equips['weapon'].attack()),
                                player_data.equips['weapon'].attack() + 1)

    enemy_damage = encountered_enemy.attack
    # player hits enemy
    encountered_enemy.health = player_damage
    print(f"You hit the {encountered_enemy.name} for {player_damage} damage.")

    # enemy hits player
    player_data.health -= enemy_damage
    print(f"The {encountered_enemy.name} hit you for {enemy_damage} damage.")

    if player_data.health < 0:
        print("\nGAME OVER")
        exit()


def run(player_data, encountered_enemy):
    roll_player = randint(0, 100)
    roll_enemy = randint(0, 100)

    if roll_player > roll_enemy:
        print("You got away from the enemy")
        return True

    print(f"The {encountered_enemy.name} prevented you from running away.")
    player_data.health -= encountered_enemy.attack
    print(f"The {encountered_enemy.name} hit you for {encountered_enemy.attack} damage.")
    return False


def controller(encountered_id, player_data):
    encountered_enemy = enemy.get_enemy_by_id(encountered_id)

    print(f"\nYou Encountered a {encountered_enemy.name}")

    while encountered_enemy.health > 0:
        print(
            f"\n{player_data.name}'s Health: {player_data.health}\n{encountered_enemy.name}  Health:  {encountered_enemy.health}")
        action = input("Type an Action\n"
                       "[Fight], [Bag], [Run]\n")

        # actions!
        if action.lower() == "fight":
            fight(encountered_enemy, player_data)

        if action.lower() == "bag":
            bag.access_bag(player_data)
            controller(encountered_id, player_data)

        if action.lower() == "run" and run(player_data, encountered_enemy):
            return

    print(f"You defeated the  {encountered_enemy.name}")
