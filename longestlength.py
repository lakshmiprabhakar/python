def find_longestword():
    wrds=input("\nInput a list of words to find longest word: ")
    longest=0
    for words in wrds.split():
        if len(words)>longest:
            longest=len(words)
            longest_word=words
    print("The longest word is",longest_word,"and word length is",len(longest_word))
find_longestword()