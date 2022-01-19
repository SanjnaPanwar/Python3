username="sanjna panwar"
userpassword="sanju@123"
name=input("enter your name : ")
password=input("enter your password and your password should be in number,character and special character:")
if name==username: 
    # password=input("enter password:")
    if password==userpassword:
        print("login successful")
    else:
      print("your password is not correct.")
elif name!=username and  password !=userpassword:
    print("user name and password is incorrect. please try again") 
    print("create new account:")      
    username2=input("enter your name:")
    print("your username is" ,username2)
    userpassword2=input("enter your password and your password should be in number,character and special character:")
    re_enter_password=input("enter again your password:")
    if userpassword2==re_enter_password:
        print("your account is created succefully")
    else:
        print("yourpassword is not matchin.please try again:")
else:
    print("your user name is wrong,please try again.")    