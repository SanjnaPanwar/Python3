our_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,12,13,14,15]
c=[]
size=3
for i in range(0,len(our_list),size):
    c.append(our_list[i:i+size])
print(c)
