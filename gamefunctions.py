"""Functions for gameplay; including purchasing items, generating
random monsters, and printing formatted text for menus and greetings.

This module provides functions used throughout the game. It includes
logic for determining how many items a player can afford, creating random
monsters with given parameters, and printing formatted output such as welcome
messages and shop menus. These functions support gameplay and
simplify repeated formatting tasks.

Typical usage example:

    items, money = purchase_item(50, 100, 3)
    monster = new_random_monster()
    print_welcome("Finn", 20)
    print_shop_menu("Sword", 150, "Shield", 90)
"""

import random

#Purchase Item Function
def purchase_item(itemPrice, startingMoney, quantitytoPurchase=1):
    """
    Calculate how many items a player can purchase.

    Parameters:
        itemPrice (int): The cost of a single item.
        startingMoney (int): The amount of money the player has.
        quantityToPurchase (int): The maximum number of items the
            player is allowed to buy. Defaults to 1.

    Returns:
        tuple: A tuple containing:
            - int: The number of items purchased.
            - int: The remaining money after the purchase.

    Example:
        >>> purchase_item(50, 100, 3)
        (2, 0)
    """

    itemspurchased = 0
    affordable = startingMoney // itemPrice #Calculation of number of items that can be afforded with starting money
    itemspurchased = min(affordable, quantitytoPurchase) #Calculation of number of items that can be purchased
    remainingMoney = startingMoney - (itemspurchased * itemPrice) #Calculation of remaining money after purchase
    return itemspurchased, remainingMoney #Return of number of items purchased and remaining money after purchase

#Random Monster Funciton
def new_random_monster():
    """
    Generate a random monster with random attributes.

    This function selects a monster from a list of possible
    monsters. Each monster type includes ranges for health, power, and
    money. The function randomly generates a monster within those ranges
    and returns a dictionary describing the monster.

    Parameters:
        None

    Returns:
        A dictionary containing:
            - name (str): The monster's name.
            - description (str): A short description of the monster.
            - health (int): Randomized health value.
            - power (int): Randomized power value.
            - money (int): Randomized amount of money dropped.

    Example:
        >>> monster = new_random_monster()
        >>> print(monster["name"])
        Goblin
    """

    monsters = [ #List of possible monsters with their attributes
        {"name" : "Goblin",
        "description" : "A small goblin snarls and charges at you.",
        "health_min": 2,
        "health_max": 10,
        "power_min": 1,
        "power_max": 3,
        "money_min": 0,
        "money_max": 20},
        {"name" : "Vulture",
        "description" : "A hungry vulture circles above, eyeing your belongings.",
        "health_min": 5,
        "health_max": 35,
        "power_min": 0,
        "power_max": 3,
        "money_min": 200,
        "money_max": 800},
        {"name" : "Orc",
        "description" : "A fierce orc stands before you, ready to attack.",
        "health_min": 12,
        "health_max": 40,
        "power_min": 3,
        "power_max": 15,
        "money_min": 5,
        "money_max": 100}]
    m = random.choice(monsters) #Assignment of random monster from list to variable m
    return { #Return of dictionary with randomly generated monster's attributes
    "name": m["name"],
    "description": m["description"],
    "health": random.randint(m["health_min"], m["health_max"]),
    "power": random.randint(m["power_min"], m["power_max"]),
    "money": random.randint(m["money_min"], m["money_max"])}

#Monster Game Actions
def displayfightstatistics(player_hp, monster):
    print(f"\nYour HP: {player_hp}")
    print(f"{monster['name']} HP: {monster['health']}\n")
def getUserFightAction(): 
    print("What will you do?")
    print("1) Attack")
    print("2) Run Away")
    if input("1 or 2? >") not in ["1", "2"]:
        print("\nInvalid choice.\n")
        return getUserFightAction()
    return input("1 or 2? >")
def do_fight_action(action, player_hp, player_gold, monster):
    if action == "1":
        dmg_m = random.randint(5, 15)
        dmg_p = random.randint(0, monster["power"])

        monster["health"] -= dmg_m
        player_hp -= dmg_p

        print(f"\nYou deal {dmg_m} damage to the {monster['name']}.")
        print(f"The {monster['name']} deals {dmg_p} damage to you.\n")

        return player_hp, player_gold, monster["health"] <= 0, player_hp <= 0

    elif action == "2":
        print("\nYou run away safely.\n")
        return player_hp, player_gold, False, False

    else:
        print("\nInvalid choice.\n")
        return player_hp, player_gold, False, False

#Documentation and Strings
def print_welcome(name, width):
    """
    Print a centered welcome message.

    This function takes a player's name and a desired width, then prints
    a welcome message centered within that width.

    Parameters:
        name (str): The player's name to include in the greeting.
        width (int): The total width used to center the message.

    Returns:
        None

    Example:
        >>> print_welcome("Finn", 15)
           Hello, Finn
    """

    greeting = f"Hello, {name}" #Creation of greeting string using name parameter
    return print(f"{greeting:^{width}}") #Return of formatted print statement formatted for the width parameter

#Print Shop Menu
def print_shop_menu(item1name, item1price, item2name, item2price):
    r"""
    Print a formatted shop menu displaying two items and their prices.

    This function takes the names and prices of two items and prints a
    formatted menu showing each item aligned with its price.

    Parameters:
        item1name (str): The name of the first item.
        item1price (float): The price of the first item.
        item2name (str): The name of the second item.
        item2price (float): The price of the second item.
    
    Returns:
        Formatted print output of the shop menu.

    
    Example:
        >>> print_shop_menu("Tacos", 5.75, "Burritos", 7.12)
        /--------------------\
        |Burritos       $7.12|
        \--------------------/
    """

    top_border = "/"+("-" * 20)+"\\"    #Border Formatting
    bottom_border = "\\"+("-" * 20)+"/"
    
    formatitem1price = f"${item1price:.2f}"
    itemline1 = f"|{item1name:<12}{formatitem1price:>8}|" #Formatted item1 line
    
    formatitem2price = f"${item2price:.2f}"
    itemline2 = f"|{item2name:<12}{formatitem2price:>8}|" #Formatted item2 line
    itemsdetails = f"{itemline1}\n{itemline2}"
    return print(f"{top_border}\n{itemsdetails}\n{bottom_border}") #returns formatted menu of items

#Test Funciton
if (__name__ == "__main__"):
    def test_functions():
    # Test purchase_item
        print(purchase_item(50, 100, 3))

    # Test new_random_monster
        print(new_random_monster())

    # Test print_welcome
        print_welcome("Finn", 20)

    # Test print_shop_menu
        print_shop_menu("Sword", 150, "Shield", 90)

