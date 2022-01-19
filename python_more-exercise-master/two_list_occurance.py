list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1]
l=[]
string_list=list1+list2
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