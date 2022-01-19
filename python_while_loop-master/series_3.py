# Ek program banao jo 1 se 100 tak ke numbers ke saath yeh kare:

#    1. Jo 3 se divisible hain unki jagah "Nav" print kare

#    2. Jo 7 se divisible hain unki jagah "Gurukul" print kare

#    3. Jo 3 aur 7 dono se divisible hain, unki jagah "NavGurukul" print karein

#   4.  Jo upar wale teen cases mein nahi aate, unki jagah sirf number print karvao.
i=0
while i<=100:
    if i%3==0 :
        print("Nav")
    elif i%7==0:
        print("Gurukul")
    elif i%3==0 and i%7==0:
        print("NavGurukul") 
    else:
        print(i)
    i+=1  
       