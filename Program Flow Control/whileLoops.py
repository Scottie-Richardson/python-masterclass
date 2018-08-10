import random

corrertNumber = random.randint(0, 100)
guessedNumber = 0

print("Guess a number between 0 and 100: ")

while guessedNumber != corrertNumber:
    inputNumber = input()
    if inputNumber == 'quit':
        break

    guessedNumber = int(inputNumber)

    if (guessedNumber < 0) or (guessedNumber > 100):
        print("Not a valid input, try again!", end='\n\n')
        continue
    elif guessedNumber > corrertNumber:
        print("Lower!", end='\n\n')
    elif guessedNumber < corrertNumber:
        print("Higher!", end='\n\n')

else:
    print("You got It!")
