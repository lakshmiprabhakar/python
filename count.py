str=input("Enter a string: ")
list1=[]
d={}
for x in str:
    list1.append(x)
for x in list1:
    d[x]=str.count(x)
print(d)