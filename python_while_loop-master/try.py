# l=[23,45,32,25,46,33,71,90]
# i=0
# while i>0:
#     if i%2!=0:
#         print(i)
user=input("enter you password:")
i=0
while i<=user:
    
    if user>=6 and user<=16:
        if user>="a" and user<="z" and user>="A" and user<="Z":
            if user>=0 and user<=9:
                    print(user,"it is valid password")
            else:
                    print("not valid password")    