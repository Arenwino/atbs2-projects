'''
Chapter 6 Manipulating Strings

Zombie Dice Bots

Try writing some of your own bots to play Zombie Dice and see how they
compare against the other bots. Specifically, try to create the following bots:
•   A bot that, after the first roll, randomly decides if it will continue
    or stop
•   A bot that stops rolling after it has rolled two brains
•   A bot that stops rolling after it has rolled two shotguns
•   A bot that initially decides it’ll roll the dice one to four times, but will
    stop early if it rolls two shotguns
•   A bot that stops rolling after it has rolled more shotguns than brains

'''

import zombiedice, random

class RandomContinueZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        cont = random.randint(0,1)
        while diceRollResults is not None and cont == 0:
            diceRollResults = zombiedice.roll() # roll again
            cont = random.randint(0,1)

class Stop2BrainsZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):

        brains = 0
        diceRollResults = zombiedice.roll() # first roll

        while diceRollResults is not None:
            brains += diceRollResults['brains']
            if brains < 2:
                diceRollResults = zombiedice.roll() # roll again
            else: 
                break

class Stop2ShotgunsZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        shotguns = 0
        diceRollResults = zombiedice.roll() # first roll

        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']
            if shotguns < 2:
                diceRollResults = zombiedice.roll() # roll again
            else: 
                break

class DecideEarlyZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        rolls = random.randint(1, 4)
        shotguns = 0
        while rolls > 0:
            diceRollResults = zombiedice.roll()
            shotguns += diceRollResults['shotgun']

            if(shotguns > 1):
                break
            rolls -= 1

class MoreShotgunsThanBrainsZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        
        shotguns = 0
        brains = 0

        diceRollResults = zombiedice.roll()
    
        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']
            brains += diceRollResults['brains']
            if shotguns > brains:
                break
            diceRollResults = zombiedice.roll() 

zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Until 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Until 1 Shotgun', minShotguns=1),
    RandomContinueZombie(name='Random Continue Bot'),
    Stop2BrainsZombie(name='Stop after 2 Brains Bot'),
    Stop2ShotgunsZombie(name='Stop after 2 Shotguns Bot'),
    DecideEarlyZombie(name='Choose between 1-4 rolls early Bot'),
    MoreShotgunsThanBrainsZombie(name='Stop when more shotguns than brains'),
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
zombiedice.runTournament(zombies=zombies, numGames=1000)
#zombiedice.runWebGui(zombies=zombies, numGames=1000)
