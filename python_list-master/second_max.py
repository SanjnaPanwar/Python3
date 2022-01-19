# number=[50,40,23,70,56,12,5,10,7]
# i=0
# max=number[i]
# smax=number[i]
# while i<len(number):
#     if number[i]>max:
#         max=number[i]
#     elif number[i]>smax and number[i]<max:
#         smax=number[i]
#     i+=1
# print(max)
# print(smax)


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

mark=[]
size=int(input("enter size of list:"))
for i in range(size):
    element=int(input("enter elements of your list:"))
    mark.append(element)
    i=0
    max=mark[i]
    smax=mark[i]
    while i <len(mark):
        if mark[i]>max:
            max=mark[i]
        elif mark[i]>smax and mark[i]<max:
            smax=mark[i]
        i+=1
print(max)
print(smax)