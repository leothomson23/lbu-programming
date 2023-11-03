if __name__ == "__main__":
    def encrypt(code):
        print(code.replace(" ", "")[::-1])
    code = input("Enter the message you want encrypted: ")
    encrypt(code)

#Credits:
#https://www.w3schools.com/python/python_howto_reverse_string.asp
#https://www.geeksforgeeks.org/python-remove-spaces-from-a-string/