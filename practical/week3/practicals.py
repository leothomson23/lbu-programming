if __name__ == "__main__":
    #Practical 1
    print(10 < 100)
    print(100 != 100)
    print (50 >= 50)
    print("\n")

    #Practical 2
    age = 18
    if age > 18:
        print("Your age is larger than 18")
    elif age == 18:
        print("Your name is equal to 18")
    else:
        print("Your age is smaller than 18.")

    if age > 21:
        print("Your age is larger than 21")
    elif age == 21:
        print("Your name is equal to 21")
    else:
        print("Your age is smaller than 21.")

    if age > 31:
        print("Your age is larger than 31")
    elif age == 31:
        print("Your name is equal to 31")
    else:
        print("Your age is smaller than 31.")
    print("\n")

    #Practical 3
    print("a" < "b")
    print("b" < "a")
    print("John" < "Terry")
    print("\n")

    #Practical 4
    print("john" < "Terry")
    print("\n")

    #Practial 5
    print(5 < 10.2)
    #print(5 < "Monty")    - ends in error due to incompatible data-types
    #print(5 < "5")     - ends in error due to incompatible data-types
    print("\n")

    #Practical 6
    age = 30
    print(age >=18 and age <=65)
    print(age <18 or age >65)
    print(not age > 18)
    print("\n")

    #Practical 7
    print((age >=18 and age <=65) and (not age==30))
    print("\n")

    #Practical 8
    weight = 50
    height = 150
    print(100 < weight and weight < 200)
    print(height > 131 and height < 160)
    print("\n")

    #Practical 9
    names = ["Terry", "John", "Michael", "Eric", "Terry", "Graham"]
    if "John" in names:
        print("John is in the list.")
    else:
        print("John is not in the list")

    if "Brian" in names:
        print("Brian is in the list")
    else:
        print("Brian is not in the list")
    print("\n")

    #Practical 10, 11 & 12
    age_input = int(input("What is your age?"))
    if age_input > 100:
        print("you are very old,")
        print("well done!")
    elif age_input > 80:
        print("you are fairly old")
        print("pretty good!")
    elif 29 < age_input < 40:
        print("You are aged between 30 and 40")
    else:
        print("you are not very old - yet")
    print("\n")

    #Practical 13
    name = input("Please enter your name:")
    if name:
        print("Hi,", name)
    else:
        print("You haven't entered anything!")
    print("\n")

    #Practical 14
    print("You are an adult!" if age>= 18 else "You are not an adult, yet!")
    print("\n")

    #Practical 15
    for n in names:
        print(n)
    print("\n")

    #Practical 15
    for n in range(2, 12, 2):
        print(n, "to the power of", n, "is", n**n)
    print("\n")

    #Practical 16, 17 & 18
    numbers = [10, 20 , 30, 90, 200, 30, 22, 11]
    total = 0
    for number in numbers:
        if total > 100:
            break
        else:
            total = total + number
            print(total)
            continue
    print("\n")