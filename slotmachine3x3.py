'''
    File name: slotmachine3col.py
    Author: Pierre Corazo Cesario
    Date created: 17/06/2020
    Python version: 3.8.3rc1
'''
import random
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
        if char.lower() in self.exitcommands:
            return True

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
            char = input()
            if self.inputiscommand(char):
                continue
            elif self.wanttoexit(char):
                return False
            # update to include full list of other agreements
            elif char.lower() == 'y' or not char:
                return True
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

    def enoughchips(self):
        '''Checks if user has sufficient chips.'''
        if self.chips >= 1:
            return True
        else:
            print('Insufficient chips!')
            return False

    def enoughcash(self):
        '''Checks if user has sufficient cash.'''
        if self.cash >= self.dtcratio:
            return True
        else:
            print('Insufficient cash!')
            return False

    def getresult(self):
        '''For 3 times, gets 3 random unique symbols from self.symbols
        and appends to a list.
        In reels dictionary, key, value is reelnumber, list.
        Moves contents of each list into main list.
        Returns main list.
        '''
        print('Spinning the reels!')
        self.reels = {}
        self.finalResult = []
        # gets results for each reel
        for reelnumber in range(3):
            self.reels[reelnumber] = random.sample(self.symbols, k=3)
        # adds results of each reel into main list.
        for x in range(3):
            self.finalResult[3*x:3*x+3] = self.reels[x]
        return self.finalResult

    def printResults(self, list):
        '''Takes in main list of results and
        prints it into a nice table.
        '''
        # determines longest string length for padding in table
        longStr = 0
        for string in self.symbols:
            if len(string) > longStr:
                longStr = len(string)

        # Prints padded results.
        if self.animation == True:
            print(f'{list[0].center(longStr)}')
            print(f'{list[1].center(longStr)}')
            print(f'{list[2].center(longStr)}')
            print()
            time.sleep(3)
            print(f'{list[0].center(longStr)} {list[3].center(longStr)}')
            print(f'{list[1].center(longStr)} {list[4].center(longStr)}')
            print(f'{list[2].center(longStr)} {list[5].center(longStr)}')
            print()
            time.sleep(3)
            print(f'{list[0].center(longStr)} {list[3].center(longStr)} {list[6].center(longStr)}')
            print(f'{list[1].center(longStr)} {list[4].center(longStr)} {list[7].center(longStr)}')
            print(f'{list[2].center(longStr)} {list[5].center(longStr)} {list[8].center(longStr)}')

        else:
            print(f'{list[0].center(longStr)} {list[3].center(longStr)} {list[6].center(longStr)}')
            print(f'{list[1].center(longStr)} {list[4].center(longStr)} {list[7].center(longStr)}')
            print(f'{list[2].center(longStr)} {list[5].center(longStr)} {list[8].center(longStr)}')

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
            self.counter = 0
            self.paircounter = 0
            if self.enoughchips():
                self.getfund()
                if not self.bet():
                    break
                self.printResults(self.getresult())
                if self.isCombo():
                    print('There is a combo!')
                    self.payout(self.matchedSymbol, self.symbolMultiplier[self.matchedSymbol])
                else:
                    print('No combos.')
                if not self.spinagain():
                    break
            else:
                if self.enoughcash():
                    if not self.cashconversionmode():
                        break
                else:
                    # suggest to sell organs in future
                    print('Filing bankruptcy!')
                    self.getbetcount()
                    break


print(
'''Welcome to the slot machine!
You can type 'help' for a list of commands.
'''
)

machine = SlotMachine()
machine.main()
