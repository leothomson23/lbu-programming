#!/usr/bin/env python3
if __name__ == "__main__":
    def conversion(num):
        if num < 0:
            print('Value must be positive.')
        else:
            print(num, 'converted to binary is', bin(num)[2:])

    value = int(input('Enter a value: '))
    binary = conversion(value)

