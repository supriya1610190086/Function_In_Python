def eligble_for_vote(age):
    if age<18:
        print("Not eligible")
    else:
        print("You are eligible")
eligble_for_vote(int(input("enter the age")))