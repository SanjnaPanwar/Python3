def minimum():
    mark=[]
    size=int(input("enter size of list:"))
    for i in range(size):
        element=int(input("enter your element of list:"))
        mark.append(element)
    i=0
    b=mark[i]
    while i>size:
        j=mark[i]
        if j>b:   
            b=j
        i=i+1
    print(b,"min")
minimum()
