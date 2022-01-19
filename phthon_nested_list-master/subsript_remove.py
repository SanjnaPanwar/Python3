a = ["the quick brown fox jumped over the lazy dog. the dog slept over the verandah."]
b=[]
for i in range(((len(a))-1),-1,-1):
    for "over" in a:              
    # b.append(a[i])
        a.remove("over")
print(a) 

# mainStr.remove("over")
# print(len(mainStr))
# # a=['Red', 'Maroon', 'Yellow', 'Olive']
# b=[]
# i=0
# while i<len(mainStr):
#     j=0
#     c=[]
#     while j<len(mainStr[i]):
#         c.append(mainStr[i])
#         j+=1
#     b.append(c)
#     i+=1

# print(b)