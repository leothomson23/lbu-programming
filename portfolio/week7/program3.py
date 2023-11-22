#!/usr/bin/env python3
if __name__ == "__main__":
    def countries_and_capitals():
        list = {'england':'London', 'scotland':'Edinburgh', 'wales':'Cardiff', 'spain':'Madrid', 'germany':'Munich'}

        while True:
            entry = input('Enter a country name: ')
            entry = entry.lower()

            if entry == '':
                break

            if entry.lower() in list:
                print('The capital of', entry.capitalize(), 'is', list[entry])
            else:
                capital = input('Please enter the capital of ' + entry.capitalize())
                list[entry] = capital
                print('Added to the list.')

    countries_and_capitals()


