if __name__ == "__main__":
    #Practical 1
    total = 100
    print("The total is", total)

    #Practical 2
    total = total + 99
    print("The total is now", total)

    #Practical 3
    total -= 1
    print("The total is", total)

    total *= 4
    print("The total is", total)

    total /= 2
    print("The total is", total)

    #Practical 4
    total = 98.2
    count = 5

    average = total / count

    #Practical 5
    print(type(False))
    print(type(1000))
    print(type(100.111))
    print(type("Hello"))
    print(type(True))
    print(type(100/5))
    print(type(100//5))

    #Practical 6
    print("ABC" * 10)

    #Practical 7
    name = 'Leo Thomson'
    address =  'Carnegie Village'
    print(name * 10)
    print(address * 10)
    print('Your name has ', len(name), 'characters in it')

    #Practical 8
    name = input("What's your name? ")
    print("Hello there", name)

    #Practical 9
    no1 = int(input("Enter your first number: "))
    no2 = int(input("Enter your second number: "))
    print("Your numbers multiplied are: ", no1 * no2)

    #Practical 10
    print("This text includes characters such as \'\\\' \'\"\' and \"\'\",\n\t This is a new line which starts with a tab\n\t\t This new line starts with two tabs.")

    #Practical 11
    print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\nHello There!\n\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")

    #Practical 12
    print("This text spans three lines,")
    print("and includes both single ('),")
    print('and double (") quotes.')

    #Practical 13
    surname = "Palin"
    initial = surname[2]
    print(initial)

    #Practical 14
    #surname = "Palin"
    #initial = surname[10]
    #print(initial)
    #Made as a comment to avoid errors while running program.

    #Practical 15
    initial = surname[-2]
    print(initial)

    #Practical 16
    end = surname[1:]
    print(end)

    #Practical 17
    end = surname[:-1]
    print(end)

    #Practical 18
    primes = [2, 3, 5, 7, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    print(primes[0:4])

    #Practical 19
    names = ["Terry", "John", "Michael", "Eric"]
    names[-2] = "Tim", "Bill"
    print(names)

    #Practical 20
    nums = [1,2,3] * 5
    print(nums * 5)