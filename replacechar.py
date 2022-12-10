str1=input("Enter a string:")
for i in range (1,len(str1)):
    str2=str1[0]+str1[1:].replace(str1[0],'$')
print("String after replaced with '$' is ",str2)
            
