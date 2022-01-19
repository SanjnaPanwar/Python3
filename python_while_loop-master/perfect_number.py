a=int(input("enter any number:"))
sum=0
for i in range(1,a):
    if a%i==0:
        sum+=i
if sum==a:
    print("number is perfect",a)
else:
    print("number is not perfect",a)