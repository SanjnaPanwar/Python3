year=int(input("please enter year:"))
if year%400==0: 
    print("it is a century leap year")
elif year%4==0:
    print("it is a leap year")   
else:
    print("it is not a leap year") 