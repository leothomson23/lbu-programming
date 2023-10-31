if __name__ == "__main__":
    entry = input("Enter your message: ")

    if len(entry) <= 1:
        print(entry)
    else:
        print(entry [:-1])