user=input("enter something:")
if( user>="a" and user<="z") or (user<="A" and user>="Z"):
    print("it is alphabet" )
elif  user>="0" and user<="9":
    print("it is an integer")
else:
    print("it is a special character")    
    