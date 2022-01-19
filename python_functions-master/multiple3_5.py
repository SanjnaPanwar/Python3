def multiples(limit):
    sum=0
    for i in range(limit):
        if i%3==0 or i%5==0:
            sum+=i
    print(sum)
multiples(10)
