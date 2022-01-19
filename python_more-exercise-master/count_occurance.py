string_list = ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"]

l=[]
for i in range(len(string_list)):
    count=0
    for j in range(len(string_list)):
        if string_list[i]==string_list[j]:
            count+=1
    if string_list[i] in l:
        continue
    l.append(string_list[i])
    print(string_list[i],"=",count)
print(l)


string_list = ["Delhi", "Delhi", "Mumbai", "Mumbai", "Delhi", "Chennai", 'Chennai']
# l=[]
# for i in range(len(string_list)):
#     count=0
#     for j in range(len(string_list)):
#         if string_list[i]==string_list[j]:
#             count+=1
#     if string_list[i] in l:
#         continue
#     l.append(string_list[i])
#     print(string_list[i],"=",count)
# print(l)


# string_list = ["Empathy", "Empathy", "Kindness", "Kindness", "Compassion", "Humble", "Humble"]
# l=[]
# for i in range(len(string_list)):
#     count=0
#     for j in range(len(string_list)):
#         if string_list[i]==string_list[j]:
#             count+=1
#     if string_list[i] in l:
#         continue
#     l.append(string_list[i])
#     print(string_list[i],"=",count)
# print(l)