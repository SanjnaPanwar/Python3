# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# # Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
# d3={}
# for i in d1:
#     for j in d2:
#         if i==j:
#             d3.update({i:d1[i]+d1[j]})
#             # print(d3)
#             # print(d1[i]+d1[j])
#         else:
#             d3.update({i:d1[i]})
#             d3.update({j:d2[j]})
#     # d3.update({i:d1[i]})
# print(d3)


# # COUNT OCCURANCE
# user=input("enter anything to count:")
# d={}
# for i in user:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d)


# empty={}
# for i in range(1,6):
#     empty.update({i:i*i})
# print(empty)

# empty={}
# for i in range(1,16):
#     empty.update({i:i*i})
# print(empty)

## SHORT VALUE
# a={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# for i in a:
   
#     # print(b)
#     for j in a:
#         s={}
#         # print(c)
#         if a[i]>a[j]:
#             tem=a[i]
#             a[i]=a[j]
#             a[j]=tem
# print(a)


# # MAKING A DICTIONARY   
# a={}
# user=int(input("enter limit:"))
# j=1
# for i in range(user):
#     a.update({i:j*10})
#     j+=1
# print(a)


# #MERGE THREE DICTIONARY
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic1.update(dic2)
# dic1.update(dic3)
# print(dic1)


# a={1:2,2:3,3:4,4:5,5:6}
# sum=0
# for i in a:
#     sum+=a[i]
# print(sum)


# a={1:2,2:3,3:4,4:5,5:6}
# pro=1
# for i in a.values():
#     pro*=i
# print(pro)



# a=["sanjna","laddu","sanju","binnu"]
# b=[1,2,3,4]
# c={}
# for i in range(len(a)):
#     c.update({a[i]:b[i]})
# print(c)


# a={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# for i in a.keys():
#     for j in a.keys():
#         if i>j:
#             temp=i
#             i=j
#             j=temp
# print(a)



# a={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# for i in a.values():
#     z=i
#     for j in a.values:
#         x=j
#         if x>z:
#             z=x
# print(z)

# student_data={}
# user=int(input("enter limit of student information;"))
# i=0
# while i <=user:
#     sub={}
#     m=1
#     j=0
#     while j<(i):
#         name_of_stuent=input("enter student's name:")
#         class_of_student=input("enter student's class : ")        
#         subject_of_student=input("enter student's subject:")
#         sub["name"]=[name_of_stuent]
#         sub["class"]=[class_of_student]
#         sub["subject"]=[subject_of_student]
#         # student_data.update({"id"+str(m):sub})

#         print(sub)
#         # print(student_data)
#         m+=1
#         j+=1
#     student_data.update({"id"+str(m):sub})
#     i+=1
# print(student_data)



# #making a dictionary
# data={}
# i=0
# k=1
# while i<(3):
#     sub={}
#     j=0
#     while j<1:
#         name=input("enter name;")
# #         cllass=input("enter class:")
#         subje=input("enter subject;")
#         j+=1
#         sub["name"]=[name]
#         sub["class"]=[cllass]
#         sub["subject"]=[subje]
#     i+=1
#     data.update({"id"+str(k):sub})
#     k+=1
# print(data)

# my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# user=input("enter anything to count:")
# d={}
# for i in user:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d)

# my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# for i in my_dict:
#     print(i)
#     if type(my_dict[i])==list:
#         k=0
#         for j in range(len(my_dict[i])):
#             print(my_dict[i][j],end="")
#             k+=1
#     print()
              

# a=[[1,2,3],[4,5,6],[7,8,9]]
# # k=0
# for i in range(len(a)):
#     # print(a[i]) 
#     # k=0
#     # print(a[i][k])
#     for j in range(len(a[i])):
#          print(a[i][j])
#     while k<i:
#         print(a[i][k])
#         k+=1

# my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# for i in my_dict:
#     print(i)
#     if type(my_dict[i])==list:
#         k=0
#         for j in range(len(my_dict[i])):
#             print(my_dict[i][j],end="")
#             k+=1
#     print()

# a=[{{"m":2,"r":3},{"m":5,"r":6}}]
# for i in a:
#     # print(i)
#     # for j in a[i]:
#         # print("m")
#         if type(i)==dict:
#             # print(a["m"])
#             for j in a[i]:
#                 print(a[i][j])


# a=[1,2,3,4]
# b={}
# for i in a[::-1]:
#     b=({i:b})
# print(b)

# a=[[1,2,3],[4,5,6],[7,8,9]]
# i=0
# while i<len(a):
#     j=0
#     while j <len(a[i]):
#         # if a[i]==a[j]:
#             print(a[i][j])
#             j+=1
#     i+=1



# a=["rupa","snajna","laddu"]
# b=[]
# i=0
# while i <len(a):
#     j=0
#     while j <len(a[i]):
#         b.append(a[i][j])
#         j+=1
#     i+=1
# print(b)


# a=5
# b=4.5
# print(type((a+b)))


# QUESTION NO.36
# a={'key1': 1, 'key2': 3, 'key3': 2}
# b={'key1': 1, 'key2': 2}
# for i in a and b:
#     if a[i]==b[i]:
#         print({i:a[i]},"is present")


# a={'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
# 'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
# 'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
# for i in a:
#     for j in a[i]:
#         if type(a[i])==list:
#             print(a[i][4])
#             break



# a={'c1': 'Red', 'c2': 'Green', 'c3': None}
# b={}
# for i in a:
#     if a[i]==None:
#         del a['c3']
#     else:
#         b.update(a)
# print(b)


# a={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# b={}
# for i in a:
#     if a[i]>=170:
#         b.update({i:a[i]})
# print(b)


# a=['S001', 'S002', 'S003', 'S004']
# b=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# c=[85, 98, 89, 92]
# d={}
# for i in range(len(a)):
#     e={}
#     for j in range(len(b)):
#         if i==j:
#             e.update({b[j]:c[j]})
#     d.update({a[i]:e})
# print(d)


# a={'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
# for i in a:
#     if a[i]==12:
#         print(True)
#         # print(False)
#         break
#     # elif a[i]==10:
#         print(False)
#     #     break


# a=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# b={}
# for i in range(len(a)):
#     c=[]
#     for j in range(len(a[i])):
#         if a[i]==a[j]:
#             # print(a[i])
#             c.append([a[i],a[j]])
#             print(c)
#     b.update({a[i]:c})
# print(b)


# a={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# b=[]
# c={}
# for i in a:
#     # c={}
#     if type(a[i])==list:
#         # c={}
#         for j in range(len(a[i])):
#             c.update({i:a[i][j]})
#             print(c)
#     b.append(c)
# # print(b)


# a={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['ZacharySimon']}
# b={}
# for i in a:
#     if type(a[i])==list:
#         for j in range(len(a[i])):
#             b.update({i:a[i][j]})
# print(b)



# def is_leap(year):
#     leap = False
#     Leap=True
#     if year%400==0:# or year%400==0:
#         if year%4==0:
#             return Leap
#         return Leap
#     elif year%100==0:
#         return leap
#     else:
#     # Write your logic here
    
#         return leap

# year = int(input("enter:"))
# print(is_leap(year))


# def is_leap(year):
#     leap = False
#     Leap=True
#     if year%400==0 :
#         if year%4==0:
#             return Leap
#         return Leap
#     elif year%4==0 and year%100==0:
#             return leap
#     elif year%4==0:
#         return Leap
#     elif year%100==0:
#         return leap
#     # else:
#     # Write your logic here
#         # return leap
# year = int(input("enter:"))
# print(is_leap(year))

# string = "abracadabra"
# l = list(string)
# l[5] = 'k'
# string = ''.join(l)
# print(string)

# for i in range(5):
    