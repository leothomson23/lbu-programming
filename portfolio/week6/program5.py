#!/usr/bin/env python3
if __name__ == "__main__":
    import string
    import random
    def encrypt(message):
        gap = random.randint(2, 20)
        letters = ''.join(random.choice(string.ascii_lowercase) for _ in range(gap - 1))
        encrypted = ''.join([letters + letter for letter in message])

        print('Original Message: ', message)
        print('Encrypted Message: ', encrypted)
        print('Interval: ', gap)

message = input('Enter a message you want to encrypt: ')
encrypt(message)

#Credits: https://pynative.com/python-generate-random-string/ 
