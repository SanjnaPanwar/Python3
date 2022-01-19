n=int(input("enter decimal:"))
var=n
bin=0
i=1
while n!=0:
    rem=n%2
    n=n//2
    bin=bin+(rem*i)
    i=i*10
print("bin of",var)
print(" ",bin)    
