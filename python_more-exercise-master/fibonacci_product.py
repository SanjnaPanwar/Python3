i=1
j=2
user=int(input("enter you limit:"))
product=1
for k in range(user-1):
    print(i)
    c=i+j
    i=j
    j=c
    product*=i
print("product is",product)