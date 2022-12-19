def factors(n):
    print("The Factors are")
    for i in range(1,n+1):
        if n%i==0:
            print(i)
num=int(input("Enter a number:"))
factors(num)