if __name__ == "__main__":
    #Practical 1
    import math
    print(math.sqrt(2401))

    #Practical 2
    from math import log2
    print(log2(1024))

    #Practical 3
    def displayTwice(msg):
        """Repeats the message twice"""
        print(msg)
        print(msg)

    msg = "Hello World!"
    displayTwice(msg)

    #Practical 4
    help(displayTwice)

    #Practical 5
    def findMax(a,b):
        """Finds the maximum of two values."""
        if ( a > b ):
            max = a
        else:
            max = b
        return max
    a = 5
    b = 6

    print(findMax(a,b))

    #Practical 6
    def multiplyNum(no1, no2=0):
        if no2==0:
            print(num1*num1)
        else:
            print(num1*num2)

    num1 = 5
    num2 = 2
    print(multiplyNum(num1, num2))
    print(multiplyNum(num1))

    #Practical 7
    def someFunc(x, y, z):
        print("x is", x, "\ny is", y, "\nz is", z)


    someFunc(1, 2, 3)
    someFunc(3, 2, 1)

    #Practical 8
    name = "Brian"
    print("Hello!", name, "How are you today?", sep='555')
    print("Hello!", name, "How are you today?", sep='!!!')

    #Practical 9
    def calcAve(*numbers):
        total = 0
        for num in numbers:
            total += num
        return total/len(numbers)

    print(calcAve(5, 5, 60, 90))

    #Practical 10
    hypot = lambda a,b : math.sqrt(a * a + b * b)

    print(type(hypot))