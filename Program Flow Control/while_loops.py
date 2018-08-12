import random

correct_number = random.randint(0, 100)
guessed_number = 0

print("Guess a number between 0 and 100: ")

while guessed_number != correct_number:
    input_number = input()
    if input_number == 'quit':
        break

    guessed_number = int(input_number)

    if (guessed_number < 0) or (guessed_number > 100):
        print("Not a valid input, try again!", end='\n\n')
        continue
    elif guessed_number > correct_number:
        print("Lower!", end='\n\n')
    elif guessed_number < correct_number:
        print("Higher!", end='\n\n')

else:
    print("You got It!")
