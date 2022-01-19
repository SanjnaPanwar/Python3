# 0
# 11
# 222
# 3333
# 44444

# for i in range(5):
#     for j in range(5):
#         if j<=i:
#             print(i,end="")
#     print()

# 0
# 01
# 012
# 0123
# 01234

# for i in range(5):
#     for j in range(5):
#         if j<=i:
#             print(j,end="")
#     print()



# 0
# 01
# 012
# 0123
# 01234
# 0123
# 123
# 23
# 3
# for i in range(5):
#     for j in range(5):
#         if j<=i:
#             print(j,end="")
#     print()
# for i in range(5):
#     for j in range(4):
#         if i<=j:
#             print(j,end="")
    # print()

# *
# **
# ***
# ****
for i in range(5):
    for j in range(i):
        print(" ",end=" ")
    for j in range(i,5):
        print(j,end=" ")
    for j in range(i+1):
        print(j,end=" ")
    print()


# 0
# 12
# 234
# 3456
# 45678
# for i in range(5):
#     for j in range(i+1):
#         print(j+i,end="")
#     print()

# 00000
# 1111
# 222
# 33
# 4
# for i in range(5):
#     for j in range(5-i):
#         print(i,end="")
#     print()   


# 1
# 44
# 999
# # 16161616
# for i in range(5):
#     for j in range(i):
#         print(i*i,end="")
#     print() 