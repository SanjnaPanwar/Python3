# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# size=0
# for i in numbers:
#     size+=1
# print("lenght of list is",size-1)   

# # list1=[]
# index=0
# lessthan40=0
# greaterthan40=0
# while index < size:
#     mark=numbers[index]
#     if mark<40:
#         lessthan40+=numbers[i]    
#     elif mark>40:
#         greaterthan40+=numbers[i]
#     index+=1
#     # list1.append(numbers[index])
#     # print(list1)
# print(lessthan40)
# print(greaterthan40)


numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0
count=0
list1=[]
list2=[]
while i<len(numbers):
    if numbers[i]<=40 :
        list1.append(numbers[i])
    elif numbers[i]>40:
        list2.append(numbers[i])
    count+=1
    i+=1
print(count)
print(list1) 
print(list2) 




