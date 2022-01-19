# def fizz_buzz():
#     num=int(input("enter any  number:"))
#     if num%3==0 and num%5==0:
#         return "FizzBuzz"
#     elif num%3==0:
#         return "Fizz"
#     elif num%5==0:
#         return "Buzz"
#     else:
#         return num
# fizz_buzz()
    

# def shownumber(limit):
#     for i in range(limit):
#         if i%2==0:
#             print(i,"even")
#         else:
#             print(i,"odd")
# shownumber(50)


# def sum(limit):
#     for i in range(1,limit):
#         if i%3==0 or i%5==0:
#             print(i)
# sum(67)


# def prime(limit):
#     for i in range(2,limit):
#             if limit%i==0 :
#                 print("it is notprime")
#                 break
#     else:
#         print(" prime")             
# prime(5)


# def multiplication():
#     user=int(input("enter any number:"))
#     for i in range(1,11):
#         print(user,"*",i,"=",user*i)
# multiplication()

# def bmi():
#     weight=float(input("enter your weight:"))
#     height=float(input("enter your height:"))
#     Bmi=weight/height*2
#     print(Bmi)
#     if Bmi>30:
#         print("obease")
#     elif Bmi<=18.5:
#         print("underweight")
#     elif Bmi<=25.0:
#         print("normal")
#     elif Bmi<=30.0:
#         print("overweight")
# bmi()


# def uppercase():
#     user=input("enter anything:")
#     print(user.upper())
# uppercase()


# def drinks():
#     user=int(input("please enter your age:"))
#     if user<=14:
#         print("drink toddy")
#     elif user>=15 and user<=18:
#         print("drink coke")
#     elif user>=19 and user<=21:
#         print("drink beer")
#     else:
#         print("drink whisky")
# drinks()


# def sheepcount(lis):
#     c=0
#     for i in lis:
#         if i==True:
#             c+=1
#         else:
#             continue
#     print(c)
# sheepcount([True, True, True, False,
# True, True, True, True ,
# True, False, True, False,
# True, False, False, True ,
# True, True, True, True ,
# False, False, True, True])



# def is_divisible_by(lis):
#     for i in (lis):
#         if lis[0]%i==0:
#             print(True)
#             break
#         else:
#             print(False)
#             break
# is_divisible_by([12,7,7])


# def max():
#     limit=int(input("enter limit of list:"))
#     a=[]
#     for i in range(limit):
#         element=int(input("enter elements:"))
#         a.append(element)
#     j=0
#     b=a[j]
#     while j<len(a):
#         k=a[j]
#         if k>b:   
#             b=k
#         j+=1
#     print(b,"max")
#     m=0
#     c=a[m]
#     while m<len(a):
#         d=a[m]
#         if d<c:   
#             c=d
#         m+=1
#     print(c,"min")
# max()


# a=[[0],[1,3],[5,7],[9,11],[13,15,17]]
# b=[]
# i=0
# while i<len(a):
#     j=0
#     while j<=len(a):
#         b.append(a[i][j])
#         j+=1
#     i+=1
# print(b)

# str1=input("enter:")
# def encode_string(str1):
    
#     encoded = ""
#     ctr = 1
#     last_char = str1[0]

#     for i in range(1, len(str1)):

#         if last_char == str1[i]:
#             ctr += 1
         
#         else:
#             encoded += str(ctr) + last_char
#             ctr = 0
#             last_char = str1[i]
#             ctr += 1
#     encoded += str(ctr) + last_char
#     return encoded
# print(encode_string(str1)) 
# print(encode_string("PHP"))  
# print(encode_string("AAAABBBCCCDAABDAAAAC"))


# def decode(str1):
#     ints = "1234567890"

#     num = ""
#     letters = ""
#     result_string = ""

#     i = 0

#     while i < len(str1):
    
#         if str1[i] in ints:
#             num += str1[i]
              
#         else:
#             letters += str1[i]

#         i += 1

#     for i, char in enumerate(num):

#         result_string += int(char) * letters[i]

#     return result_string
    
# print(decode("4A3B2C1D2A"))
# print(decode("4A3B2C1D3A"))
# print(decode("1P1H1P"))
# print(decode("4A3B3C1D2A1B1D4A1C")) 
# 
# 
# from re import findall
# def positive_negative_sum(str1):
#     return sum(map(int, findall(r'\d+', str1))), sum(map(int, findall(r'-\d+', str1)))
# str1 = '-100#^sdfkj8902w3ir021@swf-20'
# print("Original string:")
# print(str1)
# print("\nSum of all positive, negative integers present in the said string:")
# result = positive_negative_sum(str1)
# print("Positive values:",result[0])
# print("Negative values:",result[1]) 



# s = 'abcDEF%$'

# print('Uppercase String =', s.upper())
# print('Original String =', s)


# delimiter = ""

# csv_str = delimiter.join(['a', 'b', 'c'])

# print(csv_str)  # a,b,



# s = 'Python is Nice'

# # simple string split example
# str_list = s.split(sep=' ')
# print(str_list)



# def update():
#     # limit=int(input("enter limit:"))
#     a=[]
#     for i in range(10):
#         user=int(input("enter numbers:"))
#         a.append(user)
#     for j in a:
#         if j%2==0:
#             print(j*100)
#         else:
#             print(-1*j)
# update()


