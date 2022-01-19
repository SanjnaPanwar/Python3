dict1={1:['samal',21,'data structure','ssism'],
        2:['richie',20,'machine learning','ssism'],
        3:['laurence',23,'oops with java','ssism']
    }
for key,value in dict1.items():
  # print("name", '\t'  "age", '\t'  "course", '\t'   "collage")
  for key,value in dict1.items():
    name,age,course,collage=value
    # print("name","age","course","collage")
    print("name", '\t'  "age", '\t'  "course", '\t'   "collage")
    print(value)
