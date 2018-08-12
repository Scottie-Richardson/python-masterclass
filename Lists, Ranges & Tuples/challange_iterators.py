# Create a list of items (you may use either strings or numbers in the list),
# then create an iterator using the iter() function.
#
# Use a for loop to loop "n" times, where n is the number of items in your list.
# Each time round the loop, use next() on your list to print the next item.
#
# hint: use the len() function rather than counting the number of items in the list.

string = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
n = 0
string_iterator = iter(string)

for char in iter(string):
    if n <= len(string):
        print(next(string_iterator))
        n += 1
    else:
        break

print('', end="\n\n")

# Or another solution is the following
string2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
string2_iterator = iter(string2)

for char in range(0, len(string2)):
    print(next(string2_iterator))
