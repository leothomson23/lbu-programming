if __name__ == "__main__":
    def atleast_one(word1, word2):
        print('These letters are in atleast 1 word: ', word1 | word2)
    def both_words(word1, word2):
        print('These letters are in both words: ',word1 & word2 )
    def either_word(word1, word2):
        print('These letters are in either word, but not in both: ', (word1 - word2) | (word2 - word1))

    word1 = set(input('Enter word 1: '))
    word2 = set(input('Enter Word 2: '))

    atleast_one(word1, word2)
    both_words(word1, word2)
    either_word(word1, word2)


