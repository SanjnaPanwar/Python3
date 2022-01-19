i=int(input("enter 1st number:"))
user=int(input("enter 2nd number:"))
sum=0
while i<=user:
    if i%2==0:
       sum=sum+i
       print(sum)
    i+=1
print(sum)

