size=int(input("enter size how much you want square:"))
a={}
for i in range(size):
    keys=int(input("enter your keys:"))
    a.update({keys:keys*keys})
    print(a)


# #2nd way
c=dict()
for i in range(1,16):
    c.update({i:i*i})
print(c) 