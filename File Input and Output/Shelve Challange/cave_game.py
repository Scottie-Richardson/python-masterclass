import shelve

with shelve.open('File Input and Output\\Shelve Challange\\cave_shelve') as cave:
    loc = 1
    while True:
        availableExits = ", ".join(cave['locations'][loc]["exits"].keys())

        print(cave['locations'][loc]["desc"])

        if loc == 0:
            break
        else:
            allExits = cave['locations'][loc]["exits"].copy()
            allExits.update(cave['locations'][loc]["namedExits"])

        direction = input("Choose a direction. Available exits are " + availableExits + ": ").upper()
        print()

        # Parse the user input, using our vocabulary dictionary if necessary
        if len(direction) > 1:  # more than 1 letter, so check vocab
            words = direction.split()
            for word in words:
                if word in cave['vocab']:   # does it contain a word we know?
                    direction = cave['vocab'][word]
                    break

        if direction in allExits:
            loc = allExits[direction]
        else:
            print("You cannot go in that direction")