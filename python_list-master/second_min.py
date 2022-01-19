number=[50,40,23,70,3,56,12,5,10,7]
i=0
min=number[i]
smin=number[i]
while i<len(number):
    if number[i]<min:
        min=number[i]
    elif number[i]<smin and number[i]>min:
        smin=number[i]
    i+=1
print(min)
print(smin)


