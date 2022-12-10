print("Enter the three numbers.")
a=int(input("\nEnter the first number: "))
b=int(input("\nEnter the second number: "))
c=int(input("\nEnter the third number: "))
if a>b and a>c:
    print(a,"\t is biggest number.")
elif b>a and b>c:
    print(b,"\t is biggest number.")
else:
    biggest=c
print(c,"is the biggest number.")
