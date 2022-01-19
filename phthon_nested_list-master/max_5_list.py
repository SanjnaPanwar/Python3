
a=[[12,34,56,43],[56,57,68,97],[32,33,65,107],[45,67,89,87],[65,67,7,66]]
for i in range (len(a)):
    max=0
    for j in a[i]:
        if j>max:
            max=j
    print(max) 
