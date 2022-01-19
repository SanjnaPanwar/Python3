# import string library function 
import string 
    
# An input string.
Sentence = "Hey, laddu !, How are you?"
c=0
for i in Sentence:
      
    # checking whether the whitespace is present 
    if i in string.whitespace:
        c+=1
# Printing the whitespace values 
print("printable Value is: " + i,c)
