marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78]
]
for i in range(len(marks)):
    sum=0
    for j in range(5-i):
        sum+=(marks[i][j])/(5-i)
    print(sum)