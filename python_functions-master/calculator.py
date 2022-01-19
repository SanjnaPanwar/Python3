# 1st part
def calculator(number_x,number_y,operations):
    if operations=="add":
        return number_x+number_y
    elif operations=="subtract":
        return number_x-number_y
    elif operations=="multiplication":
        return number_x*number_y       
    else:
        return number_x/number_y    
sum=calculator(20,25,"add")
print(sum)
subtract=calculator(40,3,"subtract")
print(subtract)
multiply=calculator(10,4,"multiplication")
print(multiply)
division=calculator(40,4,"division")
print(division)
num_1=calculator(24,20,"add")
num_2=calculator(50,60,"subtract")
num_3=calculator(80,120,"multiply")
num_4=calculator(90,23,"division")
print(num_1,"\n",num_2,"\n",num_3,"\n",num_4)

# 2nd part
num1=int(input("enter 1st num.:"))
num2=int(input("enter 2nd num.:"))
add_result=calculator(num1,num2,"add")
print(add_result)
subtract_result =calculator(num1,num2,"subtract")
print(subtract_result )
multiply_result=calculator(num1,num2,"multiplication")
print(multiply_result)
divide_result=calculator(num1,num2,"division")
print(divide_result)