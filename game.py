import gamefunctions

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
print("\nTesting purchase function:")
items, money = gamefunctions.purchase_item(50, 120, 3)
print(f"Items purchased: {items}, Remaining money: {money}")
