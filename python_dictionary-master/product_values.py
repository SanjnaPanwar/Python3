dict1={1:2,2:3,3:4,4:5}
product=1
for i in dict1.values():
    product*=i
print(product)

## 2nd way
# product=1
# for i in dict1:    
#     product*=dict1[i]
# print(product)