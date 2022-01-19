# # q1
# string_name = "Shakrudin"
# # print (len(string_name))
# l=0
# for i in string_name:
#     l+=1
# print("len is",l)


# # q2
# string_name = "Rishabh Verma"
# # print (len(string_name))
# l=0
# for i in string_name:
#     l+=1
# print("len is",l)


# q3
# string_name = "navgurukul"
# if "n" in string_name:
#     print ("n hai")
# else:
#     print ("n nahi hai")


#q4
# string_name = "navgurukul"
# print ("n" in string_name)
# print (type("n" in string_name))


# strongpassword
name=input("use atleast one capital letter your name:")
if (name>"A" and name<"Z"):
    name2=input("use small letter in your name:")
    if name2>"a" and name2<"z":
        Name=name+name2
        num=int(input("use any number in your password:"))
        if num>=0 and num<9:
            numName=Name+str(num)
            special=input("use special characters in your passwrd:")
            if special=="@" or special=="$" or special=="&" or special=="#"or special=="!" or special=="*":
                pas=numName+special
                if len(pas)>=6 and len(pas)<=16:
                    print("your password is strong",pas)
                else:
                    print("your password length is not correct")
            else:
                print("you try to look on special sysmbols")
        else:
            print("lool on your number use in it")
    else:
        print("you have to cheack small characters")
else:
    print("use capital letters")