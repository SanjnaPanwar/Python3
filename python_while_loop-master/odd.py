# 50 to 100 tak ke sare odd number ko print kro?


i = 50
while i <= 100:
    if i % 2 != 0:
       print(i)
    i = i + 1


# dry run
# i=50  i<=100  if i%2!=0  print(i)  i=i+1
#                                    i=50+1=51
# i=51  51<=100   51%2!=0   51       i=51+1=52
# i=52  52<=100   52%2!=0   -        i=52+1=53
# i=53  53<=100   53%2!=0   53       i=53+1=54
# i=54  54<=100   54%2!=0   -        i=54+1=55
# i=55  55<=100   55%2!=0   55       i=55+1=56
# .
# .
# i=100 100<=100 100%2!=0   -       i=100+1=101
# i=101 101<=100 F