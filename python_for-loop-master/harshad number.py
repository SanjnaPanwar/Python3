a=int(input("enter any number to cheak harshad or not:"))
b=a
rem=0
sum=0
for a in range(b):
    rem=a%10
    sum=sum+rem
    a=a//10
if b%sum==0:
    print(b,"is a harshad number")
else:
    print(b,"is not a harshad number")        