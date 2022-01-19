print("to calculate the electricity bill")
unit=int(input("enter units:"))
amount=float(input("enter amount:"))
if unit<=50:
    print("amount=",unit*0.50)
elif unit<=150:
    print("amount=",25+(unit-50)*0.75)
elif unit<=250: 
    print("amount=",a=100+(unit-150)*1.20) 
elif unit<=350:
    print("amount=",220+(unit-250)*1.50)
surcharge=amount*0.2
totalamount=amount+surcharge 
print("electricity bill=Rs  0.2%",totalamount)
