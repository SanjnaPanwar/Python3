def prime(limit):
    for i in range(2,limit):
            if limit%i==0 :
                print("it is notprime")
                break
    else:
        print(" prime")             
prime(5)
