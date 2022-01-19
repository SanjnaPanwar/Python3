numbers=[50,40,23,70,56,12,5,10,7]
size=0
for i in numbers:
    size+=1
i=0
b=numbers[i]
while i<size:
    j=numbers[i]
    if j<b:
       b=j
    i=i+1
print(b,"minimum in list")

# dry run
# i=0   b=number[i]   while i<len(number)   j=numbers[i]   if j<b     b=j   i=i+1   print(b,"max")
# 0     50                0<9 T             j=50             50<50 F   -    i=0+1=1      -
# 1     50                1<9 T             j=40             40<50 T  b=40  i=1+1=2      -
# 2     40                2<9 T             j=23             23<40 T  b=23  i=2+1=3      -
# 3     23                3<9 T             j=70             70<23 F   -    i=3+1=4      -
# 4     23                4<9 T             j=56             56<23 F   -    i=4+1=5      -
# 5     23                5<9 T             j=12             12<23 T  b=12  i=5+1=6      -
# 6     12                6<9 T             j=5              5<12  T  b=5   i=6+1=7      -
# 7     5                 7<9 T             j=10             10<5 F   -    i=7+1=8      -
# 8     5                 8<9 T             j=7              7<5  F   -    i=8+1=9      -
# 9     5                 9<9 F









num=[12,3,5,67,7]
name="sanjna"
i=0
while i<5:
    print(str(num[i])*str(name))
    i+=1