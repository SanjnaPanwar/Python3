# count
# sum
# average
# even 
# odd
# evensum
# oddsum
elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
evensum=0
oddsum=0
count=0
i=0
while i<len(elements):
    if elements[i]%2==0:
        evensum=evensum+elements[i]
    else:    
        oddsum=oddsum+elements[i]
    i+=1
    count+=1
print("count",count)
print("sum of even",evensum)
print("sum of odd",oddsum)
even=[]
odd=[]
for nums in elements:
    if nums%2==0:
        even.append(nums)        
    else: 
        odd.append(nums)
print("even",even)
print("odd",odd)
i=0
sum=0
while i<len(elements):
    sum=sum+elements[i]
    i+=1
print("sum of elements of list",sum)
print("average of list",sum/count)