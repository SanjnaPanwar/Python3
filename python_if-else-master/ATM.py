balance=50000
print("please insert your atm card")
language="eng"
language=input("please select your language:")
if language =="eng":                       
        pin="1234"
        if pin=="1234":
           userpin=input("please enter your pin:")
           choice=int(input("please enter choice:1.cheack balance/2.withdraw/3.deposit/4.exit:"))
           if choice==1:
               print("your available balance is",balance)
           elif choice==2:
               withdraw=float(input("please enter amount to withdraw:"))
               if balance>withdraw:
                  total=balance-withdraw
                  print("please collect/yes :)")
                  print("your available balance is",total)
               else:  
                  print("insufficient amount to withdraw")
           elif choice==3:
               deposit=float(input("enter amount to deposite:"))
               total=balance+deposit
               print("successfully deposite")
               print("your balance is",total)
           elif choice==4:
               print("don't want to do anything or exit")
        else:                                                                             
            print("your pin is incorrect")                                              
else: 
        print("your selected language is incorrect,please enter again.")
       