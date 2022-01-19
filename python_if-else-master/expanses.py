number_of_student=int(input(("enter number of student:")))
expense_of_student=float(input("enter expense amount of student:"))
a=(number_of_student*expense_of_student)
print("total amount",a)
if a<=50000:
    print("Hum budget ke andar hain")
else:
    print("hum budget ke bahar hain")
