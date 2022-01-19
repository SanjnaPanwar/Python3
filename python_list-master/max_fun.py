# numbers=[50,40,23,70,56,12,5,10,7]
# size=0
# for i in numbers:
#     size+=1
# i=0
# b=numbers[i]
# while i<size:
#     j=numbers[i]
#     if j>b:   
#        b=j
#     i=i+1
# print(b,"max")




mark=[]
size=int(input("enter size of list:"))
for i in range(size):
    element=int(input("enter your element of list:"))
    mark.append(element)
i=0
b=mark[i]
while i<size:
    j=mark[i]
    if j>b:   
        b=j
    i=i+1
print(b,"max")




# mark=[]
# size=int(input("enter size of list:"))
# for i in range(size):
#     element=int(input("enter elements of your list:"))
#     mark.append(element)
#     i=0
#     max=mark[i]
#     smax=mark[i]
#     while i <len(mark):
#         if mark[i]>max:
#             max=mark[i]
#         elif mark[i]>smax and mark[i]<max:
#             smax=mark[i]
#         i+=1
# print(max)
# print(smax)



# # numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# size=0
# for i in numbers:
#     size+=1
# print("lenght of list is",size) 
# index=numbers[0]
# # index2=numbers[i]
# # for i in numbers:
# i=0
# # while i<=size:
#     if index<i:
#         index=numbers[i]

#         print("it is max in list",index)     
#     elif index>i:
#         print() 
#     i+=      