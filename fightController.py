
# WILL REMAKE IN NEXT COMMIT :)
# be able to pass different monsters into the function
def fight():
    global enemyHealth

    print("\nYou Encountered a " + enemyName)

    while enemyHealth > 0:
        print(enemyName + " Health: " + str(enemyHealth))
        action = input("Type an Action\n"
                       # Pick a action if i can figure it out later
                       "Fight, Bag, Run\n")

        # actions!
        if action.lower() == "fight":
            print("You hit the " + enemyName + " for 2 damage.")
            enemyHealth = enemyHealth - 2
            print(enemyHealth)

        if action.lower() == "bag":
            # print("You search your bag and find: ")
            print("There were no items in your bag...")

        if action.lower() == "run":
            # print("You tried to run away from the enemy but it caught you")
            print("You got away from the enemy")

    print("You defeated the " + enemyName)
