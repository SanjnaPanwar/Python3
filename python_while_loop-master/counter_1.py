# Ek program banao jo 1 se 100 tak ke beech mein woh 
# numbers print kare jo 7 se divide ho jaate hain.
# Note: Aap jo loop likhoge uska counter 556 se start hona chaiye.
i=556
while i<=656:
    a=i-555
    if a%7==0:
        print(a)
    i+=1 


# i=556  while i<=656  a=i-555      if a%7==0  print(a)    i=i+1
# i=556  556<=656      a=556-555=1   1%7==0      -         i=556+1=557
# i=557  557<=656      a=557-555=2   2%7==0      -         i=557+1=558
# .
# .
# i=562  562<=656      a=562-555=7   7%7==0      7         i=562+1=563
# .
# .
# i=569  569<=656      a=569-555=14  14%7==0     14        i=569+1=570
# .
# .
# i=576  576<=656      a=576-555=21  21%7==0     21        i=576+1=577
# .
# .
# .
# .
# .
# .
# .
# .
# .
# .i=656  656<=656   a=656-555=101      F