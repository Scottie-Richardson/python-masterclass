import os


def fact(n):
    # Calculate n! iteratively
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result


def factorial(n):
    # Calculate n! recursively
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


for i in range(6):
    print(i, factorial(i))
    print(i, fact(i))


def list_directories(s):
    def dir_list(d):
        # The nonlocal keyword allows you to use variables outside the
        #   scope of the current function while still not having to
        #   create a global variable and it must be created within
        #   the enclosing scope
        nonlocal tab_stop
        files = os.listdir(d)
        for f in files:
            current_dir = os.path.join(d, f)
            if os.path.isdir(current_dir):
                print("\t" * tab_stop + "Directory " + f)
                tab_stop += 1
                dir_list(current_dir)
                tab_stop -= 1
            else:
                print("\t" * tab_stop + f)

    tab_stop = 0
    if os.path.exists(s):
        print("Directory listing of " + s)
        dir_list(s)
    else:
        print(s + " does not exist!")

listing = os.walk('.')
print(listing)
# Unformatted output of file listings
for root, directories, files in listing:
    print(root)
    for d in directories:
        print(d)
    for file in files:
        print(file)

# Formatted file listing output
test_path = "C:"
list_directories(test_path)