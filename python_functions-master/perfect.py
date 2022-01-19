num=int(input("enter any num:"))
a=num
def perfect(a):
    sum=0
    for i in range(1,a):
        if a%i==0:
            sum+=i
    if sum==a:
        print(a,"number is perfect")
    else:
        print(a,"number is not perfect")

perfect(num)

# def perfect():
#     sum=0
#     a=1
#     for i in range(1,1000):
#         if a%i==0:
#             sum+=i
#         if sum==a:
#             print(a,"number is perfect")
#         else:
#             print(a,"number is not perfect")
#         a+=1
# perfect()