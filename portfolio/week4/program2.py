if __name__ == "__main__":
    def string(str):
        upper = 0
        lower = 0
        for i in range(len(str)):
            if str[i].isupper():
                upper += 1
        print("Uppercase Letters:", upper)
        for i in range(len(str)):
            if str[i].islower():
                lower += 1
        print("Lowercase Letters:",lower)

    string("Hello my name is Leo")