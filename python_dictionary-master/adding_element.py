dic= {
    'Name': 'RAM', 
    'Age': 17,
    }
dic['ORGANIZATION'] = "NAV GURUKUL"
dic['place'] = 'dharamsala'
print(dic)


# question-2
dic= {
    'Name': 'RAM',
    'Age': 17,
     }
dic['student']={
        'id':22, 
        'place':'dharamsala'
    }
print(dic)


# question-3
car ={
    "brand":  "ford",
    "model":  "mustang",
    "year":  1964
}
if "model" in car:
    print("Yes, 'model' is one of the keys in the car dictionary.")
else:
    print("No, 'model' key dictionary mai nahi hai.")