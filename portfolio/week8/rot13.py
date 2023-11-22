#!/usr/bin/env python3
def rot13(phrase):
    key = "abcdefghijklmnopqrstuvwxyz"
    value = "nopqrstuvwxyzabcdefghijklm"
    cypher = dict(zip(key, value))
    output = ''

    for letter in phrase:
        output += str(cypher[letter])

    print(phrase, 'converts to', output)

if __name__ == "__main__":
	phrase = input('Enter a phrase to convert: ')
	rot13(phrase)