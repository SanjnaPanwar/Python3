user=input("enter something:")
user2=input("enter :")
lenuser=len(user)
lenuser2=len(user2)
def length():
    if lenuser>lenuser2:
        print(user)
    elif lenuser<lenuser2:
        print(user2)
    elif lenuser==lenuser2:
        print(user,"\n",user2)
length()