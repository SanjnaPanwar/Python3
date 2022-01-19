name=["one","two","three","four","five"]
print(len(name))
name.append("xyz") #append items at the end
print(name)
name.insert(2,"abc")  #insert items at specific value
print(name)

name.remove("abc")  #remove and item
print(name)
name[3]="per"  #update an item at specific position
print(name)
name2=["xyz"]
print(name2)

name3=name + name2  #concatenate list
print(name3)