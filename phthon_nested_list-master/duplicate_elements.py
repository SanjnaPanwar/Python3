n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
i=0
list1=[]
while i<len(n):
    j=0
    count=0
    while j<len(n):
        if n[i]==n[j]:
            count+=1
        j+=1
    if n[i] in list1:
        i+=1
        continue
    list1.append(n[i])
    print(n[i],"=",count)
print(list1)