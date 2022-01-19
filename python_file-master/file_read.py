f = open("dem.txt", "r")
# print(f.readline())
# print(f.readline()) 
# f.close()
# f = open("demofile.txt", "r")
# for x in f:
#   print(x) 

# user = int(input("enter any number:"))
# a=user
# rem=0
# sum=0
# for user in range(a):
#     rem=user%10
#     sum+=rem
#     user=user//10
# if a%sum==0:
#     print(a ,"hsd")
# else:
#     print(a,"not hsd")


# a=int(input("enter any number to cheak harshad or not:"))
# b=a
# rem=0
# sum=0
# for a in range(b):
#     rem=a%10
#     sum=sum+rem
#     a=a//10
# if b%sum==0:
#     print(b,"is a  harshad number")
# else:
#     print(b,"is not a harshad number")


# a=[1,2,3]
# i=0
# b=[]
# count=0
# while i<len(a):
#     j=0
#     while j<len(a):
#         s=a[i],a[j]
#         b.append(s)
#         # print(b)
#         count+=1
#         j+=1
#     i+=1
# print(b)
# print("pairs",count)

# a=[19,17,12,17,17,18,10,17,14,12,19,17,12,13,11]
# i=0
# l=[]
# count=0
# while i <len(a):
#     j=0
#     while j <len(a):
#         if a[i]==a[j]:
#             count+=1
#         j+=1
#     if a[i] in l:
#         i+=1
#         continue
#     l.append(a[i])
# print(l)


user=int(input("enter yoyur no.:"))
a=user//10
b=a%10
if b==3:
    print("yes")
else:
    print("no")