# import json
# # a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }

# # convert into JSON:
# y = json.dumps(x)

# # the result is a JSON string:
# print(y) 

# import json

# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None)) 


# Python program to convert 
# Python to JSON 
     
     
# import json 
     
# # # Data to be written 
# dictionary ={ 
#   "id": "04", 
#   "name": "sunil", 
#   "depatment": "HR"
# } 
     
# # Serializing json  
# json_object = json.dumps(dictionary) 
# print(json_object)

# Python program to write JSON
# to a file
   
   
# import json
   
# # Data to be written
# dictionary ={
#     "name" : "sathiyajith",
#     "rollno" : 56,
#     "cgpa" : 8.6,
#     "phonenumber" : "9976770500"
# }
   
# with open("sample.json", "w") as outfile:
#     json.dump(dictionary, outfile)
# print(dictionary)



# import json
  
# data = {
#     "name": "Satyam kumar",
#     "place": "patna",
#     "skills": [
#         "Raspberry pi",
#         "Machine Learning",
#         "Web Development"
#     ],
#     "email": "xyz@gmail.com",
#     "projects": [
#         "Python Data Mining",
#         "Python Data Science"
#     ]
# }
# with open( "data_file.json" , "w" ) as write:
#     json.dump( data , write )

# with open("data_file.json", "r") as read_content:
#     print(json.load(read_content))


import json 
    
# JSON string: 
# Multi-line string 
data = """{ 
    "Name": "Jennifer Smith", 
    "Contact Number": 7867567898, 
    "Email": "jen123@gmail.com", 
    "Hobbies":["Reading", "Sketching", "Horse Riding"] 
    }"""
    
# parse data: 
res = json.loads( data ) 
    
# the result is a Python dictionary: 
print( res )