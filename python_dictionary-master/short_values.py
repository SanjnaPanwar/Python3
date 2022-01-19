a={'sanjna':32,'laddu':21,'sadu':33}
for i in a:                  
  for j in a:
    if a[i]>a[j]:
      tem=a[i]
      a[i]=a[j]
      a[j]=tem
print(a)
