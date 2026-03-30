import gamefunctions

#Purchase Item Function Call
itemspurchased, remainingMoney = gamefunctions.purchase_item(50, 100, 3)
print(itemspurchased, remainingMoney)
itemspurchased, remainingMoney = gamefunctions.purchase_item(50, 25, 5)
print(itemspurchased, remainingMoney)
itemspurchased, remainingMoney = gamefunctions.purchase_item(50, 100)
print(itemspurchased, remainingMoney)

#Random Monster Function Calll
print(gamefunctions.new_random_monster())
print(gamefunctions.new_random_monster())
print(gamefunctions.new_random_monster())

#Print Welcome Function Call
gamefunctions.print_welcome("Finn", 15)
gamefunctions.print_welcome("King Charles", 28)
gamefunctions.print_welcome("Ricky Bobby", 37)

#Print Shop Menu Call
gamefunctions.print_shop_menu("Fishing Rod", 250, "Flys", 2.5075)
gamefunctions.print_shop_menu("Tacos", 5.75, "Burritos", 7.1234)
gamefunctions.print_shop_menu("Shoes", 158, "Socks", 22.754)


#Assignment 8; game.py file creation and import gamefunctions.py file with 
#function calls to test the functions in gamefunctions.py.

#import gamefunctions

# Ask for name
name = input("What is your name? ")

# Call print_welcome
gamefunctions.print_welcome(name, 30)

# Call new_random_monster
print("\nA random monster appears:")
print(gamefunctions.new_random_monster())

# Call print_shop_menu
print("\nHere is the shop menu:")
gamefunctions.print_shop_menu("Flys", 75, "Rods", 10)

# Call purchase_item
print("\nItems Purchased & Remaining Money:")
items, money = gamefunctions.purchase_item(50, 120, 3)
print(f"Items purchased: {items}, Remaining money: {money}")
