import enemy


# be able to pass different monsters into the function

def fight(encountered_enemy, player_data):
    player_damage = (encountered_enemy.defense - player_data.equiped_weapon.attack)
    enemy_damage = encountered_enemy.attack

    # player hits enemy
    encountered_enemy.health -= player_damage
    print("You hit the " + encountered_enemy.name + " for " + player_damage + " damage.")

    # enemy hits player
    player_data.health -= enemy_damage
    print("The " + encountered_enemy.name + " hit you for " + enemy_damage + " damage.")


def controller(encountered_id, player_data):
    encountered_enemy = enemy.get_enemy_by_id(encountered_id)

    print("\nYou Encountered a " + encountered_enemy.name)

    while encountered_enemy.health > 0:
        print(encountered_enemy.name + " Health: " + str(encountered_enemy.health))
        action = input("Type an Action\n"
                       "Fight, Bag, Run\n")

        # actions!
        if action.lower() == "fight":
            fight(encountered_enemy, player_data)

        if action.lower() == "bag":
            bag()
            # print("You search your bag and find: ")
            print("There were no items in your bag...")

        if action.lower() == "run":
            # print("You tried to run away from the enemy but it caught you")
            print("You got away from the enemy")

    print("You defeated the " + encountered_enemy.name)
