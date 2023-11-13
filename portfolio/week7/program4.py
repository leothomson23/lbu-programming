if __name__ == "__main__":
    message = input('Please enter your message: ')
    counts = {}

    for letter in message:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1

    ordered = sorted(counts.items(), key=lambda x: x[1], reverse=True)

    print('Letter : Frequency')
    for item in range(min(6, len(ordered))):
        print(ordered[item][0],':', ordered[item][1])