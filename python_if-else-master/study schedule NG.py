time=float(input("enter time:"))
if time>=6 and time<=7:
    print("it's time to do some exercise")
elif time>=7 and time<9 :
    print("it is the time for breakfast/ready")
elif time>=9 and time<10 :
    print("it is the time of english activity")
elif time>=10 and time<=13:
    print("it is the coding time")
elif time>=13 and time<14.30:    
    print("it's break time/lunch time")
elif time>=14.30 and time<17:
    print("again coding time")
elif time>=17 and time<=18.30: 
    print("time to culture activity")
elif time>=18.30 and time<19:
    print("it is break time/snacks time")
elif time>=19 and time<21:
    print("it is night coding time")
elif time>=21 and time<22:
    print("it is dinner time ")
elif time>=22 and time<23:
    print("it's chill/walk time") 
elif time>=23 and time<6:
    print("it's time to take proper rest/sleep")         
else:
    print("invalid input")