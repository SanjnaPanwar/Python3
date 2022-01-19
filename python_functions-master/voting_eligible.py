age=int(input("enter your age:"))
def eligible_for_vote():
    if age < 18:
        print("not eligible for vote")
    else:
        print("eligible for voting")
eligible_for_vote()