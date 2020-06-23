'''
    File name: slotmachine3col.py
    Author: Pierre Corazo Cesario
    Date created: 17/06/2020
    Python version: 3.8.3rc1
'''
import random
import time

# use .json to keep progress on funds

class SlotMachine:
    '''Setup for a slot machine.'''

    # initializes SlotMachine
    def __init__(self, cash=1000, chips=10):
        self.cash = cash
        self.chips = chips
        self.symbols = ['1', '2', '3',
                        '4', '5', '6',]
        self.exitcommands = ['exit', 'quit', 'stop', 'leave',]
        self.commands = ['help', 'show funds', 'show bet count', 'all',]
        self.fourmatch = 50
        self.threematch = 10
        self.twopair = 3
        self.onepair = 2
        self.spincost = 1
        self.dtcratio = 100
        self.flag = True
        self.betcount = 0

    # prints user's chips and cash
    def getfund(self):
        if self.chips == 1:
            print(
f'''You now have {self.chips} chip.
Your current balance is ${self.cash}.''')
        else:
            print(
f'''
You now have {self.chips} chips.
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

    # increments betcount by 1
    def incrementbetcount(self):
        self.betcount += 1

    def wanttoexit(self, char):
        '''Checks if user wants to exit program'''
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

        prints padded results
        print(f'{list[0].center(longStr)}')
        print(f'{list[1].center(longStr)}')
        print(f'{list[2].center(longStr)}')
        time.sleep(3)
        print(f'{list[0].center(longStr)} {list[3].center(longStr)}')
        print(f'{list[1].center(longStr)} {list[4].center(longStr)}')
        print(f'{list[2].center(longStr)} {list[5].center(longStr)}')
        time.sleep(3)
        print(f'{list[0].center(longStr)} {list[3].center(longStr)} {list[6].center(longStr)}')
        print(f'{list[1].center(longStr)} {list[4].center(longStr)} {list[7].center(longStr)}')
        print(f'{list[2].center(longStr)} {list[5].center(longStr)} {list[8].center(longStr)}')

    # call function to initiate cashtochips
    def cashconversionmode(self):
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

    # converts cash to chips
    def cashtochips(self, amount):
        convertcash = amount // self.dtcratio
        self.chips += convertcash
        self.cash -= convertcash * self.dtcratio

    # converts chips to cash
    def chipstocash(self, amount):
        self.cash += amount * self.dtcratio
        self.chips -= amount

    # calculates winnings
    def isCombo(self):
        x = self.finalResult
        return ((x[0] == x[3] == x[6]) or # top row
        (x[1] == x[4] == x[7]) or # mid row
        (x[2] == x[5] == x[8]) or # bottom row
        (x[0] == x[4] == x[8]) or # diagonal
        (x[2] == x[4] == x[6])) # diagonal



    # calculates your new balance and prints results
    def payout(self, matches, prize):
        self.chips += self.spincost * prize
        if self.spincost * prize == 1:
            print(f'{matches} matches! You won 1 chip!')
        else:
            print(f'{matches} matches! You won {self.spincost*prize} chips!')
            self.getfund()

    # main function with all other functions
    def main(self):
        while self.flag:
            self.counter = 0
            self.paircounter = 0
            if self.enoughchips():
                self.getfund()
                if not self.bet():
                    break
                self.printResults(self.getresult())
                if self.isCombo():
                    print('there is a combo!')
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
'''
Welcome to the slot machine!
You can type help for a list of commands.
'''
)

machine = SlotMachine()
machine.main()
