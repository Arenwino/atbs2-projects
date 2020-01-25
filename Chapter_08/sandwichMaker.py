'''
Chapter 8 Input Validation

Sandwich Maker

Write a program that asks users for their sandwich preferences. The program 
should use PyInputPlus to ensure that they enter valid input, such as:
•   Using inputMenu() for a bread type: wheat, white, or sourdough.
•   Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
•   Using inputYesNo() to ask if they want cheese.
•   If so, using inputMenu() to ask for a cheese type: cheddar, Swiss,
    or mozzarella.
•   Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
•   Using inputInt() to ask how many sandwiches they want. Make sure this
    number is 1 or more.
Come up with prices for each of these options, and have your program
display a total cost after the user enters their selection

'''

import pyinputplus as pyip

prices = {
    'breads': {
        'wheat': 1.00,
        'white': 1.25,
        'sourdough': 2.00,
    },
    'proteins': {
        'chicken': 1.50, 
        'turkey': 1.25, 
        'ham': 1.75,
        'tofu': 2.00,
    },
    'cheeses': {
        'cheddar': 0.75,
        'Swiss': 1.25,
        'mozzarella': 1.25,
    },
    'mayo': 0.5,
    'mustard': 0.25,
    'lettuce': 0.50,
    'tomato': 0.50,
}

totalSandwich = 0

breadChoice = pyip.inputMenu(prices['breads'].keys(), prompt='What type of bread do you want? ')
totalSandwich += prices['breads'][breadChoice]

proteinChoice = pyip.inputMenu(prices['proteins'].keys(), prompt='What type of protein do you want? ')
totalSandwich += prices['proteins'][proteinChoice]

cheeseYesNo = pyip.inputYesNo(prompt='Do you want cheese on your sandwich? ')
if cheeseYesNo == 'yes':
    cheeseChoice = pyip.inputMenu(prices['cheeses'].keys(), prompt='What kind of cheese do you want? ')
    totalSandwich += prices['cheeses'][cheeseChoice]

mayoYesNo = pyip.inputYesNo(prompt='Do you want mayo on your sandwich? ')
if mayoYesNo == 'Yes':
    totalSandwich += prices['mayo']

mustardYesNo = pyip.inputYesNo(prompt='Do you want mustard on your sandwich? ')
if mustardYesNo == 'Yes':
    totalSandwich += prices['mustard']

lettuceYesNo = pyip.inputYesNo(prompt='Do you want lettuce on your sandwich? ')
if lettuceYesNo  == 'Yes':
    totalSandwich += prices['lettuce']

tomatoYesNo = pyip.inputYesNo(prompt='Do you want tomato on your sandwich? ')
if tomatoYesNo  == 'Yes':   
    totalSandwich += prices['tomato']

sandwichQuantity = pyip.inputInt(prompt='How many sandwiches do you want? ', min=1) 
totalSandwich *= sandwichQuantity

print('Total cost: ${:.2f}'.format(totalSandwich))