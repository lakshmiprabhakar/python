def add_ing_or_ly(str):
    if(str[-3:]=="ing"):
        str=str+"ly"
    else:
        str=str+"ing"
    return str
word=input("Enter a word to modify:")
modified_string=add_ing_or_ly(word)
print("modified_string=",modified_string)