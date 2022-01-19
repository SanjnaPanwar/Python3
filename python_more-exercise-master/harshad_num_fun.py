# num=int(input("enter any num:"))
# g=num
# num_string=list(str(num))
# print(num_string)
# a=[]
# for i in range(len(num_string)):
#     a.append(int(num_string[i]))
# print(a)
def is_harshad_number():
    num=int(input("enter any num:"))
    g=num
    rem=0
    sum=0
    for b in range(g):
        rem=num%10
        sum+=rem
        num=num//10
    if g%sum==0:
        print(bool(1))
    else:
        print(bool(0))
is_harshad_number()