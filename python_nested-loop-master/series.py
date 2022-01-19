n=int(input("enter value:"))
sum=0
for s in range(1,n):
    if s==1:
        print("",s*s)
        sum=sum+(s*s)
        # print(sum)
    elif s%2==0:   
        print("",s*s)
        sum=sum+(s*s) 
        # print(sum)

    else:
        print(-s*s)    
        sum=sum-(s*s)
print(sum)
