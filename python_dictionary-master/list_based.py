# A key-value list pairings of the said dictionary:
# [{1: 'Jean Castro', 2: 'Lula Powell', 3: 'Brian Howell', 4: 'Lynne Foster', 5: 'Zachary Simon'}]

a=['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['ZacharySimon']}
b={}
for i in a:
    if type(a[i])==list:
        for j in range(len(a[i])):
            b.update({i:a[i][j]})
print(b)
