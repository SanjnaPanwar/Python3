# w.a.p.to print rever odd numbers between 50 t0 100, 
# initilization value is 400
i=400
while i>=350:
  z=i-300
  if z%2!=0:
    print(z)
  i=i-1

# i=400    i>=350    z=i-300        if z%2!=0   print?(z)  i=i-1
# i=400    400>350   z=400-300=100  100%2!=0 F     -       i=400-1=399                                                   i=400-1=399
# i=399    399>=350  z=399-300=99   99%2!=0  T     99      i=399-1=398
# i=398    398>=350  z=398-300=98   98%2!=0  F      -      i=398-1=397
# i=397    397>=350  z=397-300=97   97%2!=0  T     97      i=397-1=396
# .
# .
# i=350    350>=350  z=350-300=50   50%2!=0  F     -       i=350-1=349
# i=349    349>=350 F   