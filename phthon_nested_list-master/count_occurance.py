char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=0
# count=0
a=[]
while i <len(char_list):
    j=0
    count=0
    while j<len(char_list):
        if char_list[i]==char_list[j]:
            count+=1
        j+=1
    if char_list[i] in a:
        i+=1
        continue
    a.append(char_list[i])
    print(char_list[i],"=",count)
print(a)
















# for i in range(len(char_list)):
#     if i in char_list:
#         if i not in char_list:
#             a.append(i)
#     print(a)


        
