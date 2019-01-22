import sys

def getint(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Invalid number entered, please try again.")
        except EOFError:
            sys.exit(1)
        finally:
                print("The 'finally' clause will always execute.")

first_number = getint("Please enter first number: ")
second_number = getint("Please enter second number: ")

try:
    print("{} divided by {} is {}".format(first_number, second_number, first_number / second_number))
except ZeroDivisionError:
    print("You can't divide by zero!")
    sys.exit(2)
# The 'else' clause will execute if there were no exceptions thrown
else:
    print("Division performed successfully!")

