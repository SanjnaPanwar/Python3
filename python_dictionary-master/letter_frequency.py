# user="MISSISSIPPI"
user=input("enter the user:")
d=user
c={}   
for i in d:
    if i in c:
        c[i]=c[i]+1
    else:
        c[i]=1
print(c)



























# for i in a:
# b=[]
# i=0
# while i <len(a):
#     j=0
#     count=0
#     while j<len(a):
#         if a[i]==a[j]:
#             count+=1
#         j+=1
#     if a[i] in a:
#         i+=1
#         continue
#     b.append([i])
#     print(a[i],"=",count)
# print(b)