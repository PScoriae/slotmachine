import random
import string

# add feature, user input determines number of slotchoices
# probability = input('How many possible alphanumerics would you like? ')

# # 4 column version
# flag = True
#
# while flag:
#     slotchoices = ['A', '7', 'X', '5']
#     repetitions = len(slotchoices)
#     fourmatch = '$1000'
#     threematch = '$500'
#     twopair = '$100'
#     onepair = '$10'
#     counter = 0
#     paircounter = 0
#     result = []
#
#     # selects randomized choices from slotchoices and appends to result
#     for x in range(4):
#         z = random.randint(0, repetitions - 1)
#         single = slotchoices[z]
#         result.append(single)
#
#     calc = result[:]
#
#     # creates list for comparison to calculate winnings
#     for y in calc:
#         while calc.count(y) > 1:
#             calc.remove(y)
#     print(' '.join(result))
#
#     # calculates winnings
#     if len(calc) == 4:  # checks if all rolls are different
#         print('Loser')
#
#     for item in calc:
#         if result.count(item) == 4:
#             print(f'4 matches! You won {fourmatch}!')
#             break
#         elif result.count(item) == 3:
#             print(f'3 matches! You won {threematch}!')
#             break
#         elif result.count(item) == 2:
#             paircounter += 1
#         if item == calc[-1]:
#             if paircounter == 2:
#                 print(f'2 pairs! You won {twopair}!')
#             elif paircounter == 1:
#                 print(f'1 pair! You won {onepair}')
#
#     # determines if user would like to continue playing
#     question = input('Would you like to try again?(Y/n) ')
#     if question.lower() == 'y' or not question:
#         continue
#     else:
#         flag = False


# 3 column version
flag = True
money = 100

while flag:
    slotchoices = ['A', '7', 'X', '5']
    repetitions = len(slotchoices)
    fourmatch = '$1000'
    threematch = '$500'
    twopair = '$100'
    onepair = '$10'
    counter = 0
    paircounter = 0
    result = []

    # selects randomized choices from slotchoices and appends to result
    for x in range(3):
        z = random.randint(0, repetitions - 1)
        single = slotchoices[z]
        result.append(single)

    calc = result[:]

    # creates list for comparison to calculate winnings
    for y in calc:
        while calc.count(y) > 1:
            calc.remove(y)
    print(' '.join(result))

    # calculates winnings
    for item in calc:
        if result.count(item) == 3:
            print(f'3 matches! You won {threematch}!')
            break
        elif result.count(item) == 2:
            print(f'2 matches! You won {onepair}!')
            break
        elif result.count(item) == 1:
            counter += 1
            if counter == 3:
                print('Loser.')

    # determines if user would like to continue playing
    question = input('Would you like to try again?(Y/n) ')
    if question.lower() == 'y' or not question:
        continue
    else:
        flag = False
