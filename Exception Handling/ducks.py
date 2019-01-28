# This is a reiteration of an earlier file that utilizes type hints for the function definition at
#       line 60.

class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Weee, this is fun")
        elif self.ratio == 1:
            print("This is hard work, but I'm flying")
        else:
            print("I think I'll just walk")


class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print("Waddle, waddle, waddle")

    def swim(self):
        print("Come on it, the water's lovely")

    def quack(self):
        print("Quack quack")

    def fly(self):
        self._wing.fly()


class Penguin(object):

    def walk(self):
        print("Waddle, waddle, I waddle too")

    def swim(self):
        print("Come on in, but it's a bit chilly this far South")

    def quack(self):
        print("Are you 'avin' a larf? I'm a penguin!")


class Flock(object):

    def __init__(self):
        self.flock = []

    # This provides the type hint if someone else were to use your function of what data type is
    #       expected and what output is expected.
    # You can also check the type of an object using type(objectName) which returns the exact type
    #       of the object. This will not identify if the object being passed is a subclass however.
    #       To check if the object is a certain type or a subclass of that type we can use
    #       isinstance(objectName, TypeName).

    def add_duck(self, duck: Duck) -> None:
        fly_method = getattr(duck, 'fly', None)
        if callable(fly_method):
            self.flock.append(duck)
        else:
            raise TypeError("Cannot add duck, are you sure it isn't a " + str(type(duck).__name__))

    # Another way to perform a check is:
    #   def add_duck(self, duck: Duck) -> None:
    #       if isinstance(duck, Duck):
    #           self.flock.append(duck)

    def migrate(self):
        problem = None
        for duck in self.flock:
            try:
                duck.fly()
            except AttributeError as e:
                print('One duck down')
                problem = e
                # raise
        if problem:
            raise problem

if __name__ == '__main__':
    donald = Duck()
    donald.fly()


