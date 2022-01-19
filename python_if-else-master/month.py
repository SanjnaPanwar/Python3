month=input("enter month name/no.:")
if month=="january" or month=="1" or month=="march" or month=="3" or month=="may" or month=="5" or month=="july" or month=="7" or month=="august" or month=="8" or month=="october" or month=="10" or month=="december" or month=="12":
    print("31 days in this month")
elif month=="february" or month=="2":
       year=int(input("please enter year:"))
       if year%4==0 and (not year %100==0) or year%400==0: 
           print("it is a leap year")  
       else:
           print("it is not a leap year") 
elif month=="april" or month=="4" or month=="june" or month=="6" or month=="september" or month=="9" or month=="november" or month=="11":
    print("30 days in this month")
else:
    print("you enter wrong month name;)")           