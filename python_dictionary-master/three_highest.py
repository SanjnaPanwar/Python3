my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }
a=[]
for i in my_dict.values():
    a.append(i)
p=sorted(a)
q=1
w=[]
while q <=3:
    w.append(p[-q])
    q+=1
print(w)
    
