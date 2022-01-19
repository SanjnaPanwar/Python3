speed=float(input("enter your speed:"))
def driver_speed(speed):
    if speed==70 :
       print("ok")
    elif speed>=70:
        a=speed-70
        point=a/5
        if point>12:
            print(point,"license suspended")
driver_speed(speed)
    
