marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]
]
average=1
for i in range(len(marks)):
    sum=0
    for j in range(5):
        sum+=(marks[i][j])/5
    print("average of year",sum)
    average+=1
