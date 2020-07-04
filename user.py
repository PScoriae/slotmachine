
class User:
    '''Setup for users playing games.'''
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.cash = 15000
        self.chips = 50

    def getFund(self):
        '''Prints user's current funds.'''
        if self.chips == 1:
            print(
f'''You now have 1 chip.
Your current balance is ${self.cash}.''')
        else:
            print(
f'''You now have {self.chips} chips.
Your current balance is ${self.cash}.
'''
)

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

def createUser():
    x = input('Enter your desired username: ')
