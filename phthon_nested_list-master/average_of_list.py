elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
count=0
sum=0
for i in range(len(elements)):
    sum+=elements[i]
    count+=1
print("average of list",sum/count)