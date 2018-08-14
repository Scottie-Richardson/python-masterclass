# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
#
# You can either enter the text from the keyboard or
# initialise a string variable with the string.

user_input = input("Please enter some text: ")

input_set = set(user_input)
vowels_set = frozenset('aeiou ')

input_set.difference_update(vowels_set)
print(sorted(input_set))