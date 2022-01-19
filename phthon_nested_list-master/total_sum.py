number = 30

n = [10, 11, 12, 13, 14, 17, 18, 19]
c=[]
i=0
while i<len(n):
    j=0
    while n[j]<n[i]:
        if n[i]+n[j]==number:
            c.append([n[j],n[i]])
        j+=1
    i+=1
print(c)