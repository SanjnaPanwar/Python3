num=[1,2,3,4,5,6,7,8,9,10]
even=[]
odd=[]
for nums in num:
    if nums%2==0:
        even.append(nums)        
    else: 
        odd.append(nums)
print(even)
print(odd)