import re
user=input("enter something:")
if (user>="a" and user<="z") or (user>="A" and user<="Z") :
    print("it is an alphabet")   
elif(bool(re.match('^[a-zA-Z0-9]*$', user)) == True):
    print("it  contain digits ")
else:
    print("it contains special characters")
    