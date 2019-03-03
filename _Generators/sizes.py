import sys


def my_range(n: int):
    print("my_range starts")
    start = 0
    while start < n:
        print("my_range is returning {}".format(start))
        yield start
        start += 1


# big_range = range(1000)
big_range = my_range(5)

print("big_range is {} bytes".format(sys.getsizeof(big_range)))

# Create a list containing all the values in big_range
big_list = []
for val in big_range:
    big_list.append(val)

print("big_list is {} bytes".format(sys.getsizeof(big_list)))

a = 2
b = 3
print("a is {}, b is {}".format(a,b))

# You can flip-flop numbers in python without the need for a temp variable
a,b = b,a
print("a is {}, b is {}".format(a,b))