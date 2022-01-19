num=int(input("enter the num:"))
rev=0
store=num 
while num>0:
    rev=(rev*10)+num%10
    num=num//10
if  store==rev:
    print(store,"is palindrom")
else:
    print(store,"is not palindrom")