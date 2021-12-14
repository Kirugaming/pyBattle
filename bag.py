from ask import ask
from item import Item


def print_bag(player_data) -> str:
    bag = "".join(
        f"\n[{bag_index + 1} : {player_data.bag[bag_index].name()}]"
        for bag_index, item_in_bag in enumerate(player_data.bag, start=0)
        if isinstance(item_in_bag, Item)
    )
    if bag == "":
        return "Your bag is empty :("
    return bag


def access_bag(player_data):
    while True:
        bag_action = input(
            f"{print_bag(player_data)}\nPick a item number to access\n[bag number][leave]").lower()
        # i cant figure out how to simplify this AAA

        if bag_action == "leave":
            return player_data
        bag_action = player_data.bag[int(bag_action) - 1]

        match ask(f"What would you like to do with {bag_action.name()}?", ("equip", "use", "trash")):
            case "equip":
                equip_item(player_data, bag_action)
            case "use":
                use_item(player_data, bag_action)
            case "trash":
                trash_item(player_data, bag_action)


def equip_item(player_data, bag_action):
    match bag_action.item_type():  # get first letter of id which determines item type
        case None:
            print("There is nothing to equip.")
        case "W":
            swap_equips(player_data, "weapon", bag_action)
        case "A":
            swap_equips(player_data, "armor", bag_action)
        case _:
            print("You can not equip this")


def swap_equips(player_data, item_type, bag_action):
    item_withholding = player_data.equips[item_type]
    player_data.equips[item_type] = bag_action

    for bag_index, item_in_bag in enumerate(player_data.bag, start=0):
        if player_data.bag[bag_index] is bag_action:
            player_data.bag[bag_index] = item_withholding
            break

    print(f"{player_data.equips[item_type].name()} was equipped\n")


def use_item(player_data, bag_action):
    # Consume item and give whatever depending on item
    pass


def trash_item(player_data, bag_action):
    match ask("Are you sure you want to trash this item?", ("y", "n")):
        case "y":
            print(f"{player_data.bag[int(bag_action) - 1].name()} Has been trashed.")
            player_data.bag[int(bag_action) - 1] = None
        case "n":
            return
