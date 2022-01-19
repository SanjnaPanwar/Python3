import json
list1=["neelam","programer",24,2400]
key1=["name","designation","age","salary"]
emp1={}
for key in (key1):
    for value in list1:
        emp1[key]=value
        list1.remove(value)
        break
# print(emp1)
list2=["komal","trainer",24,20000]
key1=["name","designation","age","salary"]
emp2={}
for key in (key1):
    for value in list2:
        emp2[key]=value
        list2.remove(value)
        break
# print(emp2)
list3=["anuradha","HR",25,40000]
key1=["name","designation","age","salary"]
emp3={}
for key in (key1):
    for value in list3:
        emp3[key]=value
        list3.remove(value)
        break
# print(emp3)
list4=["Abhishek","manager",29,63000]
key1=["name","designation","age","salary"]
emp4={}
for key in (key1):
    for value in list4:
        emp4[key]=value
        list4.remove(value)
        break
# print(emp4)
data={"emp1":emp1,"emp2":emp2,"emp3":emp3,"emp4":emp4}
with open( "employee_details.json" , "w" ) as write:
    json.dump(data, write,indent=4 )














# listdetail=[
#     ["neelam","programer",24,2400],
#     ["komal","trainer",24,20000],
#     ["anuradha","HR",25,40000],
#     ["Abhishek","manager",29,63000]  
# ]
# key1=["name","designation","age","salary"]
# key2=["emp1","emp2","emp3","emp4"]
# dic1={}
# dic2={}
# for k in range(len(key2)):
#     for i in range(len(listdetail)):
#         for j in range(len(listdetail[i])):
#             for key in key1:
#                 dic1.update({key:listdetail[i][j]})
#                 print(dic1)