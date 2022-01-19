marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78],
    [87, 67, 49, 68, 88]
]
# count=1
for i in range(len(marks)):
    sum=0
    count=0
    for j in range(0,len(marks[i])):
        sum=(sum+marks[i][j])
    count+=1
    print(sum)