# Write a small program to ask for a name and an age.
# When both values have been entered, check if the person
# is the right age to go on an 18-30 holiday (they must be
# over 18 and under 31).
# If they are, welcome them to the holiday, otherwise print
# a (polite) message refusing them entry.

name = input("Please enter your name: ")
age = int(input("How old are you {0}? ".format(name)))

if 18 <= age <= 30:
  print("Welcome to the holiday {0}".format(name))
else:
  print("Sorry {0}, you must be between 18 and 30 to participate in this holiday.".format(name))