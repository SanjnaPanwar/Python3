# # first 10 evem numbers
# i=1
# while i <=20:
#     if i%2==0:
#         print(i)
#     else:
#         pass
#     i+=1

# # first 10 odd numbers
# i=1
# while i<=20:
#     if i%2!=0:
#         print(i)
#     else:
#         pass
#     i+=1

# # print 10, 20, 30 … … 300
# i=1
# while i <=300:
#     if i%10==0:
#         print(i)
#     i+=1


# # print
# # 1 1
# # 2 4
# # 3 9...and so on
# i=1
# while i <=10:
#     print(i,i*i)
#     i+=1


# # table
# num=int(input("enter any num:"))
# i=1
# while i<=10:
#     print(num*i)
#     i+=1


# # armstrong number
# num = int(input("Enter a number: "))
# sum = 0
# temp = num
# while temp > 0:
#    digit = temp % 10
#    sum += digit ** 3

#    temp //= 10
#    print(temp)

# if num == sum:
#    print(num,"is an Armstrong number")
# else:
#    print(num,"is not an Armstrong number")



# sum=0
# i=0
# c=0
# while i<=10:
#     num=int(input("enter any number:"))
#     sum+=num
#     i+=1
#     c+=1
# print(sum/c)



# help(print);



# a=[1,2,3,4,6,2,1,4]
# b=[]
# i=0
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#     i+=1
# print(b)


# user=input("enter any name:")
# i=1
# while i <=1:
#     print("'",user,"'")
#     i+=1


# # 2 , 22 , 222 , 2222 _ _ _ _ _ n terms
# user=int(input("enter limit of series:"))
# a=str(2)
# i=1
# while i <=user:
#     print(a*i,end=",")
#     i+=1


# # 1 + 8 + 27 …………n terms
# user=int(input("enter limit:"))
# i=1
# while i<=user:
#     print(i**3,end="+")
#     i+=1


# # S = 1 + 4 – 9 + 16 – 25 + 36 – … … n terms
# user=int(input("enter limit:"))
# i=1
# while i <=user:
#     a=i*i
#     if i%2==0:
#         print(a,end="-")
#     else:
#         print(a,end="+")
#     i+=1


# # 1 + 2 + 6 + 24 + 120 . . . . . n terms
# user=int(input("enter limit:"))
# i=1
# while i<=user:
#     j=1
#     print(i*i*j,end="+")
#     i+=1
#     j+=1


# # Write a program to print only odd numbers from the given list using a while loop . L = [23, 45, 32, 25, 46,
# # 33, 71, 90]
# L = [23, 45, 32, 25, 46,33, 71, 90]
# i=0
# while i<len(L):
#     if L[i]%2!=0:
#         print(L[i])
#     i+=1
    


# # Write a program to print all the factors of a number using a while loop .
# user=int(input("enter any number to cheack factors:"))
# i=1
# while i <user:
#     if user%i==0:
#         print("factors of ",user,"is",i)
#     i+=1
    

# # Accept two numbers from the user and display sum of even numbers between them(including both)
# user1=int(input("enter start number:"))
# user2=int(input("enter end number:"))
# i=user1
# sum=0
# while i <=user2:
#     if user1%2==0:
#         sum+=i
#     user1+=1
#     i+=1
# print(sum)


# # Write a program to print the factorial of a number.
# user=int(input("enter any number:"))
# i=1
# factorial=1
# while i<=user:
#     factorial*=user
#     i+=1
#     user-=1
# print(factorial)   



# for i in (1,2,3):
#     print(i)

# for i in (2,3,4):
#     print(i)

# for i in (4,3,2,1,0):
#     print(i, end=" ")

# for i in range(10):
#     if(i%2!=0):
#         print("Hello",i)


# for i in range(10,2,-2):
#     print(i, "Hello")


# str = "Python Output based Questions"
# word=str.split()
# for i in word:
#     print(i)


# for i in range(7,10):
#     print("Python Output based Questions*")
# print("Python Output based Questions")

# for i in range(7,-2,-9):
#     print(i)
#     for j in range(i):
#         print(j)


# i="9"
# for k in i:
#     print(k)


# for i in range(1,8):
#     print(i)
# i+=2


# for i in range(4,7):
#     i=i+1
# print("Hello")

# i=4
# while(i<10):
#     i=i+3
#     print(i)


# for i in range(20):
#     if i//4==0:
#         print(i,"0")
#     print(i)


# print(5//4)


# x=1234
# while x%10:
#     x=x//10
# print(x)



# for i in 1,2,3:
#     print(i*i)

# for i in 2,4,6:
#     print("H"*i)


# p=10
# q=20     
# p=p*q//4
# q=p+q**3
# print(p,q)


# x=2
# y=6
# x=x+y/2 + y//4
# print(x)

# L = [13 , 12 , 21 , 16 , 35 , 7, 4]
# s = 5
# s1 = 3
# for i in L:
#     if (i % 4 == 0):
#         s = s + i
#         continue
#     if (i % 7 == 0):
#         s1 = s1 + i
# print(s , end=" ")
# print(s1)


# print('cs' + 'ip' if '234'.isdigit() else 'IT' + '-402')

