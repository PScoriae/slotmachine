'''
    File name: slotmachine3col.py
    Author: Pierre Corazo Cesario
    Date created: 17/06/2020
    Python version: 3.8.3rc1
'''
import random

# use .json to keep progress on funds

class SlotMachine:
    '''Setup for a slot machine.'''

    # initializes SlotMachine
    def __init__(self, cash=1000, chips=10):
        self.cash = cash
        self.chips = chips
        self.symbols = ['Cherry', 'Diamond', 'Orange',
                        'Bell', '7', 'Bar',
                        'Watermelon', 'Star', 'Grapes',]
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

    # shows number of bets played so far
    def getbetcount(self):
        print(f'You bet {self.betcount} times.')

    # shows list of commands
    def getcommands(self):
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

    # checks if user wants to exit program
    def wanttoexit(self, char):
        if char.lower() in self.exitcommands:
            return True

    # if input is command, runs respective function
    def inputiscommand(self, char):
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

    # checks if user would like to continue playing
    def spinagain(self):
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

    # asks user how many chips to bet
    def bet(self):
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

    # checks if user has sufficient funds
    def enoughchips(self):
        if self.chips >= 1:
            return True
        else:
            print('Insufficient chips!')
            return False

    # checks if user has sufficient cash
    def enoughcash(self):
        if self.cash >= self.dtcratio:
            return True
        else:
            print('Insufficient cash!')
            return False

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

    # selects randomized choices from symbols and appends to result list
    # also creates calc list for comparison
    def getresult(self):
        self.result = random.choices(self.symbols, k=3)
        print('\n' + ' '.join(self.result))
        self.calc = self.result[:]
        for x in self.calc:
            while self.calc.count(x) > 1:
                self.calc.remove(x)

    # calculates winnings
    def calculate(self):
        for item in self.calc:
            if self.result.count(item) == 3:
                self.payout(3, self.threematch)
                break
            elif self.result.count(item) == 2:
                self.payout(2, self.onepair)
                break
            elif self.result.count(item) == 1:
                self.counter += 1
                if self.counter == 3:
                    print('No matches!')

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
                self.getresult()
                self.calculate()
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
