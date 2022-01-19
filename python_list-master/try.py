# # Correcting mistake values in a list
# odd = [2, 4, 6, 8]

# # change the 1st item    
# odd[0] = 1            

# print(odd)

# # change 2nd to 4th items
# odd[1:4] = [3, 5, 7]  

# print(odd)                   

# def count_letters(l):
#     count = {}  # define a dict to hold our count
#     for i in l: # loop through the list
#         count[i] = len(i)  # for each item, compute its length and store it in the dict
#     return count # return the count
 
# if __name__ == '__main__':
#     colors = ['red', 'blue', 'green', 'yellow', 'black']
#     print(count_letters(colors))


# a=[23,1,2,3]
# b="sanjna"
# i=0
# c=a[0]
# for i in range(len(a)):
#     print(c,b)
#     i+=1


# a=[1,3,5,7,9,10]
# b=[2,4,6,8]    
# c=a+b
# c.sort()
# print(c)


# a=["wer","ewe","ewerw"]
# b=str(a)
# print(b)



# numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# size=0
# for i in numbers:
#     # print(size)
#     size+=1
 
    
# a=numbers[i]   
# for i in range(size):
#     if i<size:
#         j=numbers[i]
#         if j>a:
#             a=j
# print(a,"is max in this list")            

# a= [1, 0, 0, 1, 1, 0, 1, 1]
# dec=0
# weight=a[-1]
# while dec!=0:
#     rem=dec%10
#     dec+=rem*weight
#     a=a/10
#     weight=weight*2
#     print(a)


students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']

marks = [10, 20, 56, 45, 36, 20]


print (len(students))

print (len(marks))
length = len(students) # kyunki dono ki same length hai toh jiski bhi length le sakte ho

counter = 0

while counter < length:

    print(students[counter] + str(marks[counter]))