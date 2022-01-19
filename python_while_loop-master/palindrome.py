user=int(input("enter:"))
rem=0
a=user
while user>0:
    rem=(rem*10)+(user%10)
    user=user//10
if a==rem:
    print(a,"it is palindrome") 
else:
    print(a,"it is not palindrome")    