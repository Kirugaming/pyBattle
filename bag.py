def print_bag(player_data):
    print("Inside of your bag is...")
    for bag_index, item_in_bag in enumerate(player_data.bag, start=0):
        if all(item_in_bag is None for item_in_bag in player_data.bag):
            print("Your bag is empty :(")
            return player_data
        elif player_data.bag[bag_index]:
            print(f'[{bag_index + 1} : {player_data.bag[bag_index].name()}]')


def access_bag(player_data):
    print_bag(player_data)

    bag_action = input("Pick a item number to access\n[bag number][leave]")
    if bag_action.lower() == "leave":
        return player_data
    item_action = input(
        "What would you like to do with " + player_data.bag[int(bag_action) - 1].name() + "\n[Equip][Use]["
                                                                                          "Trash]")
    if item_action.lower() == "equip":
        equip_item(player_data, bag_action)

    if item_action.lower() == "use" and player_data.bag[int(bag_action) - 1].item_id()[0] == "C":
        use_item(player_data, bag_action)

    if item_action.lower() == "trash":
        trash_item(player_data, bag_action)


def equip_item(player_data, bag_action):
    if player_data.bag[int(bag_action) - 1] is None:
        print("There is nothing to equip.")
    elif player_data.bag[int(bag_action) - 1].item_id()[0] == "W":
        swap_equips(player_data, "weapon", bag_action)
    elif player_data.bag[int(bag_action) - 1].item_id()[0] == "A":
        swap_equips(player_data, "armor", bag_action)
    else:
        print("You can not equip this")

    access_bag(player_data)


def swap_equips(player_data, item_type, bag_action):
    item_withholding = player_data.equips[item_type]
    player_data.equips[item_type] = player_data.bag[int(bag_action) - 1]
    player_data.bag[int(bag_action) - 1] = item_withholding
    print(f"{player_data.equips[item_type].name()} was equipped\n")


def use_item(player_data, bag_action):
    # Consume item and give whatever depending on item
    pass


def trash_item(player_data, bag_action):
    trash_question = input("Are you sure you want to trash this item?[y/n]")
    if trash_question.lower() == "y":
        print(f"{player_data.bag[int(bag_action) - 1].name()} Has been trashed.")
        player_data.bag[int(bag_action) - 1] = None
    elif trash_question.lower() == "n":
        access_bag(player_data)
