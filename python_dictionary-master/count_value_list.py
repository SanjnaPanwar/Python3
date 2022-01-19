dict =  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']
   }
count=0
for i in dict:
    if type(dict[i])==list:
        for j in dict[i]:
            count+=1
            print(j)
print(count)