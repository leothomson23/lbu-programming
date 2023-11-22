#!/usr/bin/env python3
if __name__ == "__main__":
    temp = input("Enter a temperature: ")
    temp = int(temp [:-1])
    conversion = (temp * 9/5)+32

    print(temp, "C is equivalent to ", conversion, "F", sep='')