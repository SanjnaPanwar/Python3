places=["delhi",45, "gujrat", "rajasthan", "punjab", "kerala"]
a=[]
for i in range((len(places)-1),-1,-1):              
    a.append(places[i])
print(*a,sep="\n")  #(* symbol is use to print the list elements in a single line
                    # with space. To print all elements in new lines or separated by space use sep=”\n” or sep=”, ” respectively.)



# print(places[::-1])

  
