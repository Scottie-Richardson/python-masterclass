# Generates an infinite series of odd numbers
def odds():
    n = 1
    while True:
        yield n
        n += 2


def pi_series():
        odd_nums = odds()
        approximation = 0
        while True:
                approximation += (4 / next(odd_nums))
                yield approximation
                approximation -= (4 / next(odd_nums))
                yield approximation

approx_pi = pi_series()

# The higher the range used here the closer to an acurate approximation of PI.
for x in range(10000):
        print(next(approx_pi))

