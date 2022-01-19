a=[
     {"first":"1"}, 
     {"second": "2"}, 
     {"third": "1"}, 
     {"four": "5"}, 
     {"five":"5"}, 
     {"six":"9"},
     {"seven":"7"}
]                                          
res= set()            #res = list(set(val for dic in a for val in dic.values()))
for key in a:
    for val in key.values():
        res.add(val)
print(list(res))

# s = set()             #  s = set( val for dic in lis for val in dic.values())
# for dic in a:
#    for val in dic.values():
#       s.add(val)
# print(list(s))