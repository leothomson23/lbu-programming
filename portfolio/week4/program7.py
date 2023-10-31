if __name__ == "__main__":
    from statistics import mean

    count = 1
    values = []

    while count <= 6:
        entry = input("Enter a temperature: ")
        entry = int(entry[:-1])
        values.append(entry)
        count += 1

    print("\n")
    print("Maximum Temperature: ", max(values), "C", sep='')
    print("Minimum Temperature: ", min(values), "C", sep='')
    print("Average Temperature: ", mean(values), "C", sep='')