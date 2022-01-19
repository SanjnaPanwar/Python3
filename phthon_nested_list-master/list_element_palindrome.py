a=["ladal","mom","sanas","lakl","laddu","manam","nitin"]
i=0
while i<len(a):
    d=a[i]    
    j=1
    c=''
    while j<=len(d):
        c+=d[-j]
        j+=1
    if a[i]==c:
        print(i,"yes palindrome")
    else:
        print(i,"no")  
    i+=1
