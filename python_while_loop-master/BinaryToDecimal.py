n=str(input("enter binary number:"))
a=0
l=len(n)
n=int(n)
b=l
while n>0:
        if n%10==0:
                a+=0*(2**(l-b))
        if n%10==1:
                a+=1*(2**(l-b))
        n//=10
        b=b-1
print(a)