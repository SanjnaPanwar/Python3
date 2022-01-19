size=int(input("enter any num.:"))
a=[]
i=0
ls=[]
count=0
while i<size:
    element=int(input("enter element:"))
    a.append(element)
    j=0
    while j<len(a):
        k=0
        while k <len(a):
            l=a[i],a[j],a[k]
            ls.append(l)
            count+=1
            k+=1
        j+=1
    i+=1
print(ls,count)
