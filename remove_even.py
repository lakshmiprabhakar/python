list1=[]
even=[]
n=int(input("Enter the limit of list: "))
print("Enter the integers into the list ")
for i in range(0,n):
 print("Enter the element no:{}".format(i+1))
 k=int(input())
 list1.append(k)
print("List of integers are ",list1)
for i in list1:
 if i%2!=0:
  even.append(i)
print("List of integers removing even numbers are ",even)
