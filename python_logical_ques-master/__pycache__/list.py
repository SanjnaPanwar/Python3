# #reverse a list
# user=input("enter something:")
# a=user
# i=1
# b=[]
# while i <=len(a):
#     b.append(a[-i])
#     i=i+1
# print(b)

# # printing elements by index value
# grocery_list = ['flour','cheese','carrots']
# for i in range(len(grocery_list)):
#     print(i,":",grocery_list[i])


# # The original list is: [ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
# str=""
# a=[ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
# # b=str.join(a)
# # print(b)
# i=0
# e=0
# while i<len(a):
#     # if type(a[i])==list:
#     #     b=a[i]
#     #     c=str.join(b)
#     #     # print(c)
#     d=str.join(a[i])
#     i+=1
#     print(d,end="")
# str = ""   # string  
# list = ['J','a','v','a','t','p','o','i','n','t']    # iterable  
# # Calling function  
# str2 = str.join(list)  
# # Displaying result  
# print(str2) 


# # List product excluding duplicates.
# # List = [6,1,3,5,6,3,1]
# # Output: 60
# a = [6,1,3,5,6,3,1]
# i=0
# p=1
# c=[]
# while i<len(a):
#     if a[i] not in c:
#         c.append(a[i])
#         p*=c[i]
#     # elif a[i] in c:
#     #     p*=a[i]
#     i+=1
# print(p)


# input_list = [1, 2, 2, 5, 8, 4, 4, 8]
# i=0
# b=[]
# c=0
# while i <len(input_list):  
#     if input_list[i]  not in b:
#         b.append(input_list[i])
#         c+=1
#     i+=1
# print(b,"count=",c)


# user=int(input("enter any num;"))
# a=9119
# b=a//1
# c=b%10
# i=1
# while i<=4:
#     b+=a//1
#     c+=b%10
#     print(b)
#     print(c)
#     i+=1


# a=[1,1,2,3,4,4,5,1]
# c=[]
# count=1
# i=0
# while i<len(a):
#     d=[]
#     if a[i] not in c:
#         c.append(a[i])  
#     if a[i] in c:
#         d.append([a[i],count])
#         count+=1
    
#     c.append(d)
#     i+=1
# print(c)
# print(count)


# a=[1,1,2,3,4,4,5,1]
# i=0
# c=1
# d=[]
# while i <len(a):
#     j=0
#     while j<len(a):
#         if a[i]==a[j]:
#             c+=1
#             d.append([c,a[i]])
#         else:
#             d.append(a[i]) 
#         j+=1
#     i+=1
# print(d)


# Original_list= [34.67, 12, -94.89, 'Python', 0, 'C#']
# a=[]
# i=0
# while i<len(Original_list):
#     if type(Original_list[i])==int :
#         a.append(Original_list[i])
#     i+=1
# print(a)

# a=['aabc', 'abc', 'ab', 'pa']
# b=[]
# i=0
# while i <len(a):
#     j=0
#     while j<len(a[i]):
#         if a[i][j]==a[i][j]:
#             print("same")
#             break
#         else:
#             print("not")
#             break
#         j+=1
#     i+=1


# a=[4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23
# ,24,25,26,27,28,29,30]
# for i in a:
#     if i%2==0:
#         print(i, end=' ')

# list1 = [4, 6, 8, 24, 12,2]
# max= sorted(list1)
# print(max)

# list1 = range(100, 110)
# print (list1.index(105))


# list1 = [1, 2, 3, 4, 5]
# list2 = list1
# list2[0] = 0;
# print( list1)


# List1 = [1998, 2002]
# List2 = [2014, 2016]
# print ((List1 + List2)*2)

# check1 = ['Learn', 'Quiz', 'Practice', 'Contribute']
# check2 = check1
# check3 = check1[:]
# check2[0] = 'Code'
# check3[1] = 'Mcq'
# count = 0
# for c in (check1, check2, check3):
#     if c[0] == 'Code':
#         count += 1
#     if c[1] == 'Mcq':
#         count += 10
# print (count)

# list = [1, 2, 3, None, (1, 2, 3, 4, 5), ['Geeks', 'for',
# 'Geeks']]
# print(len(list))

# list = []
# list_1 =[]
# n = int(input("enter the total numbers inside list.: "))
# i = 1
# while(i <= n):
#     num = int(input("enter the numbers you want to insert into list: "))
#     i +=1
#     list.append(num)
# print(list, " <--the given list by you is here.\n ")
# list.sort()
# print(list)
# print(max(list))

# numList = []
# def PythonList(start, end):
#     for x in range(start, end):
#         if x % 2 == 0:
#             numList.append(x)
#             return numList
# print(PythonList(4, 30))


# def cal(n):
#     sum=0
#     for i in range(1, n, 1):
#         sum = sum +i
#     print(sum)
# rev = cal(11)

# aList = [4, 6, 8, 24, 12, 2]
# aList.sort(reverse=True)
# print(aList.pop(0))


# def findDigitsCharsSymbols(inputString):
#     charCount = 0
#     digitCount = 0
#     symbolCount = 0
#     for char in inputString:
    #     if char.islower() or char.isupper():
    #         charCount+=1
    #     elif char.isnumeric():
    #         digitCount+=1
    #     else:
    #         symbolCount+=1
    # print(("Chars = ", charCount, "Digits = ", digitCount, "Symbol = ", symbolCount))
    # # inputString = "P@#yn26at^&i5ve"
    # print("total counts of chars, digits,and symbols \n")
    # findDigitsCharsSymbols("P@#yn26at^&i5ve")


# a=[1,1,2,3,4,4,5,1,9,0,8,7,6,5]
# a=["ranu","sanu","laddu","ladu","ladu","ranu","ran"]
# i=0
# d=[]
# while i <len(a):
#     j=0
#     c=0
#     while j <len(a):
#         if a[i]==a[j]:
#             c+=1
#         j+=1
#     if a[i] in d:
#         i+=1
#         continue
#     d.append(a[i])
#     print(a[i],"=",c)


# a=[[10, 20], [30, 40], [50, 60], [30, 20, 80]]
# b=[[61], [12, 14, 15], [12, 13, 19, 20], [12]]
# c=[]
# i=0
# while i < len(a):
#     c.append(a[i]+b[i])
#     i+=1
# print(c)


# number = 30
# n = [10, 11, 12, 13, 14, 17, 18, 19]
# c=[]
# i=0
# while i<len(n):
#     j=0
#     while n[j]<n[i]:
#         if n[i]+n[j]==number:
#             c.append([n[i],n[j]])
#         j+=1
#     i+=1
# print(c)



# a=[9,[7,4,8],[0,9,8,[4,2,1]]]
# for i in range(len(a)):
#     print(a[i])



# num = [1, 0, 0, 1, 1, 0, 1, 1]
# sum=0
# for i in range(1,len(num)):
#     sum+=num[-i]*(2**i)
# print(sum)


# name=[ 'n', 'i', 't', 'i', 'n' ]
# a=[]
# for i in range((len(name)-1),-1,-1): 
#     a.append(name[i])
# if name==a:
#     print("it is palindrome")
# elif name>a:
#     print("it is not palindrome")


# a=["ladal","mom","sanas","lakl","laddu","manam","nitin"]
# i=0
# while i<len(a):
#     d=a[i]    
#     j=1
#     c=''
#     while j<=len(d):
#         c+=d[-j]
#         j+=1
#     if a[i]==c:
#         print(i,"yes palindrome")
#     else:
#         print(i,"no")  
#     i+=1


a=[ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
i=0
b=[]
while i <len(a):
    j=0
    while j <len(a[i][j]):
        b.append(a)
        j+=1
    i+=1
print(b)
