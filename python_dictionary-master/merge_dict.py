d1={"a":100,"b":200,"c":300}
d2={"a":300,"b":200,"d":400}
s={}
for key in d1:
    for key2 in d2:
        sum=0
        if key==key2:
            sum+=d1[key]+d2[key2]
            a=({key:sum})  
            s.update(a)    
# print(key,d1[key])
b=({key:d1[key]})
s.update(b)
# print(key2,d2[key2])
c=({key2:d2[key2]})
s.update(c)
# print(a)
print(s)