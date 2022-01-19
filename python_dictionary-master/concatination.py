# list1=["one","two","three","four","five"]
# list2=[1,2,3,4,5,]
# a={} 
# for i in list1:
#     for j in list2:
#         a[i]=j
#         list2.remove(j)
#         break
# print(str(a))



# s={'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56}
# a={'python':20,"gaurav":300,'dev':34,"karan":43}
# c={}
# for i in (s,a):
#     c.update(i)
# print(c)


dict1={1:2,2:3,3:4,4:5}
sum=0
for i in dict1.values():
    sum+=i
print(sum)


# sum=0
# for i in dict1:    
#     sum+=dict1[i]
# print(sum)