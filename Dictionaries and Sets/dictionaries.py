# Dictionaries are also imutable objects in python,
#   but they cannot be accessed by index number.
#   Instead, you access the information via a "key"
textbooks = {"Algorithms": "Introduction to Algorithms",
            "Database Design": "Database Managment Systems",
            "Differential Equations": "Fundamentals of Differential Equations",
            "Automata and Computability": "Automata, Computability and Complexity"}

print(textbooks)
print("")
print("*" * 50, end="\n\n")

print(textbooks["Algorithms"])
print(textbooks["Database Design"])
print(textbooks["Differential Equations"])
print(textbooks["Automata and Computability"])

# To update a value in a dictionary or add a new element
#   you simply refer to the key and give it a value
print("")
print("*" * 50, end="\n\n")
textbooks["Linear Algebra"] = "Linear Algebra for Dummies"
print("Newly created item is: {}".format(textbooks["Linear Algebra"]))
textbooks["Linear Algebra"] = "Linear Algebra and its Applications"
print("Updated item is: {}".format(textbooks["Linear Algebra"]))
print("")
print("*" * 50, end="\n\n")

# To delete an entry from a dictionary you use the del command,
#   dictionary name and key of the entry you want to delete.
#   You can also remove an entire dictionary if you do not specify
#   the key of an item to delete. Finally if you wanted to retain
#   a dictionary, but wipe out all the data it contains,
#   you can use the .clear() method
del textbooks["Linear Algebra"]
print(textbooks)
textbooks.clear()
print(textbooks)
del textbooks
# This next line will cause an error because the textbooks dictionary no longer exists
# print(textbooks)

# The ordering of a dictionary is random and changes each time the program is run

# Dictionaries also have built in functions that return a "list-like" object for
#   either the keys or values via .keys() or .values()

# Another built in function is .items() which returns a "tuple-like" object

# Using these functions in combination with the functions for lists and tuples
#   you can shift between different structures as nessicary, for example:
print("*" * 50, end="\n\n")

textbooks = {"Algorithms": "Introduction to Algorithms",
            "Database Design": "Database Managment Systems",
            "Differential Equations": "Fundamentals of Differential Equations",
            "Automata and Computability": "Automata, Computability and Complexity",
            "Linear Algebra": "Linear Algebra and its Applications"}

list_of_keys = list(textbooks.keys())
print("This is a list of the dictionary keys")
print(list_of_keys, end="\n\n")

list_of_values = list(textbooks.values())
print("This is a list of the dictionary values")
print(list_of_values, end="\n\n")

tuple_of_textbooks = tuple(textbooks.items())
print("This is a tuple of the dictionary's key-value pairs")
print(tuple_of_textbooks, end="\n\n")

dictionary_of_textbooks_tuple = dict(tuple_of_textbooks)
print("This is a dictionary created from the textbooks tuple")
print(dictionary_of_textbooks_tuple, end="\n\n")

# When combining of concatinating ANY sequence type data you can use the .join() method
#   In the instances where you are using imutable data, the join method is much more efficent
#   For example:
letters = "abcdefghijklmnopqrstuvwxyz"
new_string = ", ".join(letters)
print(new_string)

# To combine two dictionaries you can use the .update() method
example_dictionary = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e"}
print("*" * 50, end="\n\n")
print(example_dictionary)
example_dictionary.update(textbooks)
print(example_dictionary)

# To create a new dictionary that contains all of the information from a dictionary
#   without changing it, you can use the .copy() method
example_dictionary = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e"}
example_dictionary_2 = example_dictionary.copy()
example_dictionary_2.update(textbooks)
print("\n\nThis is a new dictionary where neither of the origional dictionaries were changed: ")
print(example_dictionary_2, end="\n\n")