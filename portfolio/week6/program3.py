if __name__ == "__main__":
    def prime(num):
        if num > 1:
            for x in range(2, num):
                if (num % x) == 0:
                    print(num, "is not a prime number")
                    break
        else:
            print(num, "is a prime number")

    num = int(input('Enter a number: '))
    prime(num)