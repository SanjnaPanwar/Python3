# addition
# subtraction
# multiplication
# division

num1=float(input("enter 1st no."))
num2=float(input("enter 2nd no."))
operation=input("1=add,2=subtract,3=multiply,4=divide:")
#if operation>=1 and operation<=4:
if operation=="1":
    print("the sum is",(num1+num2))
elif operation=="2":
    print("the subtraction is",(num1-num2))
elif operation=="3":
    print("the multiplication is",(num1*num2))
elif operation=="4":
    print("the division is",(num1/num2))
else:
    print("invalid option")    