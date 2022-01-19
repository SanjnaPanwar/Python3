# multiple_list = [[5, 10, 50, 20], [2, 20, 3, 5]]
# def calculator(number_x,number_y,operations):
#     if operations=="add":
#         return number_x+number_y
#     elif operations=="subtract":
#         return number_x-number_y
#     elif operations=="multiplication":
#         return number_x*number_y       
#     else:
#         return number_x/number_y 


def list_change(): 
    multiple_list = [[5, 10, 50, 20],[2, 20, 3, 5]]    
    c=[]
    pro=0
    i=0
    while i <len(multiple_list):
        j=0 
        while j <len(multiple_list[i]):
            pro*=multiple_list[j][i]*multiple_list[j][i]
            c.append(pro)
            j+=1
        i+=1
    print(c)

