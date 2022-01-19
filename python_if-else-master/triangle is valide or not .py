print("enter three angles of a triangle to check it is valid or not")
x=int(input("enter 1st angle:"))
y=int(input("enter 2nd angle:"))
z=int(input("enter 3rd angle:"))
if x+y+z==180 and x+y>z==180: #     
    print("triangle is valid")
else:
    print("triangle is not valid")    