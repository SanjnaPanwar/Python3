i=12
total=0
while i<=421:
    total=total+i
    print(total)
    i+=1
print(total)

# i=12  total=0  i<=421   total=total+i   print(total)  i+=1
# i=12    0      12<=421 T  total=0+12=12    12         i=12+1=13
# i=13    12     13<=421 T  total=12+13=25   25         i=13+1=14
# i=14    25     13<=421 T  total=25+14=39   39         i=14+1=15
# .
# .
# .
# total=88765