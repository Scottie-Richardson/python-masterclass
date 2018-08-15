import shelve

# You can also open and close a shelve yourself instead of using the
#   "with as" function. Shelves do not completely overwrite previous
#   versions when ran multiple times as the binary or pickling
#   methods did. Instead it persists and simply continues to add
#   data to the shelve file if it does not already exist within the file
with shelve.open('File Input and Output\\sample_shelve') as courses:
    courses['Algorithms'] = "Introduction to Algorithms"
    courses['Database Design'] = "Database Managment Systems"
    courses['Differential Equations'] = "Fundamentals of Differential Equations"
    courses['Automata and Computability'] = "Automata, Computability and Complexity"
    courses['Linear Algebra'] = "Linear Algebra and its Applications"

    print(courses['Algorithms'])
    print(courses['Database Design'])

print(courses)

# Other than the way a shelve is created and utilized, it behaves almost
#   identically with a dictionary data structure other than the fact that
#                       A SHELVE KEY MUST BE A STRING,
#   where a dictionary could be a variety of data types.

# When updating values in a shelve you have to reassign that value explicitly.
#   For example using the .append() method if working with a mutable item will
#   not actually update the shelve unless you specify writeback=True when you
#   initially open the shelve, however when dealing with large amounts of data
#   this could be very costly for the system memory to accomplish. Instead it
#   would be much more efficent to explicitly update the data that has actually
#   changed via a temp variable.
