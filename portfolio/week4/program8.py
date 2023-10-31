if __name__ == "__main__":
    from statistics import mean

    values = []

    while True:
        entry = input("Enter a temperature: ")
        if entry == "":
            print("\n")
            print("Maximum Temperature: ", max(values), "C", sep='')
            print("Minimum Temperature: ", min(values), "C", sep='')
            print("Average Temperature: ", mean(values), "C", sep='')
            break
        else:
            entry = int(entry[:-1])
            values.append(entry)
