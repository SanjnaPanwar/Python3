file=open("people1-exercise.txt","r")
count=0
for i in file:
    count+=1
print(count)
file.close