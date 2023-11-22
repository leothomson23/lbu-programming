#!/usr/bin/env python3
if __name__ == "__main__":
    def factors(value):
        if value <= 0:
            print('Value must be positive.')

        factors = []
        for num in range(1, value + 1):
            if value % num == 0:
                factors.append(num)
        print('The factors of ', value, 'are', factors)

    value = int(input('Enter a value: '))
    factors(value)