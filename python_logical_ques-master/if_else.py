# # cheacking num is positive or negative 
# num=int(input("enter any number:"))
# if num=="-":
#     print(num)
# else:
#     print(-num)


# check three digit number
# num=int(input("enter a num;"))
# if num>=100 and num<=999:
#     print("3 digit number")
# else:
#     print("not three digit")

# day=int(input("enter day number:"))
# if day>=1 and day<=5:
#     charge=2
#     print(day*charge)
# elif day>=6 and day<=10:
#     charge=3
#     print(day*charge)
# elif day>=11 and day<=15:
#     charge=4
#     print(day*charge)
# elif day>15 :
#     charge=5
#     print(day*charge)
# else:
#     print("invalid input")

# cheak strin present or not
# cheack=input("enter something:") 
# if "1" in cheack or "2" in cheack or"3" in cheack or "4" in cheack or "5" in cheack or "6" in cheack or"7" in cheack or "8" in cheack or "9" in cheack or "0" in cheack :
#     print("yes")
# else:
#     print("no")



# # second max
# n1=int(input("enter 1st num:"))
# n2=int(input("enter 2nd num:"))
# n3=int(input("enter 3rd num:"))
# if n1>=n2 and n1>n3:
#     print(n1,"and",n2,"are equal")
# if n1>=n3 and n1>n2:
#     print(n1,"and",n2 ,"are equal")
# if n2>n1 and n2>=n3:
#     print(n2,"and",n3,"are equal")
# if n3>n1 :
#     print(n3,"is greater")
# if n3>n2:
#     print(n3,"is greater")
# else:
    # print(n3,"is greatest")

# # ing and ly addition
# some=input("enter something:")
# if "ing" not in some:
#     print(some+"ing")
# elif "ing" in some:
#     print(some+"ly")

# name=input("enter your name:")
# lastname=input("enter last name:")
# print(lastname,"",name)

some =int(input("enter  something:"))
a=some//10
b=a%10
if b==3:
    print('yes')
else:
    print("no")