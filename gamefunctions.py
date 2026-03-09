#Game Funcitons
#Finn Disbrow
#This file contains two functions
#one that calculates how many items a player can purchase based on their money and the item price, 
#and another that generates a random monster with specific attributes.


#Purchase Item Function
itemspurchased = 0
def purchase_item(itemPrice, startingMoney, quantitytoPurchase=1):
    affordable = startingMoney // itemPrice
    itemspurchased = min(affordable, quantitytoPurchase)
    remainingMoney = startingMoney - (itemspurchased * itemPrice)
    return itemspurchased, remainingMoney

itemspurchased, remainingMoney = purchase_item(50, 100, 3)
print(itemspurchased, remainingMoney)

itemspurchased, remainingMoney = purchase_item(50, 25, 5)
print(itemspurchased, remainingMoney)

itemspurchased, remainingMoney = purchase_item(50, 100)
print(itemspurchased, remainingMoney)


#Random Monster Function
import random
def new_random_monster():
    monsters = [
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
    m = random.choice(monsters)
    return {
    "name": m["name"],
    "description": m["description"],
    "health": random.randint(m["health_min"], m["health_max"]),
    "power": random.randint(m["power_min"], m["power_max"]),
    "money": random.randint(m["money_min"], m["money_max"])}

print(new_random_monster())
print(new_random_monster())
print(new_random_monster())

#Documentation and Strings

def print_welcome(name, width): #Function to output welcome message,
    greeting = f"Hello, {name}" #takes name and width as parameters
    return print(f"{greeting:^{width}}")
#Calling Function
print_welcome("Finn", 15)
print_welcome("King Charles", 28)
print_welcome("Ricky Bobby", 37)

#Print Shop Menu
def print_shop_menu(item1name, item1price, item2name, item2price):
    top_border = "/"+("-" * 20)+"\\"    #Border Formatting
    bottom_border = "\\"+("-" * 20)+"/"
    
    formatitem1price = f"${item1price:.2f}"
    itemline1 = f"|{item1name:<12}{formatitem1price:>8}|" #Formatted item1 line
    
    formatitem2price = f"${item2price:.2f}"
    itemline2 = f"|{item2name:<12}{formatitem2price:>8}|" #Formatted item2 line
    itemsdetails = f"{itemline1}\n{itemline2}"
    return print(f"{top_border}\n{itemsdetails}\n{bottom_border}") #returns menu of items

#Calling Function
print_shop_menu("Fishing Rod", 250, "Flys", 2.5075)
print_shop_menu("Tacos", 5.75, "Burritos", 7.1234)
print_shop_menu("Shoes", 158, "Socks", 22.754)