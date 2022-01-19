specialchr= "!","@","#","$","&"
user=input("enter any character:")
if user>="a" and user<="z" or user>="A" and  user<="Z":
    user1=int(input("enter any number:"))
    if user1>=0 and user1<=10000:
        i=input("enter any special character:")
        if i in specialchr:
            print("your password is strong")
else:
    print("it is not strong password")    
               