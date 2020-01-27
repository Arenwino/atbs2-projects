'''
Chapter 11 Debugging

Debugging Coin Toss

The following program is meant to be a simple coin toss guessing game. The
player gets two guesses (it’s an easy game). However, the program has several
bugs in it. Run through the program a few times to find the bugs that keep
the program from working correctly.
'''

import random

guess = ''
secondGuess = ''

coinSides = ('heads', 'tails')
while guess not in coinSides:
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.choice(coinSides) # 0 is tails, 1 is heads
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    while secondGuess not in coinSides:
        print('Enter heads or tails:')
        secondGuess = input()
    if toss == secondGuess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')