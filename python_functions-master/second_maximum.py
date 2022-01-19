def secondmaximum(): 
    mark=[]
    size=int(input("enter size of list:"))
    for i in range(size):
        element=int(input("enter elements of your list:"))
        mark.append(element)
        i=0
        max=mark[i]
        smax=mark[i]
        while i <len(mark):
            if mark[i]>max:
                max=mark[i]
            elif mark[i]>smax and mark[i]<max:
                smax=mark[i]
            i+=1
    print(max)
    print(smax)
secondmaximum()