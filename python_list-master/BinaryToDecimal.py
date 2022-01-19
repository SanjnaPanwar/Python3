binary_number = [1, 0, 0, 1, 1, 0, 1, 1]
i=1
sum=0
k=0
while i<=len(binary_number):
        b=(2**k)*(binary_number[-i])
        sum+=b
        i+=1
        k+=1
print(sum)



#dry run
# binarynumber=[1,0,0,1,1,0,1,1]
# i=1    sum=0   k=0    while i<=len(binnum)  b=(2**k)*(binanum[-i])       sum+=b     i+=1  k+=1  print(sum)
# 1       0      0         1<=8              b=(2**0)*binanum[-1]=1*1=1   sum=0+1=1   i=2   k=1      1
# 2       1      1         2<=8              b=(2**1)*binanum[-2]=2*1=2    2+1=3      i=3   k=2      3
# 3       3      2         3<=8              b=(2**2)*binanum[-3]=4*0=0    3+0=3      i=4   k=3      -
# 4       3      3         4<=8              b=(2**3)*binanum[-4]=8*1=8    3+8=11     i=5   k=4      11
# 5       11     4         5<=8              b=(2**4)*binanum[-5]=16*1=16  11+16=27   i=6   k=5      27
# 6       27     5         6<=8              b=(2**5)*binanum[-6]=32*0=0   27+0=27    i=7   k=6      -
# 7       27     6         7<=8              b=(2**6)*binanum[-7]=36*0=0   27+0=27    i=8   k=7      -
# 8       27     7         8<=8              b=(2**7)*binanum[-8]=128*1=128 27+128=155 i=9  k=8      155
# 9       155    8         9<=8 F

# output=155


# binary_number =[1, 0, 0, 1, 1, 0, 1, 1]
# i=1
# sum=0
# k=0
# while i<=len(binary_number):
#         b=(2**k)*(binary_number[-i])
#         sum+=b
#         i+=1
#         k+=1
# print(sum)

