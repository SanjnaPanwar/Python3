# 1 se 50 ke beech ke saare 5 ke multiples print karo.
#  Lekin aapko % (modulous operator) ka use nahi karna hai. Uske bina karo.
i=0
while i<=50:
    if i!=0:
        print(i)
    i=i+5


    # dry run
    # i=0   i<=50  if i!=0   print(i)  i=i+5  
    #                                 i=0+5=5
    # i=5   5<=50   5!=0 T    5        i=5+5=10
    # i=10  10<=50  10!=0     10       i=10+5=15
    # i=15  15<=50  15!=0     15       i=15+5=20
    # .
    # .
    # i=50  50<=50  50!=0     50       i=50+5=55
    # i=55  55<50 F