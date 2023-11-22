#!/usr/bin/env python3
if __name__ == "__main__":
    def celstofah(temp):
        print(temp, "C is equivalent to",(temp * 9/5)+32, "F")

    def fahtocels(temp):
        print(temp, "F is equivalent to",((temp - 32)*5)/9, "F")

    temp = int(input("Enter a temperature: "))
    celstofah(temp)
    fahtocels(temp)