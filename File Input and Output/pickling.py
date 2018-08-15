# To utilize the Python pickling protocol, it must be imported
import pickle

sample_data = ('Scottie',
                'Richardson',
                '1991',
                ((1, 'Corvette Z06'),
                 (2, 'Audi R8'),
                 (3, 'Camero SS')))

even = list(range(0, 21, 2))
odd = list(range(1, 21, 2))
some_int = 4350069

# Pickling in Python is an extremely simple way to store many data
#   types and objects to binary data. Pickling can also store multiple
#   items within one file in the same "with as" function call
#######################################################################
######################## IMPORTANT TO REMEMBER ########################
#######################################################################
# When using the pickling method you have to remember that data must
#   be read back in the same order that it was written to the file, as
#   well as the fact that as of Python 3.7.0, which uses pickling
#   protocol 3 by default eventhough there is a protocol 4, the
#   different levels of the protocol are not backwards compatable. So
#   if working with older data, you will need the correct pickling
#   protocol to unpickle the data.
# You can designate the protocol to be used by giving adding the
#   protocol=# argument
# It is also very important to note that unpickling data from untrusted
#   sources is extremely discouraged due to the lack of security that
#   pickling offers.
#######################################################################
with open("File Input and Output\\sample_data.pickle", 'bw') as pickle_file:
    pickle.dump(sample_data, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)
    pickle.dump(even, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)
    pickle.dump(odd, pickle_file, protocol=1)
    pickle.dump(some_int, pickle_file, protocol=4)

with open("File Input and Output\\sample_data.pickle", 'br') as pickle_file:
    loaded_sample_data = pickle.load(pickle_file)
    loaded_even = pickle.load(pickle_file)
    loaded_odd = pickle.load(pickle_file)
    loaded_some_int = pickle.load(pickle_file)

print(loaded_sample_data)
print(loaded_even)
print(loaded_odd)
print(loaded_some_int)

first_name, last_name, birth_year, top_3_dream_cars = loaded_sample_data
print("\n" + ("=" * 50))
print("\tName:", end=" ")
print(first_name, end=" ")
print(last_name)
print("\tBorn:", end=" ")
print(birth_year)
print(("=" * 50)
       + "\n     {} {}'s Top Three Dream Cars\n".format(first_name, last_name)
       + ("=" * 50))
for car in top_3_dream_cars:
    car_rank, car_title = car
    print(car_rank, end=": ")
    print(car_title)
print("=" * 50, end="\n\n")

print("List of even integers from 0 to 20:", end=" ")
for i in even:
    print(i, end=" ")
print("")

print("List of odd integers from 0 to 20:", end=" ")
for i in odd:
    print(i, end=" ")
print("")

print("Random integer:", end=" ")
print(loaded_some_int, end="\n\n")
