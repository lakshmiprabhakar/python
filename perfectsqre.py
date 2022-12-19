list1=[]
j=32
i=int(input("Initial range:"))
n=int(input("Final range:"))
for i in range(n+1):
    if j**2==i:
        if i%2==0:
            list1.append(i)
        j=j+1
while(i<n+1):
    if j**2==i:
        if i%2==0:
            list1.append(i)
        j=j+1
    i=i+1
print(list1)