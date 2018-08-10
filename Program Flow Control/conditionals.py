name = input("Please enter your name: ")
age = int(input("How old are you {0}? ".format(name)))

# This can also be written as:
# if age >= 18 and age < 65:
# Or as:
# if 18 >= age < 65:
if not(18 < age > 65):
    print("You are old enough to vote")
elif age >= 65:
    print("You are old enough to retire")
elif age < 18:
    print("Please come back in {0} years {1}.".format((18 - age), name))
