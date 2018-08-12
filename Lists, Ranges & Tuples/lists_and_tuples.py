# Create an empty list without constructor
list_1 = []

# Create an empty list with list constructor
list_2 = list()

# Both empty lists are equivalent
if list_1 == list_2:
    print("Lists are equal", end="\n\n")

# If you directly assign one list to another, they are the same list.
#   Meaning that the second list referes to the same list in memory,
#   and any operation done on one is done to both.
even = [2, 4, 6, 8]
duplicate_even = even
if duplicate_even is even:
    print("The two variables point to the same location in memory.")
else:
    print("The two variables do not point to the same location in memory.")
print(even)
duplicate_even.sort(reverse=True)
print(even, end="\n\n")

# To assign one list to another without pointing to the same variable
#   in memory, pass the list through the list constructor
odd = [1, 3, 5, 7, 9]
duplicate_odd = list(odd)
if duplicate_odd is odd:
    print("The two variables point to the same location in memory.")
else:
    print("The two variables do not point to the same location in memory.")
print(odd)
duplicate_odd.sort(reverse=True)
print(odd, end="\n\n")


################################################################################
################################################################################
#                                    TUPLES                                    #
################################################################################
################################################################################
# Tuples are imutable objects meaning that they cannot be changed by referencing
#   an index and assigning it a value, in order to change the actual value within
#   a tuple, you must recreate the entire tuple
example_tuple = ("a", 15, "bike", 19.5)
print(example_tuple)

# This will cause an error
# example_tuple[2] = "car"

# To correctly change the value:
example_tuple = example_tuple[0], example_tuple[1], "car", example_tuple[3]
print(example_tuple)

# You can also "unpack" a tuple in the following way
brand, year, vehicle_type, mpg = example_tuple
print(brand)
print(year)
print(vehicle_type)
print(mpg)