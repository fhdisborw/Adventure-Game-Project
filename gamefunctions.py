#Game Funcitons
#Finn Disbrow
import random

#Purchase Item Function
def purchase_item(itemPrice, startingMoney, quantitytoPurchase=1):
    """This funciton calculates how many items a player can purchase based on the item price, 
    the player's starting money, and the quantity available to purchase. It returns the 
    number of items purchased and the remaining money."""
    itemspurchased = 0
    affordable = startingMoney // itemPrice #Calculation of number of items that can be afforded with starting money
    itemspurchased = min(affordable, quantitytoPurchase) #Calculation of number of items that can be purchased
    remainingMoney = startingMoney - (itemspurchased * itemPrice) #Calculation of remaining money after purchase
    return itemspurchased, remainingMoney #Return of number of items purchased and remaining money after purchase

#Random Monster Funciton
def new_random_monster():
    """This funciton generates a random monster with a name, description, health, power, and money.
    It uses a predefined list that contains the possible monsters and their attributes, 
    and returns a dictionary with the randomly generated monster's attributes."""
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

#Documentation and Strings
def print_welcome(name, width):
    """This funciton takes name and width as parameters
    and prints a welcome message centered within the specified width."""
    greeting = f"Hello, {name}" #Creation of greeting string using name parameter
    return print(f"{greeting:^{width}}") #Return of formatted print statement formatted for the width parameter

#Print Shop Menu
def print_shop_menu(item1name, item1price, item2name, item2price):
    """This function takes the names and prices of two items as parameters 
    and prints a formatted menu of the items with their prices."""
    top_border = "/"+("-" * 20)+"\\"    #Border Formatting
    bottom_border = "\\"+("-" * 20)+"/"
    
    formatitem1price = f"${item1price:.2f}"
    itemline1 = f"|{item1name:<12}{formatitem1price:>8}|" #Formatted item1 line
    
    formatitem2price = f"${item2price:.2f}"
    itemline2 = f"|{item2name:<12}{formatitem2price:>8}|" #Formatted item2 line
    itemsdetails = f"{itemline1}\n{itemline2}"
    return print(f"{top_border}\n{itemsdetails}\n{bottom_border}") #returns formatted menu of items

#Purchase Item Function Call
itemspurchased, remainingMoney = purchase_item(50, 100, 3)
print(itemspurchased, remainingMoney)
itemspurchased, remainingMoney = purchase_item(50, 25, 5)
print(itemspurchased, remainingMoney)
itemspurchased, remainingMoney = purchase_item(50, 100)
print(itemspurchased, remainingMoney)

#Random Monster Function Calll
print(new_random_monster())
print(new_random_monster())
print(new_random_monster())

#Calling Function
print_welcome("Finn", 15)
print_welcome("King Charles", 28)
print_welcome("Ricky Bobby", 37)

#Print Shop Menu Call
print_shop_menu("Fishing Rod", 250, "Flys", 2.5075)
print_shop_menu("Tacos", 5.75, "Burritos", 7.1234)
print_shop_menu("Shoes", 158, "Socks", 22.754)