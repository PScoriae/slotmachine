import json


class User:
    '''Setup for users playing games.'''
    def __init__(self, cash, chips):
        self.cash = cash
        self.chips = chips

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

    def updateInfo(self):
        '''Updates the current user's information into the database.'''
        userDB[self.username] = {'username': self.username,
        'password': self.password, 'cash': self.cash, 'chips': self.chips,}

class Admin:
    '''Subclass of User with admin priveliges.'''
    def __init__(self, username, password):
        super().__init__(self, username, password)

    def setChips(self):
        while True:
            try:
                x = input('Enter desired amount of chips: ')
                self.chips = x
                break
            except:
                print('I do not understand.')
