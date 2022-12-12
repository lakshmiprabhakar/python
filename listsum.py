list1=[]
limit=int(input("Enter the limit of the list: "))
for i in range(0,limit):
    print("Enter the elements,",i+1)
    a=int(input())
    list1.append(a)
s=0
for i in list1:
    s=s+i
print("The sum of the list is",s)
