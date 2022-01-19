# a=[]
# size=int(input("enter size of your list:"))
# for i in range(size):
#     val=int(input("enter elemnts of your list:"))
#     a.append(val)
# minval=min(a)
# print("min value in list:",minval) 
# a.remove(minval)
# smin=min(a)
# print("second min value in list=",smin)   


numbers=[50,40,23,70,56,12,5,10,7]
size=0
for i in numbers:
    size+=1
i=0
b=numbers[i]
while i<size:
    j=numbers[i]
    if j>b:
       b=j
    i=i+1
    # b.remove(b)
print(b," max")
secondmax=j
numbers.remove(b)
print(secondmax)