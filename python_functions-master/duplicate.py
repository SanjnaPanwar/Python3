

def duplicate_element():  
    mark=[]
    size=int(input("enter size of list:"))
    for i in range(size):
        element=int(input("enter your element of list:"))
        mark.append(element)
    i=0
    list1=[]
    while i<len(mark):
        j=0
        count=0
        while j<len(mark):
            if mark[i]==mark[j]:
                count+=1
            j+=1
        if mark[i] in list1:
            i+=1
            continue
        list1.append(mark[i])
        print(mark[i],"=",count)
    print(list1)
duplicate_element()