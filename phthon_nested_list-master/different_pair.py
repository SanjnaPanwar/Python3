size=int(input("enter any num.:"))
a=[]
i=0
ls=[]
while i<size:
    element=int(input("enter element:"))
    a.append(element)
    j=0
    while j<len(a):
        l=a[i],a[j]
        ls.append(l)
        j+=1
    i+=1
print(ls)
