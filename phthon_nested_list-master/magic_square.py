magic_square = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]
i=0
while i<len(magic_square):
    j=0
    sum=0
    while j<len(magic_square):
        sum+=magic_square[i][j]
        j+=1
    i+=1
print(sum)
k=0
while k<len(magic_square) :
    a=0
    sum2=0
    while a<len(magic_square):     
        sum2+=magic_square[k][a]
        a+=1
    k+=1
print(sum2)
l=0
m=l
sum3=0
while l<len(magic_square):
    sum3+=magic_square[l][m]
    l+=1
print(sum3)
if sum==sum2 and sum2==sum3:
    print("it is magic square")
else:
    print("it is not magic square")    
