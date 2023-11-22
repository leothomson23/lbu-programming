#!/usr/bin/env python3
if __name__ == "__main__":
    g1 = 113
    g2 = 175
    g3= 12

    total = g1+g2+g3

    fullgroups = total//24
    remainder = total%24

    print("There will be ", fullgroups, " full groups.")
    print("There will be a smaller group of ", remainder, " students.")