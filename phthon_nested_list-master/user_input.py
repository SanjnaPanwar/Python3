n=[]
size=int(input("enter size of list:"))
i=0
while i<size:
    u=(input("enter elements of list:"))
    n.append(u)
    i+=1
print(n)
u1=input("enter anything to cheak it is present in list or not:")
if u1 in n :
    print(u1,"is present")
else:
    print(u1,"is not present in list")