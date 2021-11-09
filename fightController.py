import enemy


# be able to pass different monsters into the function
def fight(encountered_id):

    encountered_enemy = enemy.get_enemy_by_id(encountered_id)

    print("\nYou Encountered a " + encountered_enemy.name)

    while encountered_enemy.health > 0:
        print(encountered_enemy.name + " Health: " + str(encountered_enemy.health))
        action = input("Type an Action\n"
                       "Fight, Bag, Run\n")

        # actions!
        if action.lower() == "fight":
            print("You hit the " + encountered_enemy.name + " for 2 damage.")
            encountered_enemy.health -= 2
            print(encountered_enemy.health)

        if action.lower() == "bag":
            # print("You search your bag and find: ")
            print("There were no items in your bag...")

        if action.lower() == "run":
            # print("You tried to run away from the enemy but it caught you")
            print("You got away from the enemy")

    print("You defeated the " + encountered_enemy.name)
