print("enter sides of triangle")
x=int(input("1st side:"))
y=int(input("2nd side:"))
z=int(input("3rd side:"))    
if x+y>z or x+z>y or z+y>x:
    print("it is a valid trianlge")
else:
    print("it is not valid tringle")     