size=int(input("enter size of your list:"))
b=[]
for i in range((size)):
    element=input("enter the elements:")
    b.append(element)
    c=[]
    for j in range((len(b)-1),-1,-1):  #it is used for reverse the list
        c.append(b[j])
        j+=1
    i+=1
print(b)
print(c)
if b==c:
    print("it is palindrom")
else:
    print("it is not palindrom")