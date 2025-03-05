print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 1:
        print('that is alot of cats')
    else:
        print('that is not many cats')
except ValueError:
    print('you did not enter a number')
