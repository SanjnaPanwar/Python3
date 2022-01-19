number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19]
i=0
a=n[i]
c=[]
while i<=len(n):
    b=n[i]
    if a+b==number:
        # print(c.append(number))
        c.append(n)
    i+=1
print(c)
