#!/usr/bin/env python3
if __name__ == "__main__":
    from statistics import mean
    import sys

    def conversion(values):
        if values == "":
            print("No temperatures entered.")
            return
        else:
            print("Maximum Temperature: ", max(values), "C", sep='')
            print("Minimum Temperature: ", min(values), "C", sep='')
            print("Average Temperature: ", mean(values), "C", sep='')

    values = sys.argv[1:]
    conversion(values)
