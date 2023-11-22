#!/usr/bin/env python3
if __name__ == "__main__":
    def decrypt(message, interval):
        print('Your message decrypted would be: ',message[interval - 1::interval])
    message = input('Enter the message you want to decrypt: ')
    interval = int(input('Enter the interval: '))

    decrypt(message, interval)