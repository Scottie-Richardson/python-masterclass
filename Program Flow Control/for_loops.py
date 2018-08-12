# Print all numbers from 0 to 9
for i in range(0, 10):
    print(i, end=" ")
print('', end='\n\n')

# Print all the numbers from 0 to 100 in increments of 10
for i in range(0, 101, 10):
    if i < 100:
        print(i, end=", ")
    else:
        print(i, end="\n\n")

# Print the 4 different strings
for state in ['up high', 'to the side', 'down low', 'too slow']:
    if state != "too slow":
        print(state, end=', ')
    else:
        print(state, end="\n\n")

# Print a multiplication table for 1 to 10
for i in range(1, 11):
    for j in range(1, 11):
        print("{0:2} x {1:2} is {2:<3}".format(i, j, i*j), end='  |  ')
    print('')
print('')

# Use a for loop and an if statement to print just the capitals in the quote.
quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

for cap in quote:
    if cap in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        print(cap, end=" ")
print('', end="\n\n")

# Print all numbers divisible by 7 from 0 to 100
for i in range(0, 101):
    if (i % 7) == 0:
        print(i, end=" ")
print('', end='\n\n')

# Use continue, break and else to skip items being itterated over or exit the loop
foodItems = ["egg", "bacon", "spam", "cheese"]
nasty_food_item = ''

for item in foodItems:
    if item == 'spam':
        continue
    print("Buy " + item)

for item in foodItems:
    if item == 'spam':
        nasty_food_item = item
        break
else:
    print("I will have that please!")

if nasty_food_item == 'spam':
    print("Can I please have something without spam?")
