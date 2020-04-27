import random

attempts = 0

print('Hi, type your name please. ')

name = raw_input()
x = random.randint(0,10)

print('Well, ' + name + ', i am thinking a number between 0 and 10.')

while attempts < 3:
    print('Try to guess, type a number.') 
    trys = raw_input()
    trys = int(trys)
    attempts = attempts + 1
    if trys < x:
        print('Your number is too low.')
    if trys > x:
        print('Your number is too high.')
    if trys == x:
        break
if trys == x:
    attempts = str(attempts)
    print('Well done ' + name + ', that is the right number.')
if trys != x:
    x = str(x)
    print('No, sorry. The number i was thinking was ' + x)

