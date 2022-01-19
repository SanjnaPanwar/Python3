a={"sanjna":34,"laddu":5,"sam":43}
b={}
for i in a.keys():
    # print(float(i))
    for j in a.values():
        b.update({i:float(j)})
        print(b)