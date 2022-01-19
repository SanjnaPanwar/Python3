# 1st part
def check_numbers():
    num1=int(input("enter 1st num.:"))
    num2=int(input("enter 2nd num.:"))
    if num1%2==0 and num2%2==0:
        print("dono even hai")
    else:
        print("dono even nhi hai")
check_numbers()

# 2nd part
def check_numbers_list(a,b):
    i=0
    while i<len(a):
        if (a[i] and b[i])%2==0:
            print(i,"even")
        else:
            print(i,"not even")
        i+=1
check_numbers_list([2,6,18,10,3,75],[6,19,24,12,3,87])