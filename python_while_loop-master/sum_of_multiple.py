i=30
sum=0
while i<=420:
    if i%8==0:    #calculate sum of multiple of 8
        sum=sum+i
        print(sum)
    i+=1
print(sum) 


# dry run
# i=30   sum=0  whilei<=420  if i%8==0    sum=sum+i print(sum)  i+=1 
# i=30     0     0<=420      if 30%8==0   sum=0         -       i=30+1=31
# i=31     0    30<=420     if 31%8==0 F       -        -       i=31+1=32
# i=32     0    32<=420     if 32%8==0 T  sum=0+32=32   32      i=32+1=33
# i=33
# i=34
# i=35
# i=36
# i=37
# i=38
# i=39
# i=40     32   40<=420    if 40%8==0 T   sum=32+40=72   72     i=40+1=42
# .      
# .
# .
# sum=10976