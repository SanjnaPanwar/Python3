a = {(1,2):1,(2,3):2}
print(a[1,2])


# a = {(1,2):1,(2,3):2}
# print(a[1,2])
# a = {'a':1,'b':2,'c':3}
# print (a['a','b'])


# fruit = {}
# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] = 1
# addone('Apple')
# addone('Banana')
# addone('apple')
# addone('Apple')
# print (len(fruit))
# print(fruit)

# Student = {}
# Age = {}
# Details = {}
# Student['name'] = "bikki"
# Age['student_age'] = 14
# Details['Student'] = Student
# Details['Age'] = Age
# print (len(Details["Student"]))


# my_dict = {}
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(1,2)] = 12
# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
# print (sum)
# print(my_dict)



# box = {}
# jars = {}
# crates = {}
# box['biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box
# crates['jars'] = jars
# print(len(crates))


# rec = {
# "Name" : "Python", 
# "Age":"20",
# "Addr" : "NJ", 
# "Country" :"USA"
# }
# id1 = id(rec)
# del rec
# rec = {
#     "Name" : "Python", 
#     "Age":"20", 
#     "Addr" : "NJ", 
#     "Country" : "USA"
# }
# id2 = id(rec)
# print(id1 == id2)


# dict1={1:2,2:3,3:4,4:5}
# sum=0
# for i in dict1.values():    
#     sum=sum+1
# print(sum)


# # Python program to demonstrate
# # finding 3 highest values in a Dictionary
# from heapq import nlargest
 
# # Initial Dictionary
# my_dict = {'A': 67, 'B': 23, 'C': 45,
#            'D': 56, 'E': 12, 'F': 69}
 
# print("Initial Dictionary:")
# print(my_dict, "\n")
 
# ThreeHighest = nlargest(3, my_dict, key = my_dict.get)
 
# print("Dictionary with 3 highest values:")
# print("Keys: Values")
 
# for val in ThreeHighest:
#     print(val, ":", my_dict.get(val))



# data= {1: 1, 2: 1, 3: 1, 4: 3, 5: 2}
# maxVal= None
# maxKey= -1
# for k in data:
#     if maxVal is None or maxVal< data[k]:
#         maxVal= data[k]
#         maxKey= k
# print(maxVal)
# print(maxKey)


# name_dict = {"Oliva": 18, "potter": 56, "Harry": 15}

# new_val = name_dict#values()
# maximum_val = max(new_val)
# print("Maximum value from dict:",maximum_val)


# my_dictionary = {'Micheal' : {'i' : 15, 'z' : 14},
# 			'George' : {'q' : 2, 'y' : 10, 'w' : 3},
# 			'John' : {'n' : 19}}
# new_out = {}
# for new_k, new_v in my_dictionary.items():
# 	count_new = 0
# 	for element in new_v.values():
# 		if element > count_new:
# 			count_new = element
# 	new_out[new_k] = count_new
	
# print(new_out)

# a="23.4"
# b="sanjna"
# print(a+b)



# a=[[12,34,56,43],[56,57,68,97],[32,33,65,67],[45,67,89,87],[65,67,7,66]]
# i=0
# while i <len(a):
#     j=0
#     while j<len(a[i]):
#         s=a[i][j]
#         k=0
#         while k <j:
#             f=a[i][j]
#             if s>f:
#                 s=f
#                 print(s)
#             k+=1
        
#         j+=1
#     i+=1

# a=[[12,34,56,43],[56,57,68,97],[32,33,65,107],[45,67,89,87],[65,67,7,66]]
# for i in range (len(a)):
#     max=0
#     for j in a[i]:
#         if j>max:
#             max=j
#     print(max)    

