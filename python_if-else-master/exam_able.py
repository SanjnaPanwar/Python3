total=int(input("enter total class:"))
attend=int(input("enter attended class:"))
if total>=attend:
    a=(attend/total)*100
    if a>=50:
        print("yes able to give exam")
    else:
        print("not able to give exm")
else:
    print("invalid total class")
