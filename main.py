import json
from slotmachine import SlotMachine
from user import User, Admin


def loadData():
    '''Attempts to load userDB.'''
    try:
        filename = 'userDB.json'
        with open(filename) as f:
            userDB = json.load(f)
    except FileNotFoundError:
        userDB = {}
        print(f'{filename} does not exist!\nCreating user database.')
        filename = 'userDB.json'
        with open(filename, 'w') as f:
            json.dump(userDB, f)
    else:
        print('User data loaded.')
    return userDB

def saveData(database):
    db = database
    filename = 'userDB.json'
    with open(filename, 'w') as f:
        json.dump(db, f)
    print('User data saved.')

def newUser(database):
    '''Makes a new account for the user.'''
    db = database
    while True:
        username = str(input('Enter your desired username: '))
        if not username.isalnum():
            print('Alphanumerics only.')
            continue
        pw = str(input('Enter your desired password: '))
        if not pw.isalnum():
            print('Alphanumerics only.')
            continue
        else:
            break
    if username not in userDB.keys():
        db[username]['pw'] = pw
        db[username]['chips'] = 50
        db[username]['cash'] = 15000
        saveData(db)
        print(f'You are now registered as {username}!\nRedirecting to login screen.')
        login(db)
    else:
        print('Sorry, that username is taken.')
        return newUser()

def login(db):
    '''Attempts to log in user.'''
    username = str(input('Enter your username: '))
    password = str(input('Enter your password: '))
    if username not in userDB:
        print('No such username registered.')
        return login()
    elif password == userDB[username]['pw']:
        print(f'Welcome back, {username}!')
        return username
    else:
        print('Incorrect password.')
        return login()

def logOrNew(db):
    '''Asks if the user would like to log in or make a new account.'''
    x = str(input("To log in, enter: 1\nTo make a new account, enter: 2\n"))
    if x == '1':
        return login(db)
    elif x == '2':
        newUser(db)
    else:
        print('I do not understand. Please try again.')
        return logOrNew(db)


userDB = loadData()
username = logOrNew(userDB)
# print(userDB[username]['chips'])
playerChips, playerCash = userDB[username]['chips'], userDB[username]['cash']
player = User(playerCash, playerChips)
machine = SlotMachine(player)
machine.main(player)
