######################################################################
#####                  READING FROM A TEXT FILE                  #####
######################################################################
# The 'r' designates that we are reading from the file
test_file = open('File Input and Output\\sample.txt', 'r')

for line in test_file:
    print(line, end="")

test_file.close()
# Unlike most languages it is not nessicary to test for the EOF (end of file)

print("#" * 50, end="\n\n")

# Another way to open a file in Python is using the with statment.
# When using the with statment python automatically closes the
# file when it reaches the end
with open('File Input and Output\\sample.txt', 'r') as test_file:
    for line in test_file:
        if "JABB" in line.upper():
            print(line, end="")

print('')
print("#" * 50, end="\n\n")

# You can also use the following methods on a file
#       Reads an individual character from a file
#           .read()

#       Reads an individual line from a file
#           .readline()

#       Reads ALL of the lines in a file
#           .readlines()

######################################################################
#####                   WRITING TO A TEXT FILE                   #####
######################################################################
games = ['Halo',
         'Call of Duty',
         'Need for Speed',
         'Destiny',
         'God of War']

# The 'w' designates that we are writing to the file
with open("File Input and Output\\games.txt", 'w') as games_file:
    for game in games:
        print(game, file=games_file)

# You can also manipulate files with the following commands
#================================================================================================
#||     Character     ||                                Meaning                                ||
#================================================================================================
#||        'r'	      ||     open for reading (default)                                        ||
#||        'w'        ||     open for writing, truncating the file first                       ||
#||        'x'        ||     open for exclusive creation, failing if the file already exists   ||
#||        'a'        ||     open for writing, appending to the end of the file if it exists   ||
#||        'b'        ||     binary mode                                                       ||
#||        't'        ||     text mode (default)                                               ||
#||        '+'        ||     open a disk file for updating (reading and writing)               ||
#||        'U'        ||     universal newlines mode (deprecated)                              ||
#================================================================================================