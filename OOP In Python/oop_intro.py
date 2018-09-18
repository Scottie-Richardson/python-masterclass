# Create a new class
class Kettle(object):
    # Python class constructor uses __init__
    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True

    def switch_off(self):
        self.on = False

# Create an instance of Kettle class
kenwood = Kettle("Kenwood", 11.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 15.99
print(kenwood.price)

hamilton = Kettle("Hamilton", 18.99)

# Two different ways of accessing the data within a class
print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))
print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

# Call a class method
print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

# Use a class method by calling the class and passing it an object of
#   the same class type.
print(kenwood.on)
Kettle.switch_on(kenwood)
print(kenwood.on)
