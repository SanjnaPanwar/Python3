elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
evensum=0
oddsum=0
i=0
while i<len(elements):
    if elements[i]%2==0:
        evensum=evensum+elements[i]
    else:    
        oddsum=oddsum+elements[i]
    i+=1
print(evensum)
print(oddsum)
