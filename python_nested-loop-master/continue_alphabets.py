user=int(input("enter number of alphabet you want:"))
i=0
while i <user:
    k=ord("A")
    j=0
    while j <i+1:
        print(chr(k+i),end=" ")
        k+=1
        j+=1
    print()
    i+=1
