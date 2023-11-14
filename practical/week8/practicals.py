if __name__ == "__main__":
    #Practical 1
    name = 'Donald'
    addr = '1600 Pennsylvania Ave.'
    print(f"Your name is {name}, and your address is {addr}")

    #Practical 2 & 3
    width = 104.32
    height = 15.654
    print(f'The area of a rectangle with a width of {width} and a height of {height} is {width * height:.3f}')

    #Practical 4
    age = 45
    print(f"{name:15} - {age:10}")
    print(f"{name:15} - {age:10}")
    print(f"{name:15} - {age:10}")

    print(f"{name:>15} - {age:10}")
    print(f"{name:^15} - {age:^10}")
    print(f"{name:@^15} - {age:#^10}")

    #Practical 5
    print(f"{name:$>20} - {age:$>20}")

    #Practical 6
    print("Your name is {}, and your address is {}".format(name, addr))
    print("Your name is {1}, and your address is {0}".format(addr, name))
    print("Your name is {id}, and your address is {0}".format(addr, id=name))

    #Practical 7
    from math import pi
    r = 52
    area = pi * r * r
    print('A circle with radius {} has an area of {area}'.format(r, area=area))

    #Practical 8
    print('{:@^15} - {:#^10}'.format(name, age))

    #Practical 9
    file = open("info.txt")
    contents = file.read()
    print(contents)
    file.close()

    #Practical 10
    file = open("info.txt")
    line1 = file.readline()
    line2 = file.readline()
    line3 = file.readline()
    print(line1)
    print(line2)
    print(line3)
    file.close()

    #Practical 11
    file = open("info.txt")
    for line in file:
        print(line)
    file.close()

    #Practical 12
    file = open("info.txt", "a")
    file.write("\nThis is an extra line.")
    file.close()

    #Practical 13
    with open('info.txt', 'r') as file:
        for line in file:
            print(line)