weight=0
for i in range(11):
    user=float(input('enter your weight:'))
    weight=weight+user
a=weight/11
print(a)    
if a%5==0:
    print("age is multiple of 5")
else:
    print("a is not multiple of 5")    