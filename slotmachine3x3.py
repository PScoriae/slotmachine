'''
File name: slotmachine3col.py
Author: Pierre Corazo Cesario
Date created: 17/06/2020
Python version: 3.8.3rc1
'''
import random
import sys
import time

# use .json to keep progress on funds
# flask to create gui web app version.
# json to handle different users.

class SlotMachine:
    '''Setup for a slot machine.'''
    def __init__(self, cash=15000, chips=1000):
        self.symbols = ['Diamond', 'Gold', 'Silver',
                        'Bronze', '7', 'Cherry',]
        self.symbolMultiplier = {self.symbols[0]: 10, self.symbols[1]: 7,
                                self.symbols[2]: 5, self.symbols[3]: 2,
                                self.symbols[4]: 9, self.symbols[5]: 8}
        self.exitcommands = ['exit', 'quit', 'stop', 'leave',]
        self.commands = ['help', 'show funds', 'show bet count', 'all',]
        self.cash = cash
        self.chips = chips
        self.spincost = 1
        self.dtcratio = 100  # Dollar to chip ratio
        self.flag = True
        self.betcount = 0
        self.animation = True

    def getfund(self):
        '''Prints user's current funds.'''
        if self.chips == 1:
            print(
f'''You now have {self.chips} chip.
Your current balance is ${self.cash}.''')
        else:
            print(
f'''You now have {self.chips} chips.
Your current balance is ${self.cash}.
'''
)

    def getbetcount(self):
        '''Prints current bet count.'''
        print(f'You bet {self.betcount} times.')

    def getcommands(self):
        '''Prints list of commands.'''
        print(
f'''
Quit commands:
{self.exitcommands}

General commands:
{self.commands}'''
        )

    def incrementbetcount(self):
        '''Increments betcount by 1.'''
        self.betcount += 1

    def wanttoexit(self, char):
        '''Checks if user wants to exit program.'''
        return char.lower() in self.exitcommands

    def inputiscommand(self, char):
        '''If input is command, runs respective function.'''
        if char.lower() == 'show funds':
            self.getfund()
            return True
        elif char.lower() == 'show bet count':
            self.getbetcount()
            return True
        elif char.lower() == 'help':
            self.getcommands()
            return True
        elif char.lower() == 'convert cash':
            self.cashconversionmode()
            self.getfund()
            return True
        elif char.lower() == 'cashout':
            self.chipconversionmode()
            self.getfund()
            return True

    def spinagain(self):
        '''Checks if the user would like to continue playing.'''
        while True:
            print('Would you like to spin again?(Y/n)')
            char = input() or 'y'
            if self.inputiscommand(char):
                continue
            elif self.wanttoexit(char):
                return False
            # update to include full list of other agreements
            elif char.lower() in ['y', 'yes']:
                return True
            elif char.lower() in ['n', 'no']:
                return False
            else:
                print("I don't understand")

    def bet(self):
        '''Asks user how many chips to bet.'''
        while True:
            print('How many chips are you betting? Default is 1.')
            amount = str(input('')) or '1'
            try:
                if self.inputiscommand(amount):
                    continue
                elif self.wanttoexit(amount):
                    return False
                elif amount.lower() == 'all':
                    self.incrementbetcount()
                    self.spincost = self.chips
                    self.chips = 0
                    return True
                elif 0 < int(amount) <= self.chips:
                    self.incrementbetcount()
                    self.spincost = int(amount)
                    self.chips -= self.spincost
                    return True
                else:
                    print('Error! Please enter a valid amount.')
            except:
                print('Please enter a number!')

    def spinReel(self):
        '''Spins the reels and returns a list with results.'''
        print('Spinning the reels!')
        self.reels, self.finalResult = {}, []
        # gets results for each reel
        for reelnumber in range(3):
            self.reels[reelnumber] = random.sample(self.symbols, k=3)
        # adds results of each reel into main list.
        for x in range(3):
            self.finalResult[3*x:3*x+3] = self.reels[x]
        return self.finalResult

    def printResults(self, list):
        '''Prints list of results into a pseudo 3x3 reel.'''
        # determines longest string length for padding in table
        longStr = 0
        for string in self.symbols:
            if len(string) > longStr:
                longStr = len(string)

        # Prints padded results.
        if self.animation == True:
            for x in range(3):
                print(f'{list[x].center(longStr)}')
            print()
            time.sleep(1.5)
            for x in range(3):
                print(f'{list[x].center(longStr)} {list[x+3].center(longStr)}')
            print()
            time.sleep(1.5)
            for x in range(3):
                print(f'{list[x].center(longStr)} {list[x+3].center(longStr)} {list[x+6].center(longStr)}')
        else:
            for x in range(3):
                print(f'{list[x].center(longStr)} {list[x+3].center(longStr)} {list[x+6].center(longStr)}')

    def cashconversionmode(self):
        '''Input mode to convert cash to chips.'''
        print('Now in cash conversion mode.')
        self.getfund()
        print('Enter amount of cash to convert:')
        while True:
            try:
                amount = str(input())
                if self.inputiscommand(amount):
                    continue
                elif self.wanttoexit(amount):
                    return False
                elif amount == 'all':
                    self.cashtochips(self.cash)
                    return True
                elif self.dtcratio <= int(amount) <= self.cash:
                    self.cashtochips(int(amount))
                    return True
                else:
                    print('Error! Please enter a valid amount.')
            except:
                print('I do not understand.')

    def chipconversionmode(self):
        '''Input mode to convert chips to cash.'''
        print('Now in chip conversion mode.')
        self.getfund()
        print('Enter amount of chips to convert:')
        while True:
            try:
                amount = str(input())
                if self.inputiscommand(amount):
                    continue
                elif self.wanttoexit(amount):
                    return False
                elif amount == 'all':
                    self.chipstocash(self.chips)
                    return True
                elif 0 < int(amount) <= self.chips:
                    self.chipstocash(int(amount))
                    return True
                else:
                    print('Error! Please enter a valid amount.')
            except:
                print('I do not understand.')

    def cashtochips(self, amount):
        '''Converts cash to chips.'''
        convertcash = amount // self.dtcratio
        self.chips += convertcash
        self.cash -= convertcash * self.dtcratio

    def chipstocash(self, amount):
        '''Converts chips to cash.'''
        self.cash += amount * self.dtcratio
        self.chips -= amount

    def isCombo(self):
        x = self.finalResult
        # Checks for row matches.
        for index in range(2):
            if x[index] == x[index+3] == x[index+6]:
                self.matchedSymbol = x[index]
                return True

        # Checks for negative diagonal.
        if x[0] == x[4] == x[8]:
            self.matchedSymbol = x[0]
            return True

        # Checks for positive diagonal.
        if x[2] == x[4] == x[6]:
            self.matchedSymbol = x[2]
            return True

    def payout(self, matchedSymbol, symbolMultiplier):
        '''Pays the player accounting for coin and symbol multiplier.'''
        self.chips += self.spincost * symbolMultiplier
        print(f'You got a match for {matchedSymbol}! You won {self.spincost*symbolMultiplier} chips!')
        self.getfund()

    def main(self):
        '''Main function to run the logic of the game.'''
        while self.flag:
            self.counter, self.paircounter = 0, 0
            if self.chips >= 1:
                self.getfund()
                if not self.bet():
                    sys.exit()
                self.printResults(self.spinReel())
                if self.isCombo():
                    print('There is a combo!')
                    self.payout(self.matchedSymbol, self.symbolMultiplier[self.matchedSymbol])
                else:
                    print('No combos.')
                if not self.spinagain():
                    sys.exit()
            else:
                print('Insufficient chips!')
                if self.cash >= self.dtcratio:
                    if not self.cashconversionmode():
                        sys.exit()
                else:
                    # suggest to sell organs in future
                    print('Insufficient cash!')
                    print('Filing bankruptcy!')
                    self.getbetcount()
                    sys.exit()

print(
'''Welcome to the slot machine!
You can type 'help' for a list of commands.
'''
)

machine = SlotMachine()
machine.main()
