'''
Chapter 5 Dictionaries and Structuring Data

Fantasy Game Inventory

You are creating a fantasy video game. The data structure to model the
player’s inventory will be a dictionary where the keys are string values
describing the item in the inventory and the value is an integer value
detailing how many of that item the player has. For example, the dictionary 
value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
means the player has 1 rope, 6 torches, 42 gold coins, and so on.


List to Dictionary Function for Fantasy Game Inventory

Write a function named addToInventory(inventory, addedItems), where the
inventory parameter is a dictionary representing the player’s inventory (like
in the previous project) and the addedItems parameter is a list like dragonLoot.
The addToInventory() function should return a dictionary that represents the
updated inventory.

'''

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(f'{v} {k}')
        item_total += v

    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory

displayInventory(stuff)

inv = addToInventory(inv, dragonLoot)
displayInventory(inv)