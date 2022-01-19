# Nested dictionary:
# [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}},
# {'S004': {'Saim Richards': 92}}]

a=['S001', 'S002', 'S003', 'S004']
b=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
c=[85, 98, 89, 92]
d={}
for i in range(len(a)):
    e={}
    for j in range(len(b)):
        if i==j:
            e.update({b[j]:c[j]})
    d.update({a[i]:e})
print(d)
