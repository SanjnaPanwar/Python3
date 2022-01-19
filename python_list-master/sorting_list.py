numlist=[]
listlength=int(input("enter length of list: "))
for i in range(listlength):
    value=int(input("enter value of elements:"))
    numlist.append(value)
for i in range (listlength):
    for j in range(listlength):
        if numlist[i]<numlist[j]:
            temp=numlist[i]
            numlist[i]=numlist[j]
            numlist[j]=temp
print("asscending",numlist)
