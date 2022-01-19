def split():
    a=['Red', 'Maroon', 'Yellow', 'Olive']
    b=[]
    i=0
    while i<len(a):
        j=0
        c=[]
        while j<len(a[i]):
            c.append(a[i][j])
            j+=1
        b.append(c)
        i+=1
    print(b)
split()