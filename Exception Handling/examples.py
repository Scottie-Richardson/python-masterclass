def factorial(n):
    # n! can also be defined as n * (n-1)!
    """ calculates n! recursively """
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

try:
    print(factorial(900))
# Looking at the documentation will give you an list of other possible errors that you can catch
#   through the 'except' ststment.
except (RecursionError, OverflowError):
    print("This program can't calculate factorials that large!")

print("Program terminating")
