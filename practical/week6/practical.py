if __name__ == "__main__":
    import math
    #Practical 1
    squares = [4, 9, 16, 25]

    for x in range(len(squares)):
        square = squares[x]
        square_root = math.sqrt(square)
        print("The square root of", squares[x], "is", math.sqrt(square))

    #Practical 2
    squares.append(49)
    squares.append(64)
    squares.append(81)
    print(squares)

    #Practical 3
    squares.extend([x * x for x in range(11,14)])
    print(squares)

    #Practical 4
    squares.insert(0, 2)
    print(squares)

    #Practical 5
    squares.remove(49)
    print(squares)

    #Practical 6
    #squares.remove(3)
    #print(squares)
    #Added as note to prevent error apearing throughout later exercises.

    #Practical 7
    num = [1, 2, 3, 1, 2]
    num.remove(2)
    print(num)

    #Practical 8
    squares.pop()
    print(squares)

    #Practical 9
    squares.pop(0)
    print(squares)

    #Practical 10
    names = [ "Eric", "anna", "Sophie", "sam" ]
    names.sort()
    print(names)

    #Practical 11
    names.sort(key=lambda name : name.upper())
    print(names)

    #Practical 12
    squares.reverse()
    print(squares)

    #Practical 13
    colours = ["red", "green", "yellow", "blue", "red"]
    print(colours.index("blue"))

    #Practical 14
    colours_new = colours.copy()
    colours.extend(["purple", "orange", "beige"])
    print(colours)
    print(colours_new)

    #Practical 15
    cubes = [x * x * x for x in range(2,21)]
    print(cubes)

    #Practical 16
    all_users = ['hellothere', 'hello']
    some_users = [u for u in all_users if len(u) < 8]
    print(some_users)
    #Only includes those who haev usernames less than 8 characters.

    #Practical 17
    address = (3, 'Wharfe', 'LS6 3GZ')

    #Practical 18
    me1 = ('Leo'),
    me2 = ('Leo')
    print(type(me1)) #Returns as a tuple
    print(type(me2)) #Returns as a string

    #Practical 19
    houseno, streetname, postcode = address
    print(houseno)
    print(streetname)
    print(postcode)

    #Practical 20
    print(*address) # Prints them line by line depending on the variables they have all been assigned.
    print(address) # Print them all on one line in the form of a tuple.


