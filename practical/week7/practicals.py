if __name__ == "__main__":
    #Practical 1
    names = {"John", "Eric", "Terry", "Michael", "Graham", "Terry"}
    print(names)
    #It prints them in a random order, and only one 'Terry' item is printed.

    #Practical 2
    #names = set("John", "Eric", "Terry", "Michael", "Graham", "Terry")
    #print(names)
    #An error appears as iot only expected 1 argument, instead of the 6 that were entered.

    #Practical 3
    hex_letters1 = {"a", "b", "c", "d", "e", "f"}
    hex_letters2 = set("abcdef")
    print(hex_letters1)
    print(hex_letters2)

    #Practical 4
    sentence = "this is a sentence containing some letters"
    unique_letters = {x for x in sentence}
    print(unique_letters)

    #Practical 5
    unique_letters = {x for x in sentence if x != " "}
    print(unique_letters)
    #Prints the unique letters within a sentence, excluding the whitespaces.

    #Practical 6
    name = input("Enter your name: ")
    if name not in names:
        print("You are not listed in the set of known names")

    #Practical 7
    help(set)

    #Practical 8
    staff = {"Pete", "Kelly", "Jon", "Paul", "Sally", "Sue"}
    directors = {"Kelly", "Rupert", "Cyril", "Jon"}

    staff = staff.union({"Mark", "Ringo"})
    print(staff)

    staff_directors = staff.intersection(directors)
    print(staff_directors)

    external = directors.difference(staff)
    print(external)

    staff_or_external = staff.symmetric_difference(directors)
    print(staff_or_external)

    #Practical 9
    vowels = set({"a", "e", "i"})
    vowels.update("ou")
    print(vowels)

    #Practical 10
    staff = {"Pete", "Kelly", "Jon", "Paul", "Sally", "Sue"}
    managers = {"Kelly", "Jon", "Paul", "Sally", "Sue"}

    print(managers.issubset(staff))     # Checks if Managers is a subset of Staff
    print(managers.issuperset(staff))   # Checks if Managers is a superset of Staff

    #Practical 11
    help(frozenset)

    #Practical 12
    import math

    roots = {n: math.sqrt(n) for n in range(1, 26)}
    print(roots)

    #Practical 13
    stock = {"apple": 10, "banana": 15, "orange": 11}
    print("Apple stock level is", stock["apple"])

    stock["kiwi"] = 10
    print(stock)

    if "apple" in stock:
        print("Apples have a stock level")

    #Practical 14
    help(dict)

    #Practical 15
    stock.popitem()     #Removes the last item inserted into the list.
    print(stock)

    #Practical 16
    for item in stock:
        print(item)

    for item, level in stock.items():
        print(item, "has a stock level of", level)

    #Practical 17
    for num,sqrt in roots.items():
        print(f'The square root of {num} is {sqrt}')