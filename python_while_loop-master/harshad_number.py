user=int(input("enter any number:"))
a=user
rem=0
sum=0
while user>0:
    rem=user%10
    sum=sum+rem
    user=user//10
if a%sum==0:
    print("it is harshad no.")
else:
    print("not harshad num.")        


# dry run  
# user=input   a=user  rem=0  sum=0   while user>0:  rem=user%10  sum=sum+rem  user=user//10   if a%sum==0:  print(it's harshad no.)  else: print(not)
# 45           a=45     0       0      45>0 T        rem=45%10=5  sum=0+5=5    user=45//10=4   
# 4            a=45     5       5      4>0 T         rem=4%10=4   sum=5+4=9    user=4//10=0      45%9==0 T       it's harshad no.

