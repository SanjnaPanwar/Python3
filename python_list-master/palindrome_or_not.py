name=[ 'n', 'i', 't', 'i', 'n' ]
a=[]
for i in range((len(name)-1),-1,-1): 
    a.append(name[i])
if name==a:
    print("it is palindrome")
elif name>a:
    print("it is not palindrome")
            