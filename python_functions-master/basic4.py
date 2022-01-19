# 1st part
def add_numbers(num1,num2):
    print(num1+num2)
add_numbers(56,12)

# 2nd part
def add_numbers_list():
    a=[50,60,10]
    b=[10,20,13]
    sum=0
    i=0
    while i <len(a):
        sum+=a[i]+b[i]
        i+=1
    print(sum)
add_numbers_list()