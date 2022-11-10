l=[]
word=input("Enter a word\t")
vowels=['a','e','i','o','u','A','E','I','O','U']
for i in word:
    if i in vowels:
        l.append(i)
print("The vowels present in the word are \t",l)
