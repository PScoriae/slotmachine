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
        self.dupe_checker = False
        self.symbols = ['Cherry', 'Banana', 'Watermelon', '7']
        self.fourmatch = 10
        self.threematch = 3
        self.twopair = 2
        self.onepair = 1
        self.spincost = 1
        self.dtcratio = 100
        self.flag = True

    def getfund(self):
        if self.chips == 1:
            print(
f'''
You now have {self.chips} chip.
Your current balance is ${self.cash}.
'''
                )
        else:
            print(
f'''
You now have {self.chips} chips.
Your current balance is ${self.cash}.
'''
                )

    # determines if user would like to continue playing
    def spinagain(self):
        print('Would you like to spin again?(Y/n)')
        question = input()
        if question.lower() == 'y' or not question:
            return True
        else:
            return False

    def bet(self):
        print('How many chips are you betting? Default is 1.')
        while True: # maybe change to for loop with defined number of tries
            multiplier = input('') or '1'
            try:
                if multiplier.lower() == 'exit':
                    return False
                    break
                elif 0 < int(multiplier) <= self.chips:
                    self.spincost = int(multiplier)
                    self.chips -= self.spincost
                    return True
                    break
                else:
                    print('Error! Please enter a valid amount.')
            except:
                print('That is not a number!')

    # checks if user has sufficient funds
    def enoughchips(self):
        if self.chips >= 1:
            return True
        else:
            print('Insufficient chips!')
            return False

    def enoughcash(self):
        if self.cash >= self.dtcratio:
            return True
        else:
            print('Insufficient cash!')
            return False

    # call function to initiate cashtochips
    def conversionmode(self):
        print('Now in cash conversion mode.\n'
        'How much cash would you like to convert?')
        while True:
            try:
                amount = str(input())
                if amount.lower() == 'exit':
                    return False
                elif self.dtcratio <= int(amount) <= self.cash:
                    self.cashtochips(int(amount))
                    return True
                else:
                    print('Error! Please enter a valid number.')
            except:
                print('I do not understand.')

    # converts cash to chips
    def cashtochips(self, amount):
        convertcash = amount // self.dtcratio
        self.chips += convertcash
        self.cash -= convertcash * self.dtcratio

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

    # # converts chips to cash
    # def chipstocash(self, amount):
    #     self.cash += amount * dtcratio
    #     self.chips = 0

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
                    if not self.conversionmode():
                        break
                else:
                    # suggest to sell organs in future
                    print('Filing bankruptcy!')
                    break


print(
'''
Welcome to the slot machine!
You can type exit at any time to leave the program.
'''
)

machine = SlotMachine()
machine.main()
