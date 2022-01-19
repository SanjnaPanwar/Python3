dict={
    "name":"Raju",
    "marks":56
    }
user=input("enter key:")
for key in dict.keys():
    # if user=="name":
    if user in dict.keys():
        print("exist")
        break
    else:
        print("not exist")
        break