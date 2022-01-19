day=input("enter today's name :")
time=input("breakfast/dinner")
if day=="monday":
    if time=="breakfast":
        print("poha")
    else:
        print("roti sabji")
elif day=="tuesday":
    if time=="breakfast":
        print("fried gram")
    else:
        print("dal roti")
elif day=="wednesday":
    if time=="breakfast":
        print("mango shake") 
    else:
         print("pulao")
elif day=="thursday":
    if time=="breakfast":
        print ("oats") 
    else:
        print("puri sabji")
elif day=="friday":
    if time=="breakfast":
        print("sprauts")
    else:
        print("rajma and roti")
elif day=="saturday":
    if time=="breakfast":
        print("idli")
    else:
        print("rajma chawal")
else:
    print("you enter wrong day name")