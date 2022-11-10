year=int(input("enter the current year\n"))
fut=int(input("enter the future year\n"))
print("The leap years are")
for year in range(year,fut+1):
    if(year%4==0) and year%100!=0 or year%400==0:
        print(year)
    
